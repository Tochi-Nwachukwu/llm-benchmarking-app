from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Define Pydantic model for each LLM simulation result
class LLMMetrics(BaseModel):
    model_name: str = Field(..., example="GPT-4o")
    ttft: float = Field(..., example=1.32)  # Time to First Token
    tps: float = Field(..., example=300.5)  # Tokens Per Second
    e2e_latency: float = Field(..., example=2.1)  # End-to-End Request Latency
    rps: float = Field(..., example=75.0)  # Requests Per Second
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