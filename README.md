# MemoryMap AI
A Deep Learning Based Visual Memory System for Personal Object Retrieval.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://memorymap-ai.streamlit.app/)

🔗 **Live Application:** [https://memorymap-ai.streamlit.app/](https://memorymap-ai.streamlit.app/)

## What it does
Upload a photo of a room, give the location a name, and MemoryMap AI detects
objects and remembers where/when they were seen. Later you can search for an
object and retrieve its latest known location.

## Run Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app/main.py
```
*(or `streamlit run app/main.py`)*

The first run downloads the lightweight YOLO model through Ultralytics.

## Architecture
Image -> YOLO detector -> SQLite memory -> object search -> dashboard

## Research upgrades
- Siamese/Triplet network for physical-object re-identification
- YOLO tracking for video
- LSTM/Transformer for movement patterns
- Personalized next-location prediction
