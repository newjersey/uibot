from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

import os
import openai

# Request OpenAI Key
os.environ["OPENAI_API_KEY"] = input("OpenAI key:")
openai.api_key = os.getenv("OPENAI_API_KEY")


# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="training_storage")
# load index
index = load_index_from_storage(storage_context)

chat_engine = index.as_chat_engine(verbose=True)
chat_engine.chat_repl()
