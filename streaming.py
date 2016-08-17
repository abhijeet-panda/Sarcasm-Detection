from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

stream = MyStreamer('W99kl3NLCRLin1lio9KRw49II',
		  'D2AIDYcr7l9hn8eOGzvLzJVlnbUnpXSrkpD7A97s2p27XgjWPC',
		  '218518385-upmc1W1IoOLCJYcnIHScgOs6yG9e08dvDfW8q7JP',
		  'fHi9i3XAJt4Nrb6PJvOQMBvGCZS65YEsDPcTjOIUFcBQK')

stream.statuses.filter(track='#joke')