

from inference_sdk import InferenceHTTPClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=os.getenv("ROBOFLOW_API_KEY")
)

# 3. Run your workflow on an image
result = client.run_workflow(
    workspace_name="akaiya-abdullah-yahoo-com",
    workflow_id="find-dresses-shirts-jackets-shoes-skirts-socks-and-pants",
    images={
        "image": "YOUR_IMAGE.jpg" # Path to your image file
    },
    use_cache=True # Speeds up repeated requests
)

# 4. Get your results
print(result)
