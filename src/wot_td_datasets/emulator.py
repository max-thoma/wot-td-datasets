"""
Emulate the IoT devices and publish the message log
"""

import asyncio
import logging
from itertools import cycle

from amqtt.client import ConnectError, MQTTClient

import wot_td_datasets.td
from wot_td_datasets.generate import DataSets, td_datasets
from wot_td_datasets.mock import generate_device_message_log

logger = logging.getLogger("emulator.py")


async def emulate_client(thing, sleep) -> None:
    """
    Emulate the IoT device and publish the message log.

    Each device can generate a message log by calling `generate_device_message_log`.
    This function returns an a `DeviceMessageLog` object. A `DeviceMessageLog`
    holds a list of MessageLogList. Each MessageLogList is a list of MessageLog;
    i.e., logs: List[List[MessageLog]]. Hence, each affordance has a list of message logs.
    In one iteration, each affordance publishes one message from the log, then it sleeps for `sleep` seconds.

    """
    client_id = thing.td().id
    client = MQTTClient(client_id=client_id)
    try:
        await client.connect("mqtt://localhost:1883/")
    except ConnectError as con:
        logger.error(con)
        return

    logs = generate_device_message_log(thing=thing)
    log_cycle = [cycle(logs.logs) for logs in logs.logs]
    log_pool = cycle(log_cycle)

    try:
        while True:
            publish_task = []
            for _ in range(len(log_cycle)):
                cycle_iter = next(log_pool)
                next_log = next(cycle_iter)
                publish_task.append(
                    asyncio.ensure_future(
                        client.publish(
                            topic=next_log.topic,
                            message=next_log.payload.encode("utf-8"),
                            retain=next_log.retain,
                        )
                    )
                )
            await asyncio.wait(publish_task)
            await asyncio.sleep(delay=sleep)
    except asyncio.CancelledError:
        await client.disconnect()
        raise


async def run_tasks(things, sleep):
    tasks = []
    for thing in things:
        tasks.append(asyncio.ensure_future(emulate_client(thing, sleep)))

    try:
        await asyncio.wait(tasks)
    except asyncio.CancelledError:
        logger.info("Task cancled sucessfully")


def emulate_dataset(
    dataset_selection: DataSets = DataSets.CUSTOM
    | DataSets.KINDER
    | DataSets.WEB_THINGS,
    sleep: int = 10,
):
    formatter = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)

    asyncio.run(run_tasks(td_datasets(dataset_selection), sleep))


def emulate_thing(thing, sleep: int = 10):
    formatter = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)

    asyncio.run(run_tasks([thing], sleep))


if __name__ == "__main__":
    wot_td_datasets.td.MESSAGE_NUM = 1
    emulate_dataset(sleep=10)
