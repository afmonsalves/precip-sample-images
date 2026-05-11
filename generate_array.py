import os
import json

# Configuration
local_image_directory = "./IDK_samples" 
github_base_url = "https://afmonsalves.github.io/precip-sample-images/IDK_samples/"

def generate_js_array(directory, base_url):
    images_list = []
    files = sorted([f for f in os.listdir(directory) if f.endswith('.png')])
    
    for filename in files:
        image_id = os.path.splitext(filename)[0]
        image_url = f"{base_url}{filename}"
        images_list.append({"id": image_id, "url": image_url})
    
    return "const images = " + json.dumps(images_list, indent=2) + ";"

if __name__ == "__main__":
    output = generate_js_array(local_image_directory, github_base_url)
    with open("array_output.txt", "w") as f:
        f.write(output)
