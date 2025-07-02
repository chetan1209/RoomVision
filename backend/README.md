# RoomVision Backend

This backend orchestrates the RoomVision multi-agent workflow using Google Cloud's Agent Development Kit (ADK).

## Structure
- **agents/**: Specialized agents for annotation, design, extraction, and Amazon product search.
- **orchestrator/**: Orchestrates agent workflow and communication.
- **static/**: Hosts output images for frontend access.
- **uploads/**: Stores user-uploaded room images.
- **utils/**: Helper scripts for image processing, API calls, and logging.
- **app.py**: Flask entrypoint.
- **requirements.txt**: Python dependencies.
