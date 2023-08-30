#/usr/bin/python3
import hashlib
from itertools import product
import string
import re

salt = "f789bbc328a3d1a3"

def get_pass():
    i = 1
    while i <=10:
        for combo in product(string.ascii_letters + string.digits, repeat=i):
            word = ''.join(combo)
            crafted = hashlib.md5((salt + word).encode("utf-8")).hexdigest()
            if(re.search("^(0e)[0-9]*$",crafted)):
                return word
        i = i+1
    return None

print(get_pass())