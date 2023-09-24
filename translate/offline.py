import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


def downlad(path):
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

    url = "https://alist.pengs.top/d/64816595359b1e5db47f442f901a98ce4efd8481/alist/models/Helsinki-NLP/opus-mt-en-zh/pytorch_model.bin"
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

    return downlad()


current_work_dir = os.path.dirname(__file__)
if os.path.exists(current_work_dir+"/hf_model/pytorch_model.bin") == False:
    # print(os.path.exists(current_work_dir+"/hf_model/pytorch_model.bin"))

    # print(current_work_dir)
    print("downloading offline translate model...")
    downlad(current_work_dir+"/hf_model/pytorch_model.bin")
