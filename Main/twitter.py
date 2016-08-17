from pattern.web import Twitter, plaintext

twitter = Twitter(language='en')
for tweet in twitter.search('"#irony"', cached=False):
 print plaintext(tweet.text) 
