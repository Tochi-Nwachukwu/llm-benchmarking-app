from fastapi import FastAPI
import config.connect as db_init
from routes.routes import router
from utils.logger import Logger
from services.metrics_simulator import run_simulator

component_name = "main"
logger = Logger()

app = FastAPI()

app.include_router(router)

# Initialize the MongoDB connection
if db_init.connect():
    logger.log(component_name, "Successfully connected to MongoDB")
    #  if connection is successful, seed the database with the correct data.
    data_migration = run_simulator()
    if data_migration == True:
        logger.log(
            component_name + "-data-migration",
            "Successfully Seeded the database with fresh simulation records",
        )
    else:
        logger.log(
            component_name + "-data-migration-job",
            "The database has already been seeded",
        )
else:
    logger.err(component_name, "Failed to connect to MongoDB")
