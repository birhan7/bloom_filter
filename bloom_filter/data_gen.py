import random
import string

def generate_data(n):
    return [
        ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        for _ in range(n)
    ]
