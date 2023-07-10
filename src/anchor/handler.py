import os
import json
import openai

from llama_index import StorageContext, ServiceContext, load_index_from_storage
from llama_index.llms import OpenAI

from datetime import date

# Set OpenAI Key
openai.api_key = os.environ["OPENAI_API_KEY"]

llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
service_context = ServiceContext.from_defaults(llm=llm)

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="training_storage")
# load index
index = load_index_from_storage(storage_context)


now = date.today()
INSTRUCTIONS = f"""
    CONTEXT:
    Today's date is {now}.
    Answer only if the question is relevant to the NJ ANCHOR program.
    Answer in simple language.
    Call "context information" "New Jersey ANCHOR program".

    QUESTION:

    """

query_engine = index.as_query_engine(service_context=service_context)

def ask(event, context):
    question = event["queryStringParameters"]['question']
    PROMPT = INSTRUCTIONS + question
    response = query_engine.query(PROMPT)
    print(response);
    return {
      "answer": response.response
    }
