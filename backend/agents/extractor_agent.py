# extractor_agent.py
# Handles object recognition from AI-generated images

# TODO: Implement extraction logic

from utils.api_helpers import extraction_helper

class ExtractorAgent:
    def run(self, image_path):
        print(f"[ExtractorAgent] Extracting objects from: {image_path}")
        items_text = extraction_helper(image_path)
        items = [item.strip() for item in items_text.split('\n') if item.strip()]
        return items

extractor_agent = ExtractorAgent()
