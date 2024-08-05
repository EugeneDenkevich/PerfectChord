from datetime import timedelta

ACCESS_EXPIRATION = timedelta(minutes=20)
SECRET_KEY_EXPIRATION = timedelta(minutes=30)
REFRESH_EXPIRATION = timedelta(days=30)
LIMIT_REFRESH_TOKENS = 5
