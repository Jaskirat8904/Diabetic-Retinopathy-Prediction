import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import pandas as pd
import time

# ───────────────────────────────────────────────
# 1. Advanced Page Config & Styling
# ───────────────────────────────────────────────
st.set_page_config(
    page_title="RetinaScan AI Pro • Clinical Portal",
    page_icon="👁️",
    layout="wide"
)

# Deep Clinical Theme
st.markdown("""
    <style>
    .main { background-color: #f1f5f9; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #0f172a; color: white; }
    .report-card { background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); border-top: 5px solid #3b82f6; }
    .metric-value { font-size: 2.5rem; font-weight: 800; color: #1e293b; }
    .status-tag { padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# 2. Medical Image Preprocessing (Advanced)
# ───────────────────────────────────────────────
def clinical_preprocess(image):
    """Advanced clinical preprocessing for fundus images."""
    # 1. Auto-crop black borders (Standard in medical AI)
    img_array = np.array(image)
    mask = img_array > 10
    if mask.any():
        coords = np.argwhere(mask)
        y0, x0, _ = coords.min(axis=0)
        y1, x1, _ = coords.max(axis=0)
        image = image.crop((x0, y0, x1, y1))
    
    # 2. Resizing & Normalization
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

# ───────────────────────────────────────────────
# 3. Model Loading
# ───────────────────────────────────────────────
@st.cache_resource
def load_model():
    model = models.resnet152(weights=None)
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, 512),
        nn.ReLU(),
        nn.Linear(512, 5),
        nn.LogSoftmax(dim=1)
    )
    # Ensure classifier.pt is in the same folder
    checkpoint = torch.load("classifier.pt", map_location="cpu", weights_only=False)
    if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
        model.load_state_dict(checkpoint['model_state_dict'])
    else:
        model.load_state_dict(checkpoint)
    model.eval()
    return model

# ───────────────────────────────────────────────
# 4. Main UI Layout
# ───────────────────────────────────────────────
# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2864/2864350.png", width=60)
    st.title("RetinaScan AI")
    st.markdown("---")
    st.write("**Patient Metadata**")
    p_name = st.text_input("Full Name", "Anonymous Patient")
    p_age = st.number_input("Age", 18, 100, 45)
    st.write("---")
    st.caption("Architecture: ResNet-152 Deep Residual Network")

# Header
st.title("🏥 Clinical Diagnostic Portal")
st.markdown(f"**Session ID:** `DR-SCAN-{int(time.time())}`")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📸 Retinal Acquisition")
    uploaded_file = st.file_uploader("Upload fundus image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Original Fundus Photography", use_container_width=True)
        
        if st.button("🚀 Analyze Patient Image"):
            with st.spinner("Executing Deep Feature Extraction..."):
                model = load_model()
                tensor = clinical_preprocess(img)
                
                with torch.no_grad():
                    output = model(tensor)
                    probs = torch.exp(output)[0].numpy()
                    pred_idx = int(probs.argmax())
                
                st.session_state['results'] = {
                    'idx': pred_idx,
                    'probs': probs,
                    'time': time.strftime("%H:%M:%S")
                }

with col2:
    st.subheader("🧠 Diagnostic Intelligence")
    if 'results' in st.session_state:
        res = st.session_state['results']
        class_names = ['No DR', 'Mild NPDR', 'Moderate NPDR', 'Severe NPDR', 'Proliferative DR']
        colors = ['#22c55e', '#f59e0b', '#f97316', '#ef4444', '#b91c1c']
        
        # Main Diagnostic Card
        st.markdown(f"""
            <div class="report-card">
                <span class="status-tag" style="background: {colors[res['idx']]}22; color: {colors[res['idx']]};">
                    Primary Diagnosis
                </span>
                <div class="metric-value" style="color: {colors[res['idx']]};">
                    {class_names[res['idx']]}
                </div>
                <div style="font-size: 1.1rem; color: #64748b;">
                    Confidence: <b>{res['probs'][res['idx']]*100:.1f}%</b>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Clinical Recommendations
        recs = [
            "Normal findings. Standard annual diabetic eye exam.",
            "Schedule follow-up within 12 months for monitoring.",
            "Referral to Ophthalmology suggested within 4 months.",
            "High-risk detection. Urgent specialist referral required.",
            "Critical finding. Immediate ophthalmology consultation necessary."
        ]
        
        st.info(f"**Clinical Recommendation:** {recs[res['idx']]}")
        
        # Probability Distribution
        st.write("**Feature Distribution (%)**")
        chart_data = pd.DataFrame({
            "Stage": ['No DR', 'Mild', 'Mod', 'Sev', 'PDR'],
            "Score": res['probs'] * 100
        })
        st.bar_chart(chart_data.set_index("Stage"))

        # Report Action
        if st.button("📋 Generate Clinical Summary"):
            st.success("Summary ready. In a real-world app, this would trigger a PDF download.")
            st.code(f"""
            --- CLINICAL SUMMARY ---
            Patient: {p_name} | Age: {p_age}
            Diagnosis: {class_names[res['idx']]}
            Timestamp: {res['time']}
            ------------------------
            """)

    else:
        st.markdown("""
            <div style="text-align: center; padding: 50px; color: #94a3b8; border: 2px dashed #cbd5e1; border-radius: 15px;">
                Awaiting input data. Please upload a retinal fundus image to begin analysis.
            </div>
        """, unsafe_allow_html=True)

# ───────────────────────────────────────────────
# 5. Explanatory Diagram (Project Value)
# ───────────────────────────────────────────────

st.write("---")
with st.expander("ℹ️ About the Technology"):
    st.write("""
    This system utilizes a **ResNet-152 (Residual Network)** architecture. 
    By using 'skip connections', the model can train 152 layers deep without suffering from the vanishing gradient problem, 
    allowing it to pick up microscopic retinal features like microaneurysms and hemorrhages.
    """)
