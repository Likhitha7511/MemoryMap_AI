# MemoryMap AI — Project Plan

## Phase 1 — MVP
1. YOLO object detection
2. Image upload
3. Location labeling
4. SQLite memory
5. Last-seen object search
6. Streamlit dashboard

## Phase 2 — Make it truly unique
### Physical object re-identification
Use a Siamese/Triplet network to create embeddings so two different laptops,
bottles, or bags are not treated as the same object.

### Video memory
Add tracking so the system follows an object between frames.

### Personal movement model
Learn sequences such as:
Study Table -> Backpack -> Classroom -> Hostel

Use an LSTM/Transformer to estimate likely next locations.

### Natural-language retrieval
Support questions such as:
- Where did I last see my charger?
- When did I see my backpack?
- Where do I usually keep my keys?

## Evaluation
Measure detection precision/recall, re-identification accuracy,
top-1/top-3 location retrieval accuracy, inference time, and retrieval latency.
