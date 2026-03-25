"""
This scripts publishes TDs to a TDD
"""

import logging
from time import sleep

import requests

from wot_td_datasets.generate import DataSets, td_datasets


def put_to_tdd(
    tdd_hostname: str,
    tdd_port: int,
    dataset_selection: DataSets = DataSets.CUSTOM
    | DataSets.KINDER
    | DataSets.WEB_THINGS,
):
    """
    Puts selected datasets to the specified TDD server.

    Args:
        tdd_hostname (str): The hostname or IP address of the target TDD server.
        tdd_port (int): The port number used to connect to the TDD server.
        dataset_selection (DataSets, optional): A bitwise flag combination
            indicating which datasets to use. Defaults to a combination of
            CUSTOM, KINDER, and WEB_THINGS.

    Returns:
        None
    """
    logger = logging.getLogger(__name__)

    things_list = td_datasets(dataset_selection)
    for thing in things_list:
        td = thing.td()

        url = f"http://{tdd_hostname}:{tdd_port}/things/{td.id}"
        payload = td.model_dump_json(
            exclude_none=True,
            by_alias=True,
            indent=2,
            exclude={"properties": {"*": "title"}},
        )
        headers = {"Content-Type": "application/json"}

        response = requests.request(
            "PUT", url, headers=headers, data=payload, timeout=15
        )

        if response.status_code not in [201, 204]:
            logger.error(
                "Something went wrong while publishing %s to the TDD located at %s, response: %s",
                td.id,
                url,
                response,
            )
        sleep(20.0 / 1000.0)
    logger.info("Published %s TDs to the TDD", len(things_list))


if __name__ == "__main__":
    put_to_tdd("localhost", 8082, DataSets.CUSTOM)
