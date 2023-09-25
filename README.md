# Dio Twitter API with Tweepy and FastAPI

This repository contains a simple API integration with Twitter using Tweepy, FastAPI and MongoDB in Python. The project is part of the [Digital Innovation One](https://web.dio.me) bootcamp.


## Introduction

This project demonstrates how to integrate with the Twitter API using Tweepy and create a web API using FastAPI in Python. It provides basic functionalities to interact with the Twitter API, including searching for user of twitter.

## Features

- Search for a twitter user based on a specific query.

## Requirements

- [Python](https://www.python.org) (>= 3.8)
- [Tweepy](https://docs.tweepy.org/en/stable/) (lib for Twitter API)
- [FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [MongoDB](https://www.mongodb.com/pt-br) (In this project was used MongoDB Atlas)
- [Twitter Developer Acount](https://developer.twitter.com/en) (for API access)


## Usage

- Set up your Twitter API credentials and MongoDB connection:
```code
CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_TOKEN_SECRET"
BEARER_TOKEN = "YOUR_BEARER_TOKEN"

URI = "YOUR_MONGODB_URI"
```
- Run the application:
```bash
python main.py
```

## Author

[Miguel Mendes Serrano](https://github.com/miguelmendesSerrano)


## License

This project is licensed under the [MIT License.](https://choosealicense.com/licenses/mit)