import re

def process_city_state_zip(city_part, state_zip_part, parsed_address_dict):
    city_pattern = r"^(.*)$"
    state_pattern = r"([A-Za-z]{2})$"
    zip_pattern = r"(\d{5})$"

    city = city_part.strip()
    if re.match(city_pattern, city):
        parsed_address_dict["city"] = city


    state_zip_parts = state_zip_part.split()
    for part in state_zip_parts:
        part = part.strip()
        if re.match(state_pattern, part):
            parsed_address_dict["state"] = part.upper()
        elif re.match(zip_pattern, part):
            parsed_address_dict["zip_code"] = part