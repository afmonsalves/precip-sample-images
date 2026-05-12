import os
import json
import random

# Configuration
local_image_directory = "./IDK_samples" 
github_base_url = "https://afmonsalves.github.io/precip-sample-images/IDK_samples/"

def generate_js_array(directory, base_url, sample_size=40):
    images_list = []
    files = sorted([f for f in os.listdir(directory) if f.endswith('.png')])
    
    # Randomly select a subset of files without replacement
    if len(files) > sample_size:
        files = random.sample(files, sample_size)
        
    for filename in files:
        image_id = os.path.splitext(filename)[0]
        image_url = f"{base_url}{filename}"
        images_list.append({"id": image_id, "url": image_url})
    
    # Outputting 'allImages' to match the variable required by the Index.html script
    return "const allImages = " + json.dumps(images_list, indent=2) + ";"

if __name__ == "__main__":
    output = generate_js_array(local_image_directory, github_base_url)
    with open("array_output.txt", "w") as f:
        f.write(output)