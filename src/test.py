import tweepy

# override tweepy.StreamListener to add logic to on_status


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


def main():
    listener = MyStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=listener)


def auth():
    auth = tweepy.OAuthHandler(consumer_token, consumer_secre)


if __name__ == '__main__':
    main()
