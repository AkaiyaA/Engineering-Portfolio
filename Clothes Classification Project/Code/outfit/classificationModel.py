# classificationModel.py

import os
from pathlib import Path
import time
import shutil

from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
from collections import defaultdict
from database import BASE_DIR, add_clothing, get_clothes, init_db

# Load API key from .env
load_dotenv("/Users/akaiyaa/Desktop/Engineering-Portfolio/Clothes Classification Project/Code/.env")

API_KEY = os.getenv("ROBOFLOW_API_KEY")

# Initialize client
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key = API_KEY
)

def main():

    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent
    image_path = BASE_DIR / "samplePants2.jpeg"

    result = client.infer(
        str(image_path),
        model_id="clothes-classification-jq2gs/6"
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
            add_clothing(label, confidence, "samplePants2.jpeg")

    original_path = str(image_path)
    
    folder = "./wardrobeImages"
    os.makedirs(folder, exist_ok=True)

    best_label = sorted_results[0][0] if sorted_results else "unknown"
    image_name = os.path.join(folder, f"{best_label}_image_{int(time.time())}.jpg")

    shutil.copy(original_path, image_name)  

    for row in get_clothes():
        print(row)

if __name__ == "__main__":
    main()