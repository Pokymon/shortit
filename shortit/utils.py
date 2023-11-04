import random
import string

def generate_short_id():
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    short_id = ''.join(random.choice(characters) for _ in range(4))
    return short_id
