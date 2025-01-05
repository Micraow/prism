import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer


def download(path):
    def calc_divisional_range(filesize, chuck=8):
        step = filesize//chuck
        arr = list(range(0, filesize, step))
        result = []
        for i in range(len(arr)-1):
            s_pos, e_pos = arr[i], arr[i+1]-1
            result.append([s_pos, e_pos])
        result[-1][-1] = filesize-1
        return result


# 下载方法

    def range_download(save_name, s_pos, e_pos):
        headers = {"Range": f"bytes={s_pos}-{e_pos}"}
        res = requests.get(url, headers=headers, stream=True)
        with open(save_name, "rb+") as f:
            f.seek(s_pos)
            for chunk in res.iter_content(chunk_size=64*1024):
                if chunk:
                    f.write(chunk)

    url = "https://hf-mirror.com/Helsinki-NLP/opus-mt-en-zh/resolve/main/pytorch_model.bin?download=true"
    res = requests.get(url)
    filesize = int(res.headers['Content-Length'])
    divisional_ranges = calc_divisional_range(filesize)

    save_name = path
# 先创建空文件
    with open(save_name, "wb") as f:
        pass
    with ThreadPoolExecutor() as p:
        futures = []
        for s_pos, e_pos in divisional_ranges:
            print(s_pos, e_pos)
            futures.append(p.submit(range_download, save_name, s_pos, e_pos))
    # 等待所有任务执行完毕
        as_completed(futures)

    return download(path)


def translate(inputs):
    current_work_dir = os.path.dirname(__file__)
    if os.path.exists(current_work_dir+"/hf_model/pytorch_model.bin") is False:
        # print(os.path.exists(current_work_dir+"/hf_model/pytorch_model.bin"))

        # print(current_work_dir)
        print("downloading offline translate model...")
        download(current_work_dir+"/hf_model/pytorch_model.bin")
    model = AutoModelForSeq2SeqLM.from_pretrained(current_work_dir+"/hf_model")
    local_files_only = True
    tokenizer = AutoTokenizer.from_pretrained(current_work_dir+"/hf_model")
    translation = pipeline("translation_en_to_zh",
                           model=model, tokenizer=tokenizer)

    text = input
    model = AutoModelForSeq2SeqLM.from_pretrained(current_work_dir+"/hf_model", local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(current_work_dir+"/hf_model", local_files_only=True)
    translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)
    text = inputs
    translated_text = translation(text, max_length=40)[0]['translation_text']
    return translated_text

def getName():
    return "离线翻译"

if __name__ == "__main__":
    print(translate("I love prism, which is a personal English assistant."))