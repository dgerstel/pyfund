import datetime
from dataclasses import dataclass
from typing import Optional, Sequence
from enum import Enum
import sys
print(sys.path)
from pyfund.config import config


enum_dict = {}
for k, v in vars(config).items():
    enum_dict[k] = {a.upper(): a for a in v}
AssetEnum = Enum("Assets", enum_dict["assets"])
Account = Enum("Account", enum_dict["accounts"])
Currency = Enum("Currency", enum_dict["currencies"])
ASSET_AND_UNIT = {a: config.asset_to_unit[a] for a in config.assets}


@dataclass
class Asset:
    """Asset with its unit and current price."""

    name: AssetEnum
    current_price: Optional[int] = None

    def __post_init__(self):
        print("For name", self.name, "TYpe of name:", type(self.name))
        self.unit = config.asset_to_unit[self.name.value]

    def __repr__(self):
        return self.name.value


@dataclass
class Purchase:
    """Represents a purchase of an asset."""

    asset_enum: AssetEnum
    price: float
    account: Account = Account.UNKNOWN
    qty: float = 1.0
    date: datetime.datetime = datetime.date.today()
    currency: Currency = Currency.EUR

    def __post_init__(self):
        self.asset: Asset = Asset(self.asset_enum)

    def __repr__(self):
        return (
            f"On {self.date} you bought {self.qty} {self.asset.unit} of {self.asset} for {self.price} {self.currency.value} "
            + f"using your {self.account.value} account."
        )


@dataclass
class History:
    """History is a list of purchases."""

    purchase_arr: Sequence[Purchase]

    def __repr__(self):
        return "\n".join([p.__repr__() for p in self.purchase_arr])

    def total_cost(self):
        return sum(p.price for p in self.purchase_arr)


def main():
    p = Purchase(AssetEnum.GOLD, 1734.34, Account.UNKNOWN)
    print(p)

    p2 = Purchase(AssetEnum.SILVER, 123.34, Account.SUPERBROKER)
    print(p2)

    h = History([p, p2])
    print(h)
    print(h.total_cost())

    print(config.assets)


if __name__ == "__main__":
    main()
