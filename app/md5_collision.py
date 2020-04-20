import hashlib
import time
from app.collisions import generate_random_string, find_collisions


def create_collisions_md5():
    results = {}
    timeout = time.time() + 60*1.5
    while time.time() <= timeout:
        string = generate_random_string()
        hashed = hashlib.md5(string.encode('utf-8'))

        if not results.get(hashed):
            results[hashed] = []

        results[hashed].append(string)

    return find_collisions(results)
