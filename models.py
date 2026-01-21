from pydantic import BaseModel

class TrendResult(BaseModel):
    parameter: str
    trend: str
    anomaly_count: int
    pre_alert: bool
