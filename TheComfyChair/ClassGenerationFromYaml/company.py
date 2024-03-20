# company.py
from dataclasses import dataclass, field


@dataclass
class CompanyModel:
    company_name: str = field(default="")
    active: bool = False
    has_dimensions: bool = False
    dimensions: list = field(default_factory=list)
    file_mapping: dict = field(default_factory=dict)
    bi_central_uuid: str = field(default="")
