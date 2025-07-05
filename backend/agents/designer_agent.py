import requests

def call_hf_space(prompt, image_path):
    url = "https://chetan1209-black-forest-labs-FLUX-1-Kontext-dev.hf.space/infer"
    with open(image_path, "rb") as img_file:
        files = {"image": img_file}
        data = {"prompt": prompt}
        response = requests.post(url, data=data, files=files)
    response.raise_for_status()
    return response.json()["image_url"]

class designer_agent:
    @staticmethod
    def run(prompt, image_path):
        result_url = call_hf_space(prompt, image_path)
        print("Result from Space:", result_url)
        return result_url