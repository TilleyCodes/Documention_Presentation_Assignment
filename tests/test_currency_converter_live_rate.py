# pylint: disable=missing-docstring
# pylint: disable=trailing-whitespace

from classes.currency_converter_live_rate import CurrencyConverterLiveRate

def test_convert_rate(monkeypatch):
    """
    Tests the convert_currency method of CurrencyConverterLiveRate using a mocked live rate.

    Mocks the get_live_rate method to return a fixed exchange rate. Ensures that 
    convert_currency calculates the correct converted amount and rate.

    Args:
        monkeypatch: A pytest fixture for modifying or replacing methods or attributes.
    """

    # pylint: disable-next=unused-argument
    def mock_get_live_rate(self, base_currency, currency, api_key):
        return 0.5
    
    # Using a mocked live rate
    monkeypatch.setattr(CurrencyConverterLiveRate, "get_live_rate", mock_get_live_rate )
    converter = CurrencyConverterLiveRate()

    result = converter.convert_currency("AUD", "USD", 200)
    assert result is not None

    (converted_amount, rate) = result 
    assert converted_amount == 100
    assert rate == 0.5