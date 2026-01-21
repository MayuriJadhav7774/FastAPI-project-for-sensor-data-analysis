from fastapi import FastAPI, UploadFile, File
import pandas as pd
from app.trend_detection import detect_trends

app = FastAPI(
    title="Sensor Data Trend Detection API",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "API running successfully"}

@app.post("/detect-trend")
async def detect_trend(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    result = detect_trends(df)
    return result
