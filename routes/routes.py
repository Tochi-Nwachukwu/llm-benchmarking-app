from fastapi import APIRouter, HTTPException
import models.DAO.DAO as db_utils
import config.constants as constants
import services.metrics_simulator as metrics_simulator
from fastapi.responses import HTMLResponse
from views.index import html_content
from models.Schema import ResponseModel, ErrorResponseModel

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=html_content)

@router.get("/rank/{metric}", response_description="retrieving llm rankings based on average performance")
async def rank_models(metric: str):
    # Check if the metric is valid
    valid_metrics = constants.metrics
    if metric not in valid_metrics:
        return ErrorResponseModel(
            "invalid metric type", 400, f"Invalid metric. Valid metrics are: {', '.join(valid_metrics)}"
        )
    # This calls a utility function that will rank the models by the specified metric
    ranked_models = db_utils.rank_models_by_metric(metric)
    return ResponseModel({"metric": metric, "ranking": ranked_models}, f"LLM rankings for {metric} retrieved ")

@router.get("/get-metrics/{llm}", response_description="Retrieving simulation metrics from the database")
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
    return ResponseModel(res, f"Metrics for {llm} added successfully.")

@router.get("/run-simulator")
async def run_simulator():
    res = metrics_simulator.run_simulator()
    if res:
        return "Simulator Started and gracefully exited"
    else:
        raise HTTPException(
            status_code=500,
            detail="There was an error running the benchmarks simulator. Check Application logs for details"
        )