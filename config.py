# import os,logging,tweepy
# from lyricsgenius import Genius
# logger = logging.getLogger()
# from bastille_lyrics_bot.pipenv.cfg import sources

consumer_key = "zGWJqwwVeeSUpZOCzoPPizJsW"
consumer_secret = "aYwBovKyIAkIITqHEkmbSMLQsvzwPkqfLrl4ocUuCju2Q0sxL0"

access_token = "859696097329115137-mnBsnbA476W0fKiKgCUiXhnjBrXNL8F"
access_token_secret = "FhafrV1LjRVWAKk6UI1NxbfZsLsFWtAfrkGW0jbp5kHUr"

genius_token = "as-1fvSOQSRFWMq4JJxLYrpGjh_c8wlO-hL1Kzjwx7tbB_FAsg21zMFJMu7LdNaF"

# def genius_api():
#     genius_token = os.environ("GENIUS_TOKEN")
    
#     # genius = Genius(
#     #     "as-1fvSOQSRFWMq4JJxLYrpGjh_c8wlO-hL1Kzjwx7tbB_FAsg21zMFJMu7LdNaF")
#     genius = Genius(GENIUS_TOKEN)

# def create_api():
#     twitter_consumer_key = os.environ("CONSUMER_KEY")
#     twitter_consumer_secret = os.environ("CONSUMER_SECRET")
#     twitter_access_token = os.environ("ACCESS_TOKEN")
#     twitter_access_token_secret = os.environ("ACCESS_TOKEN_SECRET")
   

    
    
#     # auth = tweepy.OAuthHandler("zGWJqwwVeeSUpZOCzoPPizJsW",
#     #                            "aYwBovKyIAkIITqHEkmbSMLQsvzwPkqfLrl4ocUuCju2Q0sxL0")
#     auth = tweepy.OAuthHandler(CONSUMER_KEY,
#                                CONSUMER_SECRET)
#     # auth.set_access_token("859696097329115137-mnBsnbA476W0fKiKgCUiXhnjBrXNL8F",
#     #                       "FhafrV1LjRVWAKk6UI1NxbfZsLsFWtAfrkGW0jbp5kHUr")
#     auth.set_access_token(ACCESS_TOKEN,
#                          ACCESS_TOKEN_SECRET)

#     api = tweepy.API(auth, wait_on_rate_limit=True,
#                      wait_on_rate_limit_notify=True)

#     try:
#         api.verify_credentials()
#     except Exception as e:
#         logger.error("Error creating api",exc_info = True)
#         raise e
#     logger.info("api created")
#     return api
