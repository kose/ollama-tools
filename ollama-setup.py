#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import argparse

from lib.ollama_lib import pull_ollama_model

def main(host):
    
    json_file = "recipe.json"

    # レシピjsonファイルの読み込み
    try:
        with open(json_file, 'r') as f:
            recipe_json = json.load(f)
    except Exception as e:
        print(f"Error: {json_file}: {e}")
        exit()
    except:
        print(f"{json_file} file not found.")
        exit()

    # "active": "Yes" のモデルのみ処理
    recipe_json = [item for item in recipe_json if item['active'].lower() == 'yes']

    for record in recipe_json:
        # print(record['model'])
        pull_ollama_model(host, record['model'])

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='ollama model setup')
    parser.add_argument('--host', type=str, default="localhost", help='ollama host name')
    args = parser.parse_args()

    host = args.host

    main(host)
    

# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###
