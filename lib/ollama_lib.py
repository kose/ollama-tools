# -*- coding: utf-8 -*-

# https://github.com/ollama/ollama/blob/main/docs/api.md

import os
import requests
import subprocess
import json

# ollama のモデルリストをjson形式で取得、モデル名リストとjsonを返す
def get_ollama_models(host):
    try:
        response = requests.get(f"http://{host}:11434/api/tags")
        response.raise_for_status()  # ステータスコードが異常な場合、例外を発生させる

        json_data = response.json()

        # モデルのリスト
        models = []
        for record in json_data['models']:
            models.append(record['model'])

        return models, json_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)


# ollama のモデルをpullする
def pull_ollama_model(host, model):

    # モデルが存在するかチェック
    models, _ = get_ollama_models(host) # モデルリストを取得
    if model in models:
        comment = f"exist: {model}"
        print(comment)
        return comment

    print(f"pulling ... {model}")

    # ローカルホストの場合は、コマンドを実行
    if host == "localhost":
        command = f"ollama pull {model}"
        print(f"command: {command}")
        subprocess.run([command], shell=True)
        return "success"

    # リモートホストの場合は、APIを実行
    try:
        response = requests.post(f"http://{host}:11434/api/pull", json={"model": model})
        response.raise_for_status()  # ステータスコードが異常な場合、例外を発生させる

        # responseは\nで区切られる。最後の部分を取り出す。
        status = response.text.split("\n")[-2]

        # statusはjson形式の文字列
        status = json.loads(status)

        # statusというキーがある場合は、成功
        if "status" in status:
            status = "success"
        else:
            status = f"Model not found: {model}"

        return status

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)


# ollama のモデルをdeleteする
def delete_ollama_model(host, model):

    print(f"delete ... {model}")

    # モデルが存在するかチェック
    models, _ = get_ollama_models(host) # モデルリストを取得
    if model not in models:
        return f"Model not found: {model}"
    
    try:
        response = requests.delete(f"http://{host}:11434/api/delete", json={"model": model})
        response.raise_for_status()  # ステータスコードが異常な場合、例外を発生させる

        # responseは\nで区切られる。最後の部分を取り出す。
        if response.ok:
            status = "success"
        else:
            status = "failed"

        return status

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    host = os.getenv('OLLAMA_RHOST', 'localhost')
    model_name = "llama3.2:3b"

    status = pull_ollama_model(host, model_name)
    print(f"status: {status}")

    status = delete_ollama_model(host, model_name)
    print(f"status: {status}")


    # import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###
