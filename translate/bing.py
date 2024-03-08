import requests
import json
token_url = 'https://edge.microsoft.com/translate/auth'
token_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
}
token = requests.get(token_url, headers=token_headers)


def translate(inputs):
    """调用edge的网页翻译API用作我们的翻译后端

    Args:
        input (str): 要翻译的英文

    Returns:
        str: 翻译结果（中文）
    """
    url = 'https://api-edge.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=zh-Hans'
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-TW,zh;q=0.9,ja;q=0.8,zh-CN;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer ' + token.text,
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'Referer': 'https://github.com/',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
    }
    body = [{
        'Text': input}]
    res = requests.post(url, data=json.dumps(body), headers=headers)
    res = json.loads(res.text)
    res = res[0]["translations"][0]["text"]
    return res


def getName():
    return "bing"
