# classificationModel.py

import os
import time
import shutil

from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
from collections import defaultdict
from database import add_clothing

# Load API key from .env
load_dotenv("private/.env")

API_KEY = os.getenv("ROBOFLOW_API_KEY")

# Initialize client
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key = API_KEY
)

def main():
    result = client.infer(
        "sampleShirt.jpeg",
        model_id="clothes-classification-jq2gs/3"
    )

    predictions = result.get("predictions", [])

    if not predictions:
        print("No predictions found.")
        return

    best_scores = defaultdict(float)

    for p in predictions:
        label = p.get("class", "unknown")
        confidence = p.get("confidence", 0)

        if label == "pant":
            label = "pants"
        elif label == "shoes":
            label = "shoe"
        elif label == "t-shirt":
            label = "shirt"

        if confidence > best_scores[label]:
            best_scores[label] = confidence

    sorted_results = sorted(best_scores.items(), key=lambda x: x[1], reverse=True)

    for label, confidence in sorted_results:
        print(f"{label} — {confidence * 100:.2f}%")

        # STORE ONLY GOOD RESULTS
        if confidence > 0.7:
            add_clothing(label, confidence, "sampleShirt.jpeg")

    original_path = "sampleShirt.jpeg"
    image_name = f"image_{int(time.time())}.jpg"
    shutil.copy(original_path, image_name)  
    add_clothing(label, confidence, image_name)

import sqlite3

conn = sqlite3.connect("wardrobe.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM clothes")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

if __name__ == "__main__":
    main()