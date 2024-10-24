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
            detail=f"Invalid metric. Valid metrics are: {
                ', '.join(valid_metrics)}"
        )

    #  This calls a utility function that will Rank the models by the specified metric
    ranked_models = db_utils.rank_models_by_metric(metric)
    return {"metric": metric, "ranking": ranked_models}


@app.get("/get-metrics/{llm}")
async def get_metric(llm: str):
    # Check if the LLM is valid
    #  improvements --> I can have a hash map that maps user inputs to possible llms and be more forgiving in the user typographical errors using regex
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


@app.get("/run-simulator")
async def run_simulator():
    res = metrics_simulator.run_simulator()
    if res == True:
        return "Simulator Started and gracefully exited"
    else:
        raise HTTPException(
            status_code=500,
            detail=f"There was an error running the benchmarks simulator. Check Application logs for details"
        )


# Initialize the MongoDB connection
if db_init.connect():
    print("Successfully connected to MongoDB")
else:
    print("Failed to connect to MongoDB")
