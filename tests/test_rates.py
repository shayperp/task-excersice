import configuration
import mock
import rates


def test_get_rates_with_limit_api_error(requests_mock):
    configuration.environment = 'prod'
    requests_mock.get(configuration.LATEST_RATES_URL, status_code=500)
    res = rates.get_rates_with_limit(configuration.limit)
    assert res is None


def test_get_rates_lower_than_10(requests_mock):
    configuration.environment = 'dev'
    requests_mock.get(configuration.LATEST_RATES_URL, json=mock.MOCK_DATA, status_code=200)
    res = rates.get_rates_with_limit(configuration.limit)
    assert len(res) == 68
    assert res == ['AED', 'ANG', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN', 'BHD', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BYN', 'BZD', 'CAD', 'CHF', 'CLF', 'CNY', 'CUC', 'DKK', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GTQ', 'HKD', 'HRK', 'ILS', 'IMP', 'JEP', 'JOD', 'KWD', 'KYD', 'LTL', 'LVL', 'LYD', 'MOP', 'MYR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PLN', 'QAR', 'RON', 'SAR', 'SBD', 'SGD', 'SHP', 'SVC', 'TMT', 'TND', 'TOP', 'TTD', 'USD', 'WST', 'XAG', 'XAU', 'XCD', 'XDR']

