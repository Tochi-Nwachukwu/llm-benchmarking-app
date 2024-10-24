import models.DAO.DAO as db_collections
models = {
    "GPT-4o": db_collections.gpt4o_collection,
    "Llama 3.1 405": db_collections.llama31_405_collection,
    "Gemini 1.5 Pro": db_collections.gemini15_pro_collection
}


metrics = ["ttft", "tps", "e2e_latency", "rps"]
