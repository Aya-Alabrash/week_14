import requests

# Retrieve COVID-19 cases information
def get_covid_cases(country):
    api_url = 'https://api.api-ninjas.com/v1/covid19?country={}'.format(country)
    
    # You need to replease `API_KEY` with your own Api_key from your account.
    response = requests.get(api_url, headers={'X-Api-Key': 'API_KEY'})
  
    if response.status_code == requests.codes.ok:
        data = response.json()
        country_name = data[0]['country']
        latest_cases = data[0]['cases']['2023-03-09']['total']
        return f"COVID-19 latest cases in {country_name}: {latest_cases}\n"
    else:
        print("Error:", response.status_code, response.text)
