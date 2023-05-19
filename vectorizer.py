#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
vectorizer.py: This file is used to vectorize the data files and store it in Pinecone.
Created on Mon Aug  2 15:04:00 2021
"""

import os
import pinecone
import nltk
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import DirectoryLoader

print("Updating punkt")
nltk.download('punkt')

print("Loading environment variables")
OPEN_API_KEY = os.environ["OPENAI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_API_ENV = os.environ["PINECONE_API_ENV"]

# Set your pinecone index name
PINECONE_API_INDEX = "elevator"

print("Reading in the data files from the library_data folder")
loader = DirectoryLoader("library_data", show_progress=True)
documents = loader.load()

print (f'You have {len(documents)} vector(s) in your data')
print (f'There are {len(documents[0].page_content)} characters in your document(s)')

print("Splitting the text into chunks")
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

print("Initializing the OpenAI Embeddings")
embeddings = OpenAIEmbeddings(openai_api_key=OPEN_API_KEY)

print("Initializing the Pinecone API")
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENV
)
print("Creating the Pinecone Index")
docsearch = Pinecone.from_texts(
    [t.page_content for t in texts], embeddings, index_name=PINECONE_API_INDEX)
