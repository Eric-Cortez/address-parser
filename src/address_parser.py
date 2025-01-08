import re
from src.utils import process_city_state_zip


def parse_address(address):
    address = address.strip()

    parsed_address_dict = {
        "recipient": "",
        "street_address": "",
        "city": "",
        "state": "",
        "zip_code": "",
    }

    lines = address.splitlines()

    if len(lines) >= 2:
        # tests against correctly formatted address
        parsed_address_dict["recipient"] = lines[0].strip()
        parsed_address_dict["street_address"] = lines[1].strip()

        street_city_state_zip = lines[-1].strip()

        parts = street_city_state_zip.split(",")

        if len(parts) == 2:
            process_city_state_zip(parts[0], parts[1], parsed_address_dict)



    return parsed_address_dict