from llama_index import VectorStoreIndex, SimpleDirectoryReader, SimpleWebPageReader, StorageContext, load_index_from_storage
from IPython.display import Markdown, display
import os 
import openai 


# Request OpenAI Key
os.environ["OPENAI_API_KEY"] = input("Enter your OpenAI key: ")
openai.api_key = os.getenv("OPENAI_API_KEY")

URLS = [
    "https://nj.gov/labor/myunemployment/assets/pdfs/PR-94.pdf",
    "https://nj.gov/labor/myunemployment/help/",
    "https://nj.gov/labor/myunemployment/help/PR94/",
    "https://nj.gov/labor/myunemployment/help/faqs/",
    "https://nj.gov/labor/myunemployment/help/glossary/",
    "https://nj.gov/labor/myunemployment/help/forms/",
    "https://nj.gov/labor/myunemployment/help/debitcard/",
    "https://nj.gov/labor/myunemployment/help/resources-support/",
    "https://nj.gov/labor/myunemployment/help/contact-us/",
    "https://nj.gov/labor/myunemployment/help/contact-us/reportfraud/",
    "https://nj.gov/labor/myunemployment/help/faqs/eligibility.shtml",
    "https://nj.gov/labor/myunemployment/help/faqs/appeals.shtml",
    "https://nj.gov/labor/myunemployment/help/faqs/reducebenefits.shtml",
    "https://nj.gov/labor/myunemployment/help/faqs/taxes.shtml",
    "https://nj.gov/labor/myunemployment/help/faqs/general.shtml",
    "https://nj.gov/labor/myunemployment/help/faqs/techhelp.shtml",
    "https://nj.gov/labor/myunemployment/help/debitcard/debitcardfees.shtml"
]


# Load Data from the 'data' folder 
# local file directory (SimpleDirectoryReader) supports parsing a wide range of file types: .pdf, .jpg, .png, .docx, etc.
#documents = SimpleDirectoryReader('data').load_data()

documents = SimpleWebPageReader().load_data(urls=URLS)
index = VectorStoreIndex.from_documents(documents)

# stores for re-use
index.storage_context.persist(persist_dir="training_storage")
