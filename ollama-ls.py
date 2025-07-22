#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from lib.ollama_lib import get_ollama_models

# ollama のモデル一覧を表示するスクリプト
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='ollama model list')
    parser.add_argument('--host', type=str, default="localhost", help='Ollama host name')
    args = parser.parse_args()

    host = args.host

    models, _ = get_ollama_models(host)

    # ソートして表示
    models.sort()
    for model in models:
        print(model)

# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###
