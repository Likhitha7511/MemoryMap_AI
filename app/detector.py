import streamlit as st
from ultralytics import YOLO

@st.cache_resource
def load_model():
    return YOLO("yolo11s.pt")

def detect(image):
    model = load_model()
    results = model(image, verbose=False)
    detections = []

    for result in results:
        names = result.names
        if result.boxes is None:
            continue

        for box in result.boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            detections.append({
                "object_name": names[cls_id],
                "confidence": confidence,
                "box": [float(x) for x in box.xyxy[0]]
            })
    return detections
