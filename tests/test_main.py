from pyfund.main import Purchase, AssetEnum, Account
import pytest


@pytest.mark.parametrize(
    "asset_enum,price,account_enum,expected_str",
    [
        (AssetEnum.GOLD, 1734.34, Account.UNKNOWN,
         "On 2022-06-18 you bought 1.0 oz of gold for 1734.34 EUR using your UNKNOWN account."),
        (AssetEnum.SILVER, 123.34, Account.SUPERBROKER,
         "On 2022-06-18 you bought 1.0 oz of silver for 123.34 EUR using your SuperBroker account."),
    ]
)
def test_purchase(asset_enum, price, account_enum, expected_str):
    p = Purchase(asset_enum, price, account_enum)
    assert p.__repr__() == expected_str
