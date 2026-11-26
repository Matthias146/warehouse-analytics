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
    slot = parts[2]
    level = parts[3]
    if len(aisle) != 1 or not "A" <= aisle <= "Z" or not aisle.isupper():
        raise ValueError(f"Invalid aisle '{aisle}': expected one uppercase letter")
    if len(rack) != 2 or not rack.isdigit() or not 1 <= int(rack) <= 99:
        raise ValueError(f"Invalid rack '{rack}': expected 2 digits from 01 to 99")
    if len(slot) != 2 or not slot.isdigit() or not 1 <= int(slot) <= 99:
        raise ValueError(f"Invalid slot '{slot}': expected 2 digits from 01 to 99")
    if len(level) != 1 or not level.isdigit() or not 1 <= int(level) <= 6:
        raise ValueError(f"Invalid level '{level}': expected 1 digit from 1 to 6")
    return StorageLocation(aisle=aisle, rack=rack, slot=slot, level=level)
