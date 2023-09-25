from typing import Dict, Any, List
from bson.json_util import dumps
from json import loads

import tweepy

from src.secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from src.conection import users_collection


def get_user(user_name) -> Dict[str, Any]:
    """Get user infos from Twitter API.
    Args:
        user_name (str): Identifier user by screen_name
     Returns:
        Dict[str, Any]: User infos
    """

    auth = tweepy.OAuthHandler(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    user = api.get_user(screen_name=user_name)

    user_info = {'id': user.id,
                 'name': user.name,
                 'screen_name': user.screen_name,
                 'created_at': user.created_at,
                 'followers_count': user.followers_count,
                 'friends_count': user.friends_count,
                 'favourites_count': user.favourites_count,
                 'statuses_count': user.statuses_count,
                 'profile_image_url_https': user.profile_image_url_https,
                 'profile_background_image_url_https': user.profile_background_image_url_https,
                 }
    
    return user_info


def save_user(user_name) -> None:
    """Save user infos on MongoDB.
    Args:
        user_name (str): Identifier user by screen_name
    """

    add_user = get_user(user_name=user_name)
    users_collection.insert_one(add_user)


def get_db_user(screen_name) -> List[Dict[str, Any]]:
    """Get user infos persisted in MongoDB.
    Args:
        screen_name (str): Identifier user by screen_name
     Returns:
        List[Dict[str, Any]]: User infos
    """

    cursor = users_collection.find({"screen_name": screen_name})
    json_result = dumps(cursor)
    dict_list_user = loads(json_result)

    return dict_list_user
