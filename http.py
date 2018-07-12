import requests


def getContent(url):
    try:
        page = requests.get('http://' + url)
    except:
        return "Site can't be reached."

    content = page.content
    return content
