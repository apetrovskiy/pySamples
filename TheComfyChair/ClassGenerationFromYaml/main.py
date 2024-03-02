from typing import Protocol
from company_loader import get_companies
from protocols import Settings

# settings = protoc
get_companies(settings=Settings())
