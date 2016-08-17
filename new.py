from twython import Twython
api = Twython('W99kl3NLCRLin1lio9KRw49II',
		  'D2AIDYcr7l9hn8eOGzvLzJVlnbUnpXSrkpD7A97s2p27XgjWPC',
		  '218518385-upmc1W1IoOLCJYcnIHScgOs6yG9e08dvDfW8q7JP',
		  'fHi9i3XAJt4Nrb6PJvOQMBvGCZS65YEsDPcTjOIUFcBQK')
print api.search(q='#sarcasm')