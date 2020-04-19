import random

from app.hashing import check_sum


def generate_random_string():
    return ''.join([str(random.randint(33, 125)) for i in [0] * 16])


def find_collisions(collisions):
    final_version = {}

    for k, v in collisions.items():
        if len(v) > 1:
            final_version[k] = v
    
    return final_version


def create_collisions(num_iters):
    results = {}

    for i in range(num_iters):
        string = generate_random_string()
        hashed = check_sum(string)

        if not results.get(hashed):
            results[hashed] = []
        
        results[hashed].append(string)
    
    return find_collisions(results)
