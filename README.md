# datatopinecone

datatopinecone was written using python 3.11.3

datatopinecone.py will parse any files you place in a ```library_data``` folder, and store them in a 1536 dimension Pinecone vector index.

## Installation

### Set up environment variables

* ```OPENAI_API_KEY```
* ```PINECONE_API_KEY```
* ```PINECONE_API_ENV```

### Set the Pinecone index name variable

* ```PINECONE_API_INDEX``` in datatopinecone.py

### Install requirements

* ```pip -r requirements.txt```

### Populate library_data folder

* Create a ```library_data``` folder.
* Fill the ```library_data``` folder with the documents you want to populate the Pinecone index. A wide variety of documents can be used, ```.txt, .pdf, .doc, .csv, ...more```.

### Run vextorizer.py

* This will take a while, depending on the amount of files and their sizes. There is a progress bar in the terminal. Be patient.
