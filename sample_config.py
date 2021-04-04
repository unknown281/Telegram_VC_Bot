HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"])
    OWNER_ID = int(environ["OWNER_ID"])
    SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 2368867
    API_HASH = 198659d0a1c5dd61f6eb404ce1bd026e
    SUDO_CHAT_ID = 1001185921197
    OWNER_ID = 772197858


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
