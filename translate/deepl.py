import time
import random
import requests


def translate(input):
    input = '"' + input + '"'
    u_input = input.encode("unicode_escape").decode()
    data = '{"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","raw_en_sentence":' + input + ',"raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4,"quality":"fast"}],"lang":{"user_preferred_langs":["ZH","EN"],"source_lang_user_selected":"auto","target_lang":"ZH"},"priority":-1,"commonJobParams":{},"timestamp":' + str(
        int(time.time() * 10000)) + '},"id":' + str(
            random.randint(1, 100000000)) + '}'
    r = requests.post('https://www2.deepl.com/jsonrpc',
                      headers={
                          'accept': '*/*',
                          'accept-language': 'zh-TW,zh;q=0.9,ja;q=0.8,zh-CN;q=0.7,en-US;q=0.6,en;q=0.5',
                          'cache-control': 'no-cache',
                          'content-type': 'application/json',
                          'pragma': 'no-cache',
                          'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                          'sec-ch-ua-mobile': '?0',
                          'sec-ch-ua-platform': '"Windows"',
                          'sec-fetch-dest': 'empty',
                          'sec-fetch-mode': 'cors',
                          'sec-fetch-site': 'cross-site',
                          'Referer': 'https://deepl.com/',
                          'Referrer-Policy': 'strict-origin-when-cross-origin',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
                      },
                      data=data.encode())
    try:
        return r.json()['result']['translations'][0]['beams'][0]['postprocessed_sentence']
    except:
        return "too many requests"

# print(translate("I love prism"))


def getName():
    return "deepl"
