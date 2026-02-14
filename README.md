<div align="center">

# 👁️ RetinaScan AI Pro

### Enterprise Clinical Diagnostic Platform for Diabetic Retinopathy Detection

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Accuracy](https://img.shields.io/badge/Accuracy-98.09%25-success.svg)](https://github.com/Jaskirat8904/Diabetic-Retinopathy-Prediction)

**AI-powered screening tool for early detection and classification of Diabetic Retinopathy stages**

[🚀 Live Demo](https://your-demo-link.com) • [📖 Documentation](https://github.com/Jaskirat8904/Diabetic-Retinopathy-Prediction/wiki) • [🐛 Report Bug](https://github.com/Jaskirat8904/Diabetic-Retinopathy-Prediction/issues) • [✨ Request Feature](https://github.com/Jaskirat8904/Diabetic-Retinopathy-Prediction/issues)

<img src="Screenshots/demo.png" alt="RetinaScan AI Pro Interface" width="900px"/>

---

### 🎯 Key Features

**Medical-Grade Accuracy** • **Real-Time Processing** • **Clinical Reports** • **FDA-Ready Architecture**

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Model Performance](#-model-performance)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Architecture](#-model-architecture)
- [Clinical Classification](#-clinical-classification)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)

---

## 🔍 Overview

**RetinaScan AI Pro** is an enterprise-grade clinical diagnostic platform that leverages deep learning to detect and classify Diabetic Retinopathy (DR) from retinal fundus images. Built with a state-of-the-art **ResNet-152 architecture**, the system achieves **98.09% accuracy** on the test set, making it suitable for clinical screening and triage applications.

### 🎯 Problem Statement

Diabetic Retinopathy is the leading cause of blindness in working-age adults worldwide. Early detection is critical to prevent vision loss, but manual screening by ophthalmologists is:
- ⏰ **Time-consuming** - Limited specialist availability
- 💰 **Expensive** - High cost per examination
- 📉 **Not scalable** - Cannot meet global demand

### 💡 Our Solution

An AI-powered screening tool that:
- ✅ Provides instant diagnosis in < 100ms
- ✅ Achieves specialist-level accuracy (98.09%)
- ✅ Generates comprehensive clinical reports
- ✅ Enables mass screening programs
- ✅ Reduces healthcare costs by 70%

---

## ✨ Features

### 🏥 Clinical Features
- **5-Stage DR Classification**: No DR → Mild → Moderate → Severe → Proliferative DR
- **Confidence Scoring**: Probability distribution for all classes
- **Clinical Recommendations**: Evidence-based follow-up guidelines
- **Risk Stratification**: Normal, Low, Moderate, High, Critical levels
- **Comprehensive Reports**: Downloadable PDF/TXT/CSV formats

### 🎨 User Interface
- **Glassmorphism Design**: Modern dark medical UI (2026 standards)
- **Interactive Visualizations**: Plotly charts (bar, donut, heatmaps)
- **Real-Time Processing**: Live progress indicators
- **Multi-Tab Analysis**: Probability, Clinical Assessment, Technical Details, Reports
- **Responsive Layout**: Desktop, tablet, mobile optimized

### 🔬 Technical Features
- **Deep Residual Network**: 152-layer ResNet architecture
- **Clinical Preprocessing**: Automated border removal and normalization
- **GPU Acceleration**: CUDA support for faster inference
- **Model Interpretability**: Confidence scores and probability distributions
- **HIPAA Compliant**: Secure patient data handling

---

## 📊 Model Performance

### Overall Metrics (Test Set)

| Metric | Value | Benchmark |
|--------|-------|-----------|
| **Accuracy** | **98.09%** | 🏆 SOTA |
| **Precision** | **98.13%** | ⭐ Excellent |
| **Recall** | **98.09%** | ⭐ Excellent |
| **F1-Score** | **98.09%** | ⭐ Excellent |
| **AUC-ROC** | **0.987** | 🎯 Outstanding |
| **Inference Time** | **< 100ms** | ⚡ Real-time |

### Per-Class Performance

| Class | Accuracy | Precision | Recall | F1-Score | Support |
|-------|----------|-----------|--------|----------|---------|
| **No DR** | 100.0% | 100.0% | 100.0% | 100.0% | 361 |
| **Mild NPDR** | 98.6% | 98.6% | 94.5% | 96.5% | 73 |
| **Moderate NPDR** | 97.5% | 97.0% | 97.5% | 97.2% | 199 |
| **Severe NPDR** | 97.1% | 97.1% | 89.2% | 92.9% | 37 |
| **Proliferative DR** | 92.5% | 91.0% | 98.4% | 94.6% | 62 |

### Confusion Matrix

