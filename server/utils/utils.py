import random
import subprocess
import json

MAX_LEN = 6
DNS = "localhost:8000"
print("DNS:", DNS)

def create_short_url():
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = random.choice(range(1, MAX_LEN + 1))
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url
