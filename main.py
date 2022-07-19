from typing import Union, Optional
from datetime import datetime

from art import tprint

from src import Core
from config import Config, logger


def main(date: Union[str, datetime, int]) -> Optional:
    """
    Run the parser script
    :param date: Date to search. Example: 12.12.2021 or 1639256400
    """
    core = Core()
    logger.error((
        "START CHECK THE CSV FILE:\n"
        "PATH TO THEM:\n"
        f"SERVER FILE: {Config.SERVER_FILE}\n"
        f"CLIENT FILE: {Config.CLIENT_FILE}\n"
        f"CHEATERS DB: {Config.CHEATERS_DB_PATH}\n"
    ))
    server_data, client_data = core.get_data_by_time(date)
    if len(server_data) == 0 and len(client_data) == 0:
        logger.error("NOTHING FOUND! TRY ANOTHER DATE")
        return
    elif len(server_data) == 0 and len(client_data) > 0:
        logger.warning(
            "THE CLIENT DATA WAS FOUND, BUT THE DATA FOR THE SERVER IS NOT! SO I CAN'T POPULATE THE DATABASE!"
        )
        return [player.to_dict for player in client_data]
    elif len(server_data) > 0 and len(client_data) == 0:
        logger.warning("THE SERVER DATA WAS FOUND, BUT THE CLIENT DATA WAS NOT! SO I CAN'T POPULATE THE DATABASE!")
        return [server.to_dict for server in server_data]
    else:
        logger.info("DATA FOR THIS DATE WAS SUCCESSFULLY FOUND! STARTING UNION!!")
        data = core.merge_data(server_data=server_data, client_data=client_data)
        if len(data) == 0:
            logger.error("DATA HAS NOT BEEN COMBINED! SOMETHING WENT WRONG!")
            return None
        logger.info("DATA WAS SUCCESSFULLY LUNCHED! STARTING WRITE IN THE DATABASE!")
        status = core.add_to_database(general_data=data)
        if not status:
            logger.error("THE DATA WAS NOT INTRODUCED TO THE BASE! SOMETHING WENT WRONG!")
        else:
            logger.info("THE DATA WAS SUCCESSFULLY INTRODUCED TO THE DATABASE!")


if __name__ == '__main__':
    """Run parser"""
    tprint("PARSER SCRIPT", font="bulbhead")
    data = main(input(
        "Enter date:\n"
        "Example: 12.12.2021 || 1639256400\n\n>>>"
    ))
    if not isinstance(data, bool) or data is not None:
        print("\n\n")
        print(data)
