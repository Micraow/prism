# 翻译层

## bing 翻译

使用方法：

translate(str:英文)

返回： 中文结果


调用edge的网页翻译API用作我们的翻译后端

1. 从 https://edge.microsoft.com/translate/auth 获取token
2. 请求 https://api-edge.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=zh-Hans post方法

header参考（伪装成edge)

```
headers = {
        'accept': '*/*',
        'accept-language': 'zh-TW,zh;q=0.9,ja;q=0.8,zh-CN;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer ' + TOKEN(即第1步中的),
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
```

响应参考：

```
[{"translations":[{"text":"你好","to":"zh-Hans"}]}]
```

## deepl, 有道翻译,本地翻译
同bing翻译

使用方法：

translate(str:英文)

返回： 中文结果

**deepl在多次查询后会返回“too many requests”**

## 必应词典

**仅供查词，查句子会报错**

用法:

explain(str:单词)

返回： 释义，带音标