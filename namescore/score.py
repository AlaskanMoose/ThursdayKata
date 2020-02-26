import requests

URL = "https://projecteuler.net/project/resources/p022_names.txt"

response = requests.get(URL)

data = response.text

score = sum([sum([ord(char) - 64 for char in [tup for tup in (word_index, word)][1].strip('"')]) * word_index for (word_index, word) in enumerate(data.split(","))])
