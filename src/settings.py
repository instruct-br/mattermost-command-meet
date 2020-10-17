from decouple import config


DEBUG = config("DEBUG", default=False)
MATTERMOST_TOKEN = config("MATTERMOST_TOKEN")
GOOGLE_MEET_URL = "http://g.co/meet/"
