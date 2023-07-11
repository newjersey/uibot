from llama_index import VectorStoreIndex, SimpleDirectoryReader, SimpleWebPageReader, StorageContext, ServiceContext, load_index_from_storage
from llama_index.llms import OpenAI

import os
import openai


# Request OpenAI Key
openai.api_key = os.environ["OPENAI_API_KEY"]

llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
service_context = ServiceContext.from_defaults(llm=llm)

# Load Data from URLS and  the 'data' folder
# local file directory (SimpleDirectoryReader) supports parsing a wide range of file types: .pdf, .jpg, .png, .docx, etc.
documents = SimpleDirectoryReader('data').load_data()

index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# stores for re-use
index.storage_context.persist(persist_dir="training_storage")
