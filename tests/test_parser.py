import pytest
from src.address_parser import parse_address

mock_addresses = [
    ("Sonic\n2260 Apollo Way\nSanta Rosa, CA 95407", {
        "recipient_name": "Sonic",
        "street_address": "2260 Apollo Way",
        "city": "Santa Rosa",
        "state": "CA",
        "zip_code": "95407",
    }),
    ("john doe\n123 elm street\nLOS ANGELES, ca 90001", {
        "recipient_name": "john doe",
        "street_address": "123 elm street",
        "city": "LOS ANGELES",
        "state": "ca",
        "zip_code": "90001",
    }),
    ("PO Box 5678\n1234 Market St\nSan Francisco, CA 94105", {
        "recipient_name": "PO Box 5678",
        "street_address": "1234 Market St",
        "city": "San Francisco",
        "state": "CA",
        "zip_code": "94105",
    }),
    ("Sir Tim Berners-Lee\n1234 Innovation Way\nSanta Rosa, CA 95407", {
        "recipient_name": "Sir Tim Berners-Lee",
        "street_address": "1234 Innovation Way",
        "city": "Santa Rosa",
        "state": "CA",
        "zip_code": "95407",
    }),
]

@pytest.mark.parametrize("address, expected", mock_addresses)
def test_parse_address(address, expected):
    parsed = parse_address(address.strip())

    assert parsed["recipient_name"] == expected["recipient_name"]
    assert parsed["street_address"] == expected["street_address"]
    assert parsed["city"] == expected["city"]
    assert parsed["state"] == expected["state"]
    assert parsed["zip_code"] == expected["zip_code"]

