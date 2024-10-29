# This function simulates the performance of the various  models
import random
import models.DAO.DAO as db_utils
from utils.logger import Logger

logger = Logger()

component_name = "LLM simulator"
# The randomizer is a function that is built to generate data. As the randomizer generates data, it uses the insert metrics DAO to insert the metrics into the correct database collection.


def randomizer():
    return {
        "ttft": random.uniform(0.5, 2.5),
        "tps": random.uniform(100, 500),
        "e2e_latency": random.uniform(1, 3),
        "rps": random.uniform(10, 100),
    }


def metrics_simulator(collection_name, model_name, metric_limit=1000):
    llm_data = []
    for _ in range(metric_limit):
        llm_data.append({"model_name": model_name, **randomizer()})
    save_metrics(collection_name, llm_data)


def save_metrics(collection_name, data):
    db_utils.insert_metrics(collection_name, data)


# This function runs the simulator, to generate data for the various LLMs - here we use
def run_simulator():
    logger.log(component_name, "Running simulation benchmarks for LLM Models...")
    try:
        if db_utils.gpt4o_collection.count_documents({}) > 0:
            logger.log(component_name, "Database already seeded. Skipping simulation.")
            return False
        else:
            metrics_simulator(db_utils.gpt4o_collection, "GPT-4o")
            metrics_simulator(db_utils.llama31_405_collection, "Llama 3.1 405")
            metrics_simulator(db_utils.gemini15_pro_collection, "Gemini 1.5 Pro")
        return True
    except Exception as e:
        print(
            f"There was an error running the metric simulatror. check the db connection: {e}"
        )
        return False
