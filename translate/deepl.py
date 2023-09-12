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
                        headers={'content-type': 'application/json'},
                        data=data.encode())
    return r.json()['result']['translations'][0]['beams'][0]['postprocessed_sentence']

# print(translate("hello andy"))
