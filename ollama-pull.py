#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from lib.ollama_lib import pull_ollama_model

# ollama のモデル一覧を表示するスクリプト
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='ollama model list')
    parser.add_argument('--host', type=str, default="localhost", help='Ollama host name')
    parser.add_argument('--model', type=str, default="", help='model name')
    args = parser.parse_args()

    host = args.host
    model = args.model

    if model == "":
        print("Usage: python ollama-pull.py --host <host> --model <model>")
        exit(1)

    # pull model
    status = pull_ollama_model(host, model)

    print(status)


# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###
