#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from lib.ollama_lib import get_ollama_models, delete_ollama_model

# ollama のモデル一覧を表示するスクリプト
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='ollama model list')
    parser.add_argument('--host', type=str, default="localhost", help='Ollama host name')
    parser.add_argument('--model', type=str, default="", help='model name')
    parser.add_argument('--one', action='store_true', help='モデルをひとつ消す')
    parser.add_argument('--all', action='store_true', help='モデルを全て消す')
    args = parser.parse_args()

    host = args.host
    model = args.model

    if args.one:
        models, _ = get_ollama_models(host) # モデルリストを取得
        delete_ollama_model(host, models[-1])
        exit (0)

    if args.all:
        models, _ = get_ollama_models(host) # モデルリストを取得
        for model in models:
            delete_ollama_model(host, model)
        exit (0)

    if model == "":
        print("Usage: python ollama-pull.py --host <host> --model <model>")
        exit(1)

    # モデルが存在するかチェック
    models, _ = get_ollama_models(host) # モデルリストを取得
    if model not in models:
        print(f"Model not found: {model}")
        exit(1)

    # pull model
    status = delete_ollama_model(host, model)

    print(status)


# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###
