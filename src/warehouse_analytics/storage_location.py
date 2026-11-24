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
    return StorageLocation(aisle=parts[0], rack=parts[1], slot=parts[2], level=parts[3])
