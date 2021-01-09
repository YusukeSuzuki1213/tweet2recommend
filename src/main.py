from typing import Any
import tweepy
from settings import (
    TWITTER_CONSUMER_TOKEN,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET,
    FOLLOWED_USER_LIST
)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status: Any):
        print(status.text)
        print(status)

    def on_error(self, status_code: int):
        if status_code == 420:
            return False


def get_auth() -> tweepy.OAuthHandler:
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_TOKEN, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    return auth


def main() -> None:
    listener = MyStreamListener()
    auth = get_auth()
    stream = tweepy.Stream(auth=auth, listener=listener)
    stream.filter(follow=FOLLOWED_USER_LIST, is_async=True)


if __name__ == '__main__':
    main()
