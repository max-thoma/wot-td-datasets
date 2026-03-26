import asyncio
import logging

from amqtt.client import ConnectError, MQTTClient

from wot_td_datasets.generate import DataSets, td_datasets
from wot_td_datasets.mock import generate_device_message_log

logger = logging.getLogger(__name__)


async def emulate_client(thing) -> None:
    client_id = thing.td().id
    client = MQTTClient(client_id=client_id)
    try:
        await client.connect("mqtt://localhost:1883/")
    except ConnectError as con:
        logger.error(con)
        return

    publish_task = []
    logs = generate_device_message_log(thing=thing)
    for log in logs.logs:
        for log_ in log.logs:
            topic_ = log_.topic
            payload_ = log_.payload.encode("utf-8")
            retain_ = log_.retain
            publish_task.append(
                asyncio.ensure_future(
                    client.publish(topic=topic_, message=payload_, retain=retain_)
                )
            )
    await asyncio.wait(publish_task)

    await client.disconnect()


async def run_tasks(things):

    tasks = []
    for thing in things:
        tasks.append(asyncio.ensure_future(emulate_client(thing)))

    await asyncio.wait(tasks)


def main():
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)

    asyncio.run(run_tasks(td_datasets(DataSets.CUSTOM)))


if __name__ == "__main__":
    main()
