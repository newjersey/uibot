# AI Q&A Bot

Q&A bot using [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/). This is a simple implementation using OpenAI's models, but the documentation contains extensive customization options (including changing the LLM). 

## Initial Setup
Install required packages by running: 
```
pip install llama-index
```

## Ongoing Operations

### Loading Data and Creating index
Load the knowledge base files (such as pdf, jpg, png, docx, txt, csv) into the 'data' folder. Llama-index has support for [third-party connectors](https://gpt-index.readthedocs.io/en/latest/how_to/connector/root.html) as well.   

Run the following whenever changes are made to the data folder to re-generate the knowledge base: 
```
python createindex.py
```

### Ask questions 
To start a Q&A dialogue run the following:
```
python ask.py
```
