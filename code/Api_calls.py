import pandas as pd
import requests
import config
import time



# starting off by gaining access to the reddit API


auth = requests.auth.HTTPBasicAuth(config.Client_ID, config.Secret_Key)

data = {
    'grant_type': 'password',
    'username': config.auth1,
    'password': config.auth2
}

headers = {
    'User-Agent': 'MyAPI/0.0.1'
    }

#----------------------------------------------

# Now I am getting token access to the API


TOKEN_ACCESS = 'https://www.reddit.com/api/v1/access_token'
res = requests.post(TOKEN_ACCESS, 
                   auth=auth, data=data, headers=headers)

if res.status_code == 200:
    TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'


#----------------------------------------------

# In the function I want to 
# make getting posts easier
# by not hardcoding the parameters
# and by combining the dataframes into one




def get_posts(endpoint, sort, after=None, limit=100):

   
    params = {
            'q': query,
            'type': 'posts',
            'restrict_sr': 'on',
            'sort': sort,
            't': 'all',
            'limit': limit,
            'after': after
        }

    all_posts = []  

#----------------------------------------------
    # part about pagination that I will use to get more posts
    
    while True:

        params['after'] = after

        response = requests.get(endpoint, headers=headers, params=params, allow_redirects=False)
        data_json = response.json()

        if 'data' not in data_json or 'children' not in data_json['data']:
            break

        posts = data_json['data']['children']
        all_posts.extend(posts)

        after = data_json['data'].get('after')

        if not after or len(all_posts) >= 1000:
            break
        
        time.sleep(2)

    return all_posts

#----------------------------------------------
# query = ' title:"this game is" OR title:"I love" OR title:"I hate" OR title:"I like" OR title:"Unpopular Opinion" OR title:"best"\
# OR title:"I love this game" OR title:"This game is the best" OR title:"This game is the worst" OR title:"This game is bad" \
# OR title:"This game is good" OR title:"I hate this game" OR title:"I like this game" OR title:"good" OR title:"bad" OR title:"bug"\
# OR title:"regret" OR title:"error" OR title:"amazing" OR title:"worst" OR title:"I wish" OR selftext:"I hate" OR selftext:"I love"\
# OR selftext:"I like" OR selftext:"the worst" OR selftext:" I regret" '

query = ' title:("I lov*" OR "I like" OR "best" OR "I love this game" OR "This game is the best" OR "This game is good" OR "I like this game" OR "good" OR "amazing") \
OR title:("this game is" OR "Unpopular Opinion" OR "regret" OR "I wish" OR "This game needs") \
OR title:("I hate" OR "This game is the worst" OR "This game is ba*" OR "I hate this game" OR "ba*" OR "There is a bug" OR "This bug" OR "error" OR "worst") \
OR selftext:("I lov*" OR "I lik*") OR selftext:("I hate" OR "the worst" OR "I regret" OR "difficul*") '

endpoint = 'https://oauth.reddit.com/r/Sims4/search/'

# Combine all posts into one list 
top_posts = get_posts(endpoint, 'top')
hot_posts = get_posts(endpoint, 'hot')
new_posts = get_posts(endpoint, 'new')

combine = top_posts + hot_posts + new_posts

#----------------------------------------------

# Now I want to place data into a pandas dataframe
# and combinine the dataframes into one


df = pd.DataFrame([{
    'title': post['data']['title'],
    'selftext': post['data']['selftext'],
    'upvote_ratio': post['data']['upvote_ratio'],
    'ups': post['data']['ups'],
    'downs': post['data']['downs'],
    'score': post['data']['score'],
    'date': post['data']['created_utc']
} for post in combine])


#----------------------------------------------
# Importing into a streamlit so I
# can view the data better


#st.title("Sims 4 Subreddit Data")

df = df.to_csv("Sims4_data.csv", index=False)

