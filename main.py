from fastapi import FastAPI
import config.connect as db_init
from routes.routes import router
from utils.logger import Logger

component_name = "main"
logger = Logger()

app = FastAPI()

app.include_router(router)

# Initialize the MongoDB connection
if db_init.connect():
    logger.log(component_name, "Successfully connected to MongoDB")
else:
    logger.err(component_name, "Failed to connect to MongoDB")
