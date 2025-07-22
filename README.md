# Ollama サポートツール

- recipe.json にしたがってインストールする。
- リモートPCの Ollama に対応。
- Ollama は Hugging Face に置いてあるモデルも対応してたの知ってた？

## simple chat

```python
import os
from langchain_ollama import ChatOllama

model_name = "gemma3:4b"
ollama_url = os.getenv('OLLAMA_RHOST', 'localhost')

llm = ChatOllama(
    model = model_name,
    temperature = 0.5,
    base_url = ollama_url
) 

response = llm.invoke("こんにちは")

print(response.content)

```

## My local Remote Ollama server

export OLLAMA_RHOST=172.18.17.71
 
 
## Reference

- [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md)
