from random import *

import requests

import re

url_start = "https://ru.wikipedia.org/w/index.php?title=Служебная:Все_страницы&from="

def get_random_prefix_args():
    random_character_first = randint(1040, 1071)
    while random_character_first == 1068 or random_character_first == 1066:
        random_character_first = randint(1040, 1071)
    random_character_second = randint(1072, 1103)
    return chr(random_character_first) + chr(random_character_second)

def random_state_by_prefix(requests_text):
    all_ref = re.search(r'<a href="(\/wiki\/.+)" title=".+">.+<\/a><\/li>', requests_text, re.M|re.I)
    print(all_ref.groups())
    return all_ref.group(1)
    #print(requests_text)
    #print(all_ref.groups())


def get_random_state():
    url_start = "https://ru.wikipedia.org/w/index.php?title=Служебная:Все_страницы&from=" + get_random_prefix_args()
    response = requests.get(url_start)
    #print(random_state_by_prefix('<li><a href="/wiki/%D0%91%D1%8F%D0%BB%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9,_%D0%91%D0%B0%D1%80%D1%82%D0%BE%D1%88" title="Бялковский, Бартош">Бялковский, Бартош</a></li>'))
    #print(random_state_by_prefix(response.text))


    state_ref = random_state_by_prefix(response.text)
    while 'class' in state_ref:
        state_ref = random_state_by_prefix(response.text)
    req = requests.get("https://ru.wikipedia.org" + random_state_by_prefix(response.text))
    return req.url


print(get_random_state())