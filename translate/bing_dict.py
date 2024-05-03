import requests
import re
url = 'https://cn.bing.com/dict/search?mkt=en-us&q='


def explain(inputs):
    res = requests.get(url+inputs).text
    r = re.compile(r"<meta name=\"description\" content=\"必应词典为您提供(.*?)\" \/>")
    res = re.findall(r, res)
    return res[0]


def getName():
    return "bing词典"


if __name__ == "__main__":
    print(explain("prism"))
