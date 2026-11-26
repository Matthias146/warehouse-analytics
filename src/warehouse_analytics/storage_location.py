from dataclasses import dataclass


@dataclass
class StorageLocation:
    aisle: str
    rack: str
    slot: str
    level: str

    def to_code(self) -> str:
        return f"{self.aisle}-{self.rack}-{self.slot}-{self.level}"


def _check_number(name: str, value: str, digits: int, max_value: int) -> None:
    if (
        len(value) != digits
        or not value.isascii()
        or not value.isdigit()
        or not 1 <= int(value) <= max_value
    ):
        raise ValueError(
            f"Invalid {name} '{value}': expected {digits} digit from 1 to {max_value}"
        )


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
    if len(aisle) != 1 or not "A" <= aisle <= "Z":
        raise ValueError(f"Invalid aisle '{aisle}': expected one uppercase letter")
    _check_number("rack", rack, digits=2, max_value=99)
    _check_number("slot", slot, digits=2, max_value=99)
    _check_number("level", level, digits=1, max_value=6)
    return StorageLocation(aisle=aisle, rack=rack, slot=slot, level=level)
