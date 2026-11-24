from dataclasses import dataclass


@dataclass
class StorageLocation:
    aisle: str
    rack: str
    slot: str
    level: str


def parse_location_code(code: str) -> StorageLocation:
    parts = code.split("-")
    aisle = parts[0]
    if len(parts) != 4:
        raise ValueError(
            f"Invalid location code '{code}': expected 4 parts, got {len(parts)}"
        )
    if len(aisle) != 1 or not aisle.isalpha() or not aisle.isupper():
        raise ValueError(f"Invalid aisle '{aisle}': expected one uppercase letters")
    return StorageLocation(aisle=aisle, rack=parts[1], slot=parts[2], level=parts[3])
