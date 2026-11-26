from dataclasses import dataclass


@dataclass
class StorageLocation:
    aisle: str
    rack: str
    slot: str
    level: str


def parse_location_code(code: str) -> StorageLocation:
    parts = code.split("-")
    if len(parts) != 4:
        raise ValueError(
            f"Invalid location code '{code}': expected 4 parts, got {len(parts)}"
        )
    aisle = parts[0]
    rack = parts[1]
    if len(aisle) != 1 or not aisle.isalpha() or not aisle.isupper():
        raise ValueError(f"Invalid aisle '{aisle}': expected one uppercase letter")
    if len(rack) != 2 or not rack.isdigit() or not 1 <= int(rack) <= 99:
        raise ValueError(f"Invalid rack '{rack}': expected 2 digits from 01 to 99")
    return StorageLocation(aisle=aisle, rack=rack, slot=parts[2], level=parts[3])
