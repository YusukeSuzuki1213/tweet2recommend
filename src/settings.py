import os
from dotenv import load_dotenv

load_dotenv()

# KEY
TWITTER_CONSUMER_TOKEN = os.getenv('TWITTER_CONSUMER_TOKEN', None)
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET', None)
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', None)
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET', None)

if TWITTER_CONSUMER_TOKEN is None:
    print('Specify TWITTER_CONSUMER_TOKEN as environment variable.')
    os.sys.exit(1)

if TWITTER_CONSUMER_SECRET is None:
    print('Specify TWITTER_CONSUMER_SECRET as environment variable.')
    os.sys.exit(1)

if TWITTER_ACCESS_TOKEN is None:
    print('Specify TWITTER_ACCESS_TOKEN as environment variable.')
    os.sys.exit(1)

if TWITTER_ACCESS_SECRET is None:
    print('Specify TWITTER_ACCESS_SECRET as environment variable.')
    os.sys.exit(1)


# TWITTER ACCOUNT
# USER_ID_1 = os.getenv('USER_ID_1', None)
# USER_ID_2 = os.getenv('USER_ID_2', None)
USER_ID_TEST = os.getenv('USER_ID_TEST', None)

""" if USER_ID_1 is None:
    print('Specify USER_ID_1 as environment variable.')
    os.sys.exit(1)

if USER_ID_2 is None:
    print('Specify USER_ID_2 as environment variable.')
    os.sys.exit(1) """

if USER_ID_TEST is None:
    print('Specify USER_ID_TEST as environment variable.')
    os.sys.exit(1)

FOLLOWED_USER_LIST = [
    # USER_ID_1,
    # USER_ID_2,
    USER_ID_TEST
]
