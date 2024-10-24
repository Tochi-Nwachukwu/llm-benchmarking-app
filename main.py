import config.connect as db_init
from fastapi import FastAPI, HTTPException
import models.DAO.DAO as db_utils
import config.constants as constants
import services.metrics_simulator as metrics_simulator

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/rank/{metric}")
async def rank_models(metric: str):
    # Check if the metric is valid
    valid_metrics = constants.metrics
    if metric not in valid_metrics:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid metric. Valid metrics are: {', '.join(valid_metrics)}"
        )

    # Rank the models by the specified metric
    ranked_models = await db_utils.rank_models_by_metric(metric)
    return {"metric": metric, "ranking": ranked_models}


@app.get("/get-metrics/{llm}")
async def get_metric(llm: str):
    # Check if the LLM is valid
    valid_llms = constants.models.keys()
    if llm not in valid_llms:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid LLM. Valid LLMs are: {', '.join(valid_llms)}"
        )

    # Retrieve metrics for the specified LLM
    llm_model = constants.models.get(llm)
    res = await db_utils.retrieve_metrics(llm_model, llm)
    return res


# Initialize the MongoDB connection
if db_init.connect():
    print("Successfully connected to MongoDB")
    # Uncomment to run the simulator if needed
    # metrics_simulator.run_simulator()
else:
    print("Failed to connect to MongoDB")
