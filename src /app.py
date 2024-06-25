import requests
from io import BytesIO
import numpy as np
import rasterio

def main(image_url: str) -> str:
    response = requests.get(image_url)
    if response.status_code != 200:
        return f"Failed to fetch image: {response.status_code}"

    with rasterio.MemoryFile(BytesIO(response.content)) as memfile:
        with memfile.open() as dataset:
            data = dataset.read(1)  # Read the first band
            anomaly_detected = np.mean(data) > 100  # Simplistic threshold

    if anomaly_detected:
        return "Anomaly detected!"
    else:
        return "No anomaly detected."

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python app.py <image_url>")
    else:
        result = main(sys.argv[1])
        print(result)
