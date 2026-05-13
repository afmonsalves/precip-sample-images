import os
import json
import random

# Configuration
base_github_url = "https://afmonsalves.github.io/precip-sample-images/"

directories_config = [
    {"folder": "./IDK_samples", "url_path": "IDK_samples/", "sample_size": 40},
    {"folder": "./regular_samples", "url_path": "regular_samples/", "sample_size": 5},
    {"folder": "./artifact_samples", "url_path": "artifact_samples/", "sample_size": 5}
]

def generate_js_array(config_list, base_url):
    images_list = []
    
    for config in config_list:
        directory = config["folder"]
        url_path = config["url_path"]
        sample_size = config["sample_size"]
        
        if not os.path.exists(directory):
            print(f"Warning: Directory {directory} not found. Skipping.")
            continue

        files = sorted([f for f in os.listdir(directory) if f.endswith('.png')])
        
        # Randomly select a subset of files without replacement
        if len(files) > sample_size:
            files = random.sample(files, sample_size)
            
        for filename in files:
            image_id = os.path.splitext(filename)[0]
            image_url = f"{base_url}{url_path}{filename}"
            images_list.append({"id": image_id, "url": image_url})
    
    return "const allImages = " + json.dumps(images_list, indent=2) + ";"

if __name__ == "__main__":
    output = generate_js_array(directories_config, base_github_url)
    with open("array_output.txt", "w") as f:
        f.write(output)