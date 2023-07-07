from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from IPython.display import Markdown, display
import os 
import openai 


# Request OpenAI Key
os.environ["OPENAI_API_KEY"] = input("Enter your OpenAI key: ")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Data from the 'data' folder 
# local file directory (SimpleDirectoryReader) supports parsing a wide range of file types: .pdf, .jpg, .png, .docx, etc.
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

# stores for re-use
index.storage_context.persist(persist_dir="training_storage")
