from dataclasses import dataclass
from pathlib import Path
from strictyaml import load, YAML
from typing import List, Dict


DIR = Path(__file__).parent.resolve()


@dataclass
class Config:
    currencies: List[str]
    accounts: List[str]
    assets: List[str]
    asset_to_unit: Dict[str, str]


def fetch_config_from_yaml(cfg_path: Path = DIR / "config.yml") -> YAML:
    """Parse yaml containing the configuration."""
    with open(cfg_path, "r") as cf:
        return load(cf.read())


def create_config(parsed_config: YAML = None) -> Config:
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    return Config(**parsed_config.data)


config = create_config()
if __name__ == "__main__":
    config = create_config()
    print(config)