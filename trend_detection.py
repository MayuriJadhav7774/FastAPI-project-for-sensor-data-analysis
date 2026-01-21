import pandas as pd
import numpy as np

def detect_trends(df: pd.DataFrame):
    results = []

    sensor_columns = ["temperature", "humidity", "co2", "voc"]

    for col in sensor_columns:
        if col not in df.columns:
            continue

        values = df[col]

        # Simple trend logic
        trend = "stable"
        if values.iloc[-1] > values.iloc[0]:
            trend = "increasing"
        elif values.iloc[-1] < values.iloc[0]:
            trend = "decreasing"

        # Anomaly detection (Z-score)
        mean = values.mean()
        std = values.std()

        if std == 0:
            anomaly_count = 0
        else:
            z_scores = (values - mean) / std
            anomaly_count = int((np.abs(z_scores) > 2).sum())

        # Pre-alert condition
        pre_alert = True if trend == "increasing" and anomaly_count > 0 else False

        results.append({
            "parameter": col,
            "trend": trend,
            "anomaly_count": anomaly_count,
            "pre_alert": pre_alert
        })

    return results
