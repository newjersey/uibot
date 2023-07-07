from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from IPython.display import Markdown, display
import os
import openai 

# Request OpenAI Key
os.environ["OPENAI_API_KEY"] = input("OpenAI key:")
openai.api_key = os.getenv("OPENAI_API_KEY")


# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="training_storage")
# load index
index = load_index_from_storage(storage_context)


# loop q&a 
query_engine = index.as_query_engine()
while True:
    print("")
    question = input("Enter question: ")
    response = query_engine.query(question)
    print(response)
