import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence


class AssetEnum(Enum):
    GOLD = "gold"
    SILVER = "silver"


class Unit(Enum):
    OZ = "oz"


ASSET_AND_UNIT = {
    AssetEnum.GOLD: Unit.OZ,
    AssetEnum.SILVER: Unit.OZ,
}


@dataclass
class Asset:
    """Asset with its unit and current price."""

    name: AssetEnum
    current_price: Optional[int] = None

    def __post_init__(self):
        self.unit = ASSET_AND_UNIT[self.name]

    def __repr__(self):
        return self.name.value


class Account(Enum):
    UNKNOWN = "UNKNOWN"
    SUPERBROKER = "SuperBroker"
    DEGIRO = "DEGIRO"


class Currency(Enum):
    EUR = "EUR"
    USD = "usd"
    PLN = "pln"


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
            f"On {self.date} you bought {self.qty} {self.asset.unit.value} of {self.asset} for {self.price} {self.currency.value} "
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


if __name__ == "__main__":
    main()
