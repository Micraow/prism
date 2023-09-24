import requests
import re
url = 'https://cn.bing.com/dict/search?mkt=en-us&q='


def explain(input):
    res = requests.get(url+input).text
    r = re.compile(r"<meta name=\"description\" content=\"必应词典为您提供(.*?)\" \/>")
    res = re.findall(r, res)
    return res[0]


if __name__ == "__main__":
    print(explain("prism"))
