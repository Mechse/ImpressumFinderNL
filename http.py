import requests


def getContent(url):
    try:
        page = requests.get('http://' + url)
    except:
        return

    content = page.content
    return content
