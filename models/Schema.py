from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

        
# This MongoDB schema can be scaled to accommodate more metrics as needed for each model, following hte same template.

class LLMMetrics(BaseModel):
    model_name: str = Field(..., example="GPT-4o")
    ttft: float = Field(..., example=1.32)  
    tps: float = Field(..., example=300.5)  
    e2e_latency: float = Field(..., example=2.1) 
    rps: float = Field(..., example=75.0) 
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        schema_extra = {
            "example": {
                "model_name": "GPT-4o",
                "ttft": 1.32,
                "tps": 300.5,
                "e2e_latency": 2.1,
                "rps": 75.0,
                "timestamp": "2024-10-19T14:25:32.635Z"
            }
        }
        

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}