from typing import Any, Optional
import tweepy
from settings import (
    TWITTER_CONSUMER_TOKEN,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET,
    FOLLOWED_USER_LIST
)


class TweepyApi:
    __instance = None

    @staticmethod
    def get_instance() -> Optional['TweepyApi']:
        if TweepyApi.__instance is None:
            TweepyApi()
        return TweepyApi.__instance

    def __init__(self):
        if TweepyApi.__instance is not None:
            raise Exception("Do not call")
        else:
            self.api = self.__create_api()
            TweepyApi.__instance = self

    def __create_api(self) -> tweepy.API:
        auth = tweepy.OAuthHandler(
            TWITTER_CONSUMER_TOKEN, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        return tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status: Any):
        if(self.__should_reply(status)):
            reply_text = "@{}\n{}".format(status.user.screen_name, "テスト")
            tweet_id = status.id_str
            self.__reply(reply_text, tweet_id)

    def on_error(self, status_code: int):
        if status_code == 420:
            print("Error")
            return False

    def __should_reply(self, status: Any) -> bool:
        return True if (
            hasattr(status, 'user') and (status.user is not None) and
            hasattr(status.user, 'screen_name') and (status.user.screen_name is not None) and
            hasattr(status, 'id_str') and (status.id_str is not None) and
            hasattr(status.user, 'id_str') and (status.user.id_str in FOLLOWED_USER_LIST) and
            hasattr(status, 'in_reply_to_status_id') and (status.in_reply_to_status_id is None) and
            hasattr(status, 'in_reply_to_status_id') and (status.in_reply_to_user_id is None) and
            hasattr(status, 'is_quote_status') and (status.is_quote_status is False) and
            not hasattr(status, 'retweeted_status')
        ) else False

    def __reply(self, reply_text: str, tweet_id: str) -> None:
        if (tweepyApi := TweepyApi.get_instance()) is None:
            raise Exception('Can not get instance of TweetApi')
        else:
            print(f'id: {reply_text}')
            print(f'tweet_id: {tweet_id}')
            tweepyApi.api.update_status(reply_text, tweet_id)


def main() -> None:
    if (tweepyApi := TweepyApi.get_instance()) is None:
        raise Exception('Can not get instance of TweetApi')
    else:
        listener = MyStreamListener()
        stream = tweepy.Stream(auth=tweepyApi.api.auth, listener=listener)
        stream.filter(follow=FOLLOWED_USER_LIST, is_async=True)


if __name__ == '__main__':
    main()
