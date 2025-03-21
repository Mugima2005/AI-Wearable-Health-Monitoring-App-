import requests
url = "https://api.spikeapi.com/metrics/calories/?user_id=282812818&start_date=2020-05-01&end_date=2020-05-03"
headers = {}
headers['x-spike-auth'] = 'fa0b3803-1111-2222-9788-eccce210d30c'
response = requests.request("GET", url, headers=headers)
print(response.text)