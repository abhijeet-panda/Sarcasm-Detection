from birdy.twitter import UserClient
import time
import urllib
import re
import json


class MyClient(UserClient):
    @staticmethod
    def get_json_object_hook(data):
        return data

client = MyClient('W99kl3NLCRLin1lio9KRw49II',
		  'D2AIDYcr7l9hn8eOGzvLzJVlnbUnpXSrkpD7A97s2p27XgjWPC',
		  '218518385-upmc1W1IoOLCJYcnIHScgOs6yG9e08dvDfW8q7JP',
		  'fHi9i3XAJt4Nrb6PJvOQMBvGCZS65YEsDPcTjOIUFcBQK')


response = client.api['statuses']['show'].get(id='598682860187332609')

print response.data

