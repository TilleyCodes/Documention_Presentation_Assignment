# pylint: disable=missing-docstring
# pylint: disable=trailing-whitespace

from classes.currency_converter_live_rate import CurrencyConverterLiveRate

# # This function is testing the conversion calculation with the live rate
def test_convert_rate(monkeypatch):

    # pylint: disable-next=unused-argument
    def mock_get_live_rate(self, base_currency, currency, api_key):
        return 0.5
   
    monkeypatch.setattr(CurrencyConverterLiveRate, "get_live_rate", mock_get_live_rate )
    converter = CurrencyConverterLiveRate()

    result = converter.convert_currency("AUD", "USD", 200)
    assert result is not None

    (converted_amount, rate) = result 
    assert converted_amount == 100
    assert rate == 0.5
