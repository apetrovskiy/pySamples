# protocols.py
from typing import Protocol
from pathlib import Path
from beartype import typing


@typing.runtime_checkable
class Settings(Protocol):
    base_dir: Path


@typing.runtime_checkable
class Company(Protocol):
    company_name: str
    active: bool
    has_dimensions: bool
    dimensions: list
    file_mapping: dict
    bi_central_uuid: str
