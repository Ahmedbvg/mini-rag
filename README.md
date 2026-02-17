# mini-rag project

This is a minimal implementation of RAG model for question answering.

## Requirements

- Python 3.8

###### Install Python using Miniconda

1. Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html)
2. Create a new environment using the following command:
   ```bash
   conda create -n mini-rag python=3.8
3- activate conda using"conda activate mini-rag-app"

## Islallation 
### install the required packages
```bash 
pip install -r requirements.txt 
```
### Setup the environment variables 
```bash
$ cp .env.example .env
```
set your enivironment variables in the `.env` file. like `OPEN_APPI_KEY` value.

##run the FASTAPI server 
```bash 
.\venv\Scripts\python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```
### to open swagger ui use 
http://localhost:5000/docs as url



##### to compuse up doker 
docker-compose -f docker/docker-compose.yml up -d
 ##### to compose down 
 docker-compose -f docker/docker-compose.yml down
 ##### to view logs 
 docker-compose -f docker/docker-compose.yml logs -f api
 #### to rebuild after code changes
 docker-compose -f docker/docker-compose.yml up -d --build

 #### update `.env` file with you credentials 