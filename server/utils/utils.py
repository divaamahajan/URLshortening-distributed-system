import random

MAX_LEN = 7

def create_short_url():
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = random.choice(range(1, MAX_LEN + 1))
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url
