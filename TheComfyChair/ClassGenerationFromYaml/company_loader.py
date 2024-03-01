# company_loader.py
import yaml
from protocols import Settings, Company
from settings import SETTINGS
from company import CompanyModel
from beartype import beartype


@beartype
def get_companies(settings: Settings):
    with open(settings.base_dir / "companies.yaml", "rb") as fp:
        return yaml.load(fp, Loader=get_loader())


# company_loader.py
@beartype
def get_loader() -> type[yaml.SafeLoader]:
    loader = yaml.SafeLoader
    loader.add_constructor("!Company", company_constructor)
    return loader


# company_loader.py
@beartype
def company_constructor(
    loader: yaml.SafeLoader,
    node: yaml.nodes.MappingNode,
) -> Company:
    """Construct an employee."""
    _node = {}

    def process_node(node) -> None:
        for _n in node.value:
            attr_name, attr_value = _n
            if isinstance(attr_name, yaml.MappingNode):
                process_node(attr_name)
            _node[attr_name.value] = ""
            _cast: str = attr_value.tag.split(":")[-1]
            if _cast in ["bool", "int"]:
                _node[attr_name.value] = eval(attr_value.value)
            elif _cast == "seq":
                _node[attr_name.value] = [item.value for item in attr_value.value]
            elif _cast == "map":
                _node[attr_name.value] = {}
                _node[attr_name.value].update(
                    {
                        (key.value, val.value)
                        for (key, val) in [item for item in attr_value.value]
                    },
                )
            else:
                _node[attr_name.value] = attr_value.value

    process_node(node)
    return CompanyModel(**_node)  # type: ignore
