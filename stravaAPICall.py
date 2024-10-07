import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "YOUR CLIENT_ID",
    'client_secret': 'YOUR_SECRET_ID',
    'refresh_token': 'YOUR_REFRESH_TOKEN',
    'grant_type': "refresh_token",
    'f': "json"
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activities_url, headers=header, params=param).json()
print(my_dataset[0]['name'])
print(my_dataset[0]['type'])
