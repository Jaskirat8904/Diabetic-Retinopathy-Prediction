# Diabetic Retinopathy Prediction

👁️ **AI-powered screening tool for early detection of Diabetic Retinopathy stages**

Built with **Streamlit** • **ResNet-152** • **98.09% validation accuracy**

---

## 🌟 Project Highlights

- Single-file **Streamlit** web application  
- Upload fundus image or use webcam  
- Instant prediction of DR severity (5 classes)  
- Confidence percentage displayed  
- Clean clinical-style recommendation text  
- Probability bar chart visualization  
- Simple report generation & download  

**Classes predicted**  
No DR • Mild NPDR • Moderate NPDR • Severe NPDR • Proliferative DR

---

## 📊 Model Performance (Test Set)

| Metric       | Value     |
|--------------|-----------|
| Accuracy     | **98.09%** |
| Precision    | 98.13%    |
| Recall       | 98.09%    |
| F1-Score     | 98.09%    |

### Confusion Matrix

| Actual \ Predicted | No DR | Mild | Moderate | Severe | PDR |
|---------------------|-------|------|----------|--------|-----|
| **No DR**           | 361   | 0    | 0        | 0      | 0   |
| **Mild**            | 0     | 69   | 3        | 0      | 1   |
| **Moderate**        | 0     | 1    | 194      | 1      | 3   |
| **Severe**          | 0     | 0    | 2        | 33     | 2   |
| **PDR**             | 0     | 0    | 1        | 0      | 61  |

---

## 🚀 How to Run Locally

### Requirements

```bash
pip install streamlit torch torchvision torchaudio pillow numpy pandas matplotlib
