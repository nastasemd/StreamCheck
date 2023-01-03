import requests
from urllib.request import Request

# Twitch api log-in
TWITCH_STREAM_API_ENDPOINT_V5 = "https://api.twitch.tv/helix/search/channels?query=bikestreaming"
reqSession = requests.Session()

# Keeping tokens hidden in a separate file
# file has 2 lines (on the first there's the client id and on the second the client secret)
file = open("C:/Tkey.txt", "r")
tokens = file.readlines()
client_id = tokens[0].strip()
client_secret = tokens[1].strip()
file.close()

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)

#data output
keys = r.json()

API_HEADERS = {
    'Client-ID' : client_id,
    'Authorization': 'Bearer ' + keys['access_token'],
}

# Streamer who you want to check
streamer_name = 'osulive'
stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=API_HEADERS)
stream_data = stream.json()

# If stream is offline stream_data['data'] is []
if len(stream_data['data']) == 1:
    print('Stream is online!')
else:
    print('Stream is offline.')
