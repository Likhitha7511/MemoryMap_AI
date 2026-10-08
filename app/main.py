import streamlit as st
from PIL import Image

from detector import detect
from database import init_db, add_observation, latest_observation, all_observations

st.set_page_config(page_title="MemoryMap AI", page_icon="🧠", layout="wide")
init_db()

st.title("🧠 MemoryMap AI")
st.caption("Your visual memory — detect, remember, and retrieve objects.")

tab1, tab2 = st.tabs(["📸 Add Memory", "🔎 Find Object"])

with tab1:
    st.subheader("Add a visual memory")
    uploaded = st.file_uploader("Upload a room/photo image", type=["jpg", "jpeg", "png"])
    location = st.text_input("Location label", placeholder="Study Table, Bedroom, Lab")

    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Uploaded image", width=650)

        if st.button("Remember this scene", type="primary"):
            if not location.strip():
                st.warning("Please enter a location.")
            else:
                detections = detect(image)
                stored = 0

                for d in detections:
                    if d["confidence"] >= 0.45:
                        add_observation(d["object_name"], d["confidence"], location.strip())
                        stored += 1

                if stored:
                    st.success(f"Stored {stored} object observations.")
                else:
                    st.info("No supported objects were detected with enough confidence.")

                st.write("Detected objects:")
                for d in detections:
                    st.write(f"• **{d['object_name']}** — {d['confidence']:.0%}")

with tab2:
    st.subheader("Where did I see it?")
    object_name = st.text_input("Object name", placeholder="laptop, bottle, backpack, phone")

    if st.button("Search memory", type="primary"):
        if not object_name.strip():
            st.warning("Enter an object name.")
        else:
            result = latest_observation(object_name.strip())

            if result:
                name, confidence, location, timestamp = result
                st.success(
                    f"📍 **{name.title()}** was last seen at **{location}** on **{timestamp}**."
                )
                st.write(f"Detection confidence: {confidence:.0%}")
            else:
                st.error("I don't have a memory of that object yet.")

    st.divider()
    st.subheader("Memory timeline")
    rows = all_observations()

    if rows:
        st.dataframe(
            [
                {"Object": r[0], "Confidence": f"{r[1]:.0%}",
                 "Location": r[2], "Time": r[3]}
                for r in rows
            ],
            use_container_width=True
        )
    else:
        st.info("No memories stored yet.")
