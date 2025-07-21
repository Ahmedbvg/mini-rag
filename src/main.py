from fastapi import FastAPI
import os
load_dotenv(".env")  # Load environment variables from .env file
from src import base 


app = FastAPI()
app.include_router(base.base_router)

