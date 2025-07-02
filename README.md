# RoomVision

RoomVision is a multi-agent system that transforms a plain photo of a user's room into a beautifully redesigned version based on their style preference — and then recommends shoppable furniture from Amazon that matches the new look. Built using Google Cloud's Agent Development Kit (ADK), RoomVision orchestrates specialized AI agents to analyze, redesign, and source products in an automated, personalized workflow.

## 🧠 Features & Functionality
- **Upload Room Photo:** Users upload a photo of their current room.
- **Select Design Prompt:** Users describe the aesthetic they want (e.g., "Scandinavian with plants").
- **AI Room Generation:** The system generates a 2D image of the room with the new style applied.
- **Object Extraction:** AI identifies individual furniture/decor items in the generated image.
- **Amazon Recommendations:** Items are matched to real products on Amazon with purchase links.

## Project Structure
```
RoomVision/
├── backend/
│   ├── agents/
│   │   ├── annotator_agent.py
│   │   ├── designer_agent.py
│   │   ├── extractor_agent.py
│   │   ├── amazon_agent.py
│   │   └── __init__.py
│   ├── orchestrator/
│   │   ├── agent_controller.py
│   │   └── __init__.py
│   ├── static/
│   ├── uploads/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.vue / App.jsx
│   │   └── main.js / main.ts
│   ├── index.html
│   ├── package.json
│   └── README.md
├── data/
│   └── sample_images/
├── utils/
│   ├── image_helpers.py
│   ├── api_helpers.py
│   └── logger.py
├── .gitignore
├── architecture_diagram.png
├── demo_script.md
├── submission_notes.md
└── README.md
```
