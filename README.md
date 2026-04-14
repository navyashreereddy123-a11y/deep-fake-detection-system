# 🛡️ DeepGuard — Deepfake Video Detection System

> Multi-signal deepfake detection using Spatial, Temporal & rPPG Signal Analysis  
> Provides **Prediction + Confidence Score + Reason** — fully explainable output.

---

## 🧠 How It Works

```
Input Video → Frame Extraction → 3-Signal Analysis → Score Fusion → Explainable Output
```

| Signal | Method | What It Checks |
|--------|--------|----------------|
| 👁️ Spatial | MediaPipe Face Mesh + Laplacian | Face texture, sharpness, landmark asymmetry |
| 🎬 Temporal | Farneback Optical Flow | Motion consistency across frames |
| 💓 Signal | rPPG (Green channel FFT) | Physiological blood-flow signal in face |

---

## ⚙️ Requirements

- Python 3.9 or 3.10 (recommended)
- pip

---

## 🚀 Steps to Run

### Step 1 — Clone / create project folder
```bash
mkdir deepfake_detector
cd deepfake_detector
# Place all .py files and requirements.txt here
```

### Step 2 — Create virtual environment (recommended)
```bash
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run CLI test (optional)
```bash
python main.py --video path/to/your_video.mp4
```

### Step 5 — Launch Streamlit UI
```bash
streamlit run app.py
```
Open browser at: **http://localhost:8501**

---

## 📤 Output Explanation

```
PREDICTION  : FAKE  (or REAL)
CONFIDENCE  : 87.3%
REASON      : Detected: no physiological rPPG signal; inconsistent motion between frames.

Sub-scores:
  Spatial   : 34.1%  (FAKE)
  Temporal  : 41.2%  (FAKE)
  Signal    : 20.0%  (FAKE)
```

- **Spatial score** — how natural the face texture looks
- **Temporal score** — how consistent the motion is frame-to-frame
- **Signal score** — whether a real physiological pulse signal is present
- **Confidence** — how certain the system is about its prediction

---

## 📁 File Structure

```
deepfake_detector/
├── app.py            ← Streamlit UI
├── main.py           ← CLI runner
├── analyzer.py       ← Core detection engine (3 analyzers + fusion)
├── utils.py          ← Frame extraction + helper functions
├── requirements.txt  ← Dependencies
└── README.md         ← This file
```

---

## 🧪 Test Videos

- Fake videos: [FaceForensics++ Dataset](https://github.com/ondyari/FaceForensics)
- Real videos: any front-facing camera footage

-
