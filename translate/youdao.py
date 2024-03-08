from Crypto.Cipher import AES
from Crypto.Hash import MD5
import base64
from requests import session
import time
import random
import json


class YoudaoTranslater:
    def __init__(self) -> None:
        self.sess = session()
        self.sess.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
            "origin": "https://fanyi.youdao.com",
            "referer": "https://fanyi.youdao.com/",
        }
        params = {
            "_npid": "fanyiweb",
            "_ncat": "pageview",
            "_ncoo": str(2147483647 * random.uniform(0, 1)),
            "_nssn": "NULL",
            "_nver": "1.2.0",
            "_ntms": self.__sticTime(),
        }
        self.sess.get("https://rlogs.youdao.com/rlog.php", params=params)
        params = {
            "keyid": "webfanyi-key-getter",
        } | self.__base_body("asdjnjfenknafdfsdfsd")
        res = self.sess.get(
            "https://dict.youdao.com/webtranslate/key", params=params)
        t = res.json()
        self.key = t["data"]["secretKey"]

    def get_lan_list(self) -> dict:
        res = self.sess.get(
            "https://api-overmind.youdao.com/openapi/get/luna/dict/luna-front/prod/langType"
        )
        return res.json()["data"]["value"]["textTranslate"]

    @staticmethod
    def __sticTime() -> str:
        return str(int(time.time() * 1000))

    @staticmethod
    def __sign(t: str, key: str) -> str:
        return (
            MD5.new(
                f"client=fanyideskweb&mysticTime={t}&product=webfanyi&key={key}".encode(
                )
            )
            .digest()
            .hex()
        )

    def __base_body(self, key: str) -> dict:
        t = self.__sticTime()
        return {
            "sign": self.__sign(t, key),
            "client": "fanyideskweb",
            "product": "webfanyi",
            "appVersion": "1.0.0",
            "vendor": "web",
            "pointParam": "client,mysticTime,product",
            "mysticTime": t,
            "keyfrom": "fanyi.web",
        }

    @staticmethod
    def __decode(src: str) -> dict:
        # see: https://blog.csdn.net/nick131410/article/details/128877625
        key = b"ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
        iv = b"ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
        cryptor = AES.new(
            MD5.new(key).digest()[:16], AES.MODE_CBC, MD5.new(iv).digest()[:16]
        )
        res = cryptor.decrypt(base64.urlsafe_b64decode(src))
        txt = res.decode("utf-8")
        return json.loads(txt[: txt.rindex("}") + 1])

    def translate(self, src: str, fromLan: str = "auto", toLan: str = "auto"):
        data = {
            "i": src,
            "from": fromLan,
            "to": toLan,
            "dictResult": True,
            "keyid": "webfanyi",
        } | self.__base_body(self.key)
        res = self.sess.post("https://dict.youdao.com/webtranslate", data=data)
        return self.__decode(res.text)


def main():
    translater = YoudaoTranslater()
    times = 0
    while True:
        print(translater.translate(input(">")))
        times += 1
    print(f"times: {times}")


def translate(input):
    translater = YoudaoTranslater()
    # return translater.translate(input)
    return translater.translate(input)['translateResult'][0][0]['tgt']


if __name__ == "__main__":
    # print(translate("I love prism"))
    main()


def getName():
    return "有道翻译"
