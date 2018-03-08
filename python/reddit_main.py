# http://wwwpythonforbeginnerscom/api/how-to-use-reddit-api-in-python

import requests
import requests.auth
import praw
import os


class SubReddit(object):
    def __init__(self):
        self.config = self.__get_env_config()
        self.reddit = None  # defined by set_praw
        self.subreddit = None  # defined by set_subreddit

    @staticmethod
    def __get_env_config():
        env_keys = [
            "REDDIT_CLIENT_ID",
            "REDDIT_SECRET",
            "REDDIT_USERNAME",
            "REDDIT_PASSWORD",
            "REDDIT_USER_AGENT"
        ]
        return {
            key: os.getenv(key)
            for key in env_keys
        }

    @staticmethod
    def __get_reddit_object(config):
        return praw.Reddit(
            client_id=config.get("REDDIT_CLIENT_ID"),
            client_secret=config.get("REDDIT_SECRET"),
            password=config["REDDIT_PASSWORD"],
            user_agent=config["REDDIT_USER_AGENT"],
            username=config["REDDIT_USERNAME"]
        )

    @staticmethod
    def __sub2dict(sub, fields):
        return {
            field: getattr(sub, field)
            for field in fields
        }

    @staticmethod
    def top_submissions_dict(submissions, fields):
        return [
            SubReddit.__sub2dict(sub, fields)
            for sub in submissions
        ]

    def set_praw(self):
        self.reddit = self.__get_reddit_object(config=self.config)

    def set_subreddit(self, subreddit_name):
        self.subreddit = self.reddit.subreddit(subreddit_name)

    def top_submissions(self, n=5, time='day'):
        return self.subreddit.top(time_filter=time, limit=n)


def subreddit_top_submission_nsj(subreddit, fields, n=10):
    sr = SubReddit()
    sr.set_praw()
    sr.set_subreddit(subreddit_name=subreddit)
    submissions = sr.top_submissions(n=n)
    return sr.top_submissions_dict(submissions=submissions, fields=fields)