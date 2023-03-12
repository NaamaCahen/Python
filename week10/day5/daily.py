import requests, time


def time_loading_webpage(url):
    before=time.time()
    x = requests.get(url)
    after=time.time()
    return after - before

print(time_loading_webpage('https://www.google.com/'))
print(time_loading_webpage('https://www.linkedin.com/'))
print(time_loading_webpage('https://www.easyjet.com/'))

