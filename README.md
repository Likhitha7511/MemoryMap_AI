# MemoryMap AI
A Deep Learning Based Visual Memory System for Personal Object Retrieval.

## What it does
Upload a photo of a room, give the location a name, and MemoryMap AI detects
objects and remembers where/when they were seen. Later you can search for an
object and retrieve its latest known location.

## Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/main.py
```

The first run downloads the lightweight YOLO model through Ultralytics.

## Architecture
Image -> YOLO detector -> SQLite memory -> object search -> dashboard

## Research upgrades
- Siamese/Triplet network for physical-object re-identification
- YOLO tracking for video
- LSTM/Transformer for movement patterns
- Personalized next-location prediction
