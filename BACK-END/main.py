from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd # Needed to read Siri's CSV [cite: 11]
import os

app = FastAPI()

# B1. Backend Setup [cite: 103]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# B3. Path to the expected ML output [cite: 113]
DATA_PATH = "ml_outputs/clean_chicago_crime.csv"

@app.get("/hotspots")
def get_hotspots():
    """
    B3. ML Integration: Load real ML outputs if available[cite: 113, 114].
    Serve results via API[cite: 114].
    """
    if os.path.exists(DATA_PATH):
        # Load the real dataset cleaned by Person A [cite: 63, 113]
        df = pd.read_csv(DATA_PATH)
        # Limit data to keep it fast (as recommended in Task A5) [cite: 54, 57]
        return df.head(100).to_dict(orient="records")
    
    # Fallback to dummy data until Siri finishes cleaning [cite: 173, 175]
    return [
        {"crime_type": "THEFT", "latitude": 41.88, "longitude": -87.63, "risk": "High"},
        {"crime_type": "BATTERY", "latitude": 41.85, "longitude": -87.65, "risk": "Low"}
    ]