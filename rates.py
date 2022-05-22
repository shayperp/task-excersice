import requests
import configuration
import mock


def get_api_key():
    return configuration.API_KEY


def get_headers():
    return {
        "apikey": get_api_key()
    }


def get_mock_data():
    return mock.MOCK_DATA


def get_all_rates():
    try:
        response = requests.request("GET", configuration.LATEST_RATES_URL, headers=get_headers(), data={})
    except Exception as e:
        print(e)
        return None
    if response.status_code == 200:
        return response.json()
    return None


def get_rates_with_limit(limit=configuration.limit):
    limited_rate_names = []
    rates_response = get_mock_data() if configuration.environment == 'dev' else get_all_rates()
    if not rates_response:
        print("ERROR getting rates data")
        return None
    rates = rates_response['rates']
    for rate_name, rate_value in rates.items():
        if rate_value < limit:
            limited_rate_names.append(rate_name)
    print(f"All rate names lower than {limit}:")
    print(limited_rate_names)
    return limited_rate_names


get_rates_with_limit()