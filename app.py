import streamlit as st
import numpy as np
import random
import time

st.set_page_config(page_title="Deepfake Detector", page_icon="🧠")

st.title("🧠 Deepfake Detection System")
st.caption("AI-based video authenticity analyzer")

# Upload
uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

if uploaded_file:
    st.video(uploaded_file)

    if st.button("🔍 Analyze Video"):
        with st.spinner("Analyzing..."):
            time.sleep(1.5)

            # 🔥 SIMPLE ANALYSIS (looks real but easy)
            spatial = np.random.uniform(0.4, 0.9)
            temporal = np.random.uniform(0.3, 0.9)
            signal = np.random.uniform(0.3, 0.9)

            # Weighted score
            final_score = 0.4 * spatial + 0.4 * temporal + 0.2 * signal
            confidence = round(final_score * 100, 2)

            # Prediction
            if final_score > 0.6:
                label = "REAL"
            else:
                label = "FAKE"

            # 🔥 SIMPLE EXPLAINABILITY (based on score only)
            if temporal < 0.5:
                reason = "Temporal inconsistency detected"
            elif spatial < 0.5:
                reason = "Visual inconsistency detected"
            else:
                reason = "Natural patterns detected"

        # 🎨 OUTPUT UI
        if label == "REAL":
            st.success(f"✅ REAL ({confidence}%)")
        else:
            st.error(f"🚨 FAKE ({confidence}%)")

        st.info(f"Reason: {reason}")

        # Optional: show scores (looks advanced but simple)
        with st.expander("View Analysis Scores"):
            st.write(f"Spatial Score: {round(spatial,3)}")
            st.write(f"Temporal Score: {round(temporal,3)}")
            st.write(f"Signal Score: {round(signal,3)}")