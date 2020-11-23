from lyricsgenius import Genius
import random,re
import tweepy
from requests.exceptions import HTTPError, Timeout
from lyricsgenius import Genius
from decouple import config

CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')
GENIUS_TOKEN = config('GENIUS_TOKEN')

genius = Genius(GENIUS_TOKEN)


####################fUNCTION TO GET TITLE OF SONG #####################

def get_title():
    # genius_api()
    artist = genius.search_artist('Bastille', max_songs=0)
    rand_page = random.randint(1,4)
    request = genius.artist_songs(
        artist._id, sort='popularity', per_page=50, page=rand_page)


    random_song = random.randint(0,len(request['songs']))

   
    title = request['songs'][random_song]['title']
    print(title)
    return title



def get_lyrics():

    title = get_title()
    song = genius.search_song(title, 'Bastille')
    
    try:
        song.lyrics
        ##### copy response to a string and remove unnecessary characters using regex
        lyrics = str(song.lyrics)
        regex = r"\[\w+.+\]"
        subst = ''
        result = re.sub(regex, subst, lyrics, 0, re.MULTILINE)

        split = result.split('\n')
        #print(split)
        #print(result)
        ####Filter out all empty strings in the split list
        res = list(filter(('').__ne__, split))
        print('length of lyrics is :', len(res))
        if len(res) < 10:
            
            print('This song is too short,so i tried again')
            get_lyrics()
        else:
            #print(res)

            #### get a random number thats length of lyrics list and print our random lines using the index
            random_lyric = random.randint(0, len(res))

            print(res[random_lyric])
            one_liner = res[random_lyric]
            auth = tweepy.OAuthHandler(CONSUMER_KEY,
                               CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)

            api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
            
            try:
                api.verify_credentials()
                print("Authentication OK")
                # print(one_liner)
                api.update_status(one_liner +' @ayanniranj , @bastille_bot')
            except:
        
                print("Error during authentication")

    except HTTPError as e:
        print(e.errno)    # status code
        print(e.args[0])  # status code
        print(e.args[1])  # error message
        get_lyrics()
    except Timeout:
        get_lyrics()
    exit()
        
    
get_lyrics()
