# mini-rag project

This is a minimal implementation of RAG model for question answering.

## Requirements

- Python 3.8

###### Install Python using Miniconda

1. Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html)
2. Create a new environment using the following command:
   ```bash
   conda create -n mini-rag python=3.8
3- activate conda
## Islallation 
### install the required packages
```bash 
$pip install -r requirements.txt 
```
### Setup the environment variables 
```bash
$ cp .env.example .env
```
set your enivironment variables in the `.env` file. like `OPEN_APPI_KEY` value.

##run the FASTAPI server 
```bash 
$uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
### to open swagger ui use 
http://localhost:5000/docs as url
