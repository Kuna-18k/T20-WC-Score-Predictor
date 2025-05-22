# 🏏 T20 World Cup Score Predictor

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Build-Active-brightgreen?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> ⚡ Predict final scores and match outcomes of T20 World Cup games using real-time input and machine learning — powered by an elegant Streamlit interface.

---

## 🎯 Project Goals

- ✅ Predict **1st innings final score** based on match situation
- ✅ Estimate **2nd innings win probability** using dynamic features
- ✅ Provide a clean and responsive **Streamlit web UI**
- ✅ Serve as a base for future cricket analytics tools

---

## 📺 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-deployment-link)

![Preview](https://user-images.githubusercontent.com/yourusername/t20-predictor-demo.gif)
*Preview of the score prediction interface. (Add your image or GIF above)*

---

## 🧠 How It Works

The app takes real-time inputs (like runs, overs, wickets) and feeds them into a trained ML model which uses cricket-specific features to make predictions.

### 🔍 Features Engineered:

| Feature               | Description                              |
|-----------------------|------------------------------------------|
| `runs`                | Current runs scored                      |
| `wickets`             | Wickets lost so far                      |
| `overs`               | Overs completed                          |
| `balls_left`          | Balls remaining in the innings (120 - bowled) |
| `run_rate`            | Current run rate                         |
| `required_run_rate`   | Target chase required rate (2nd innings) |

---

## 🧱 Project Structure

```bash
t20-score-predictor/
├── app/
│   ├── __init__.py
│   ├── ui.py              # Streamlit components
│   ├── utils.py           # Feature engineering helpers
│   └── predictor.py       # ML model loader and prediction
├── model/
│   └── t20_model.pkl      # Trained model file
├── notebooks/
│   └── feature-extraction.ipynb
├── app.py                 # Main Streamlit app entry point
├── requirements.txt       # Dependencies
├── README.md              # Project overview (this file)
└── LICENSE
