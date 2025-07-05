# agent_controller.py
# ADK-based orchestrator logic for RoomVision



from agents.amazon_agent import amazon_agent
from agents.designer_agent import designer_agent
from agents.extractor_agent import extractor_agent

class RoomVisionPipeline:
    @staticmethod
    def run(data):
        # data should be a dict with keys 'prompt' and 'image'
        design_prompt = designer_agent.run(data['prompt'], data['image'])
        extracted_items = extractor_agent.run(data['image'])
        return {
            'design_result': design_prompt,
            'extracted_items': extracted_items
        }





