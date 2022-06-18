from pyfund.main import Purchase, AssetEnum, Account, History
import pytest


@pytest.fixture
def purchases():
    return [
        Purchase(AssetEnum.GOLD, 1734.34, Account.UNKNOWN),
        Purchase(AssetEnum.SILVER, 123.34, Account.SUPERBROKER),
    ]


def test_purchase(purchases):
    assert (
        purchases[0].__repr__()
        == "On 2022-06-18 you bought 1.0 oz of gold for 1734.34 EUR using your UNKNOWN account."
    )
    assert (
        purchases[1].__repr__()
        == "On 2022-06-18 you bought 1.0 oz of silver for 123.34 EUR using your SuperBroker account."
    )


def test_history(purchases):
    h = History(purchases)
    assert (
        h.__repr__()
        == "On 2022-06-18 you bought 1.0 oz of gold for 1734.34 EUR using your UNKNOWN account."
        + "\n"
        + "On 2022-06-18 you bought 1.0 oz of silver for 123.34 EUR using your SuperBroker account."
    )
