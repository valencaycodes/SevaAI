# SevaAI
# 🤖 SevaAI – Your Empathetic Health Companion  
*A Baymax-inspired AI assistant that listens, cares, and supports.*


---

## 🧠 Overview

**SevaAI** is a voice-enabled, emotion-aware health assistant built to offer **first-level symptom support**, detect **emotional well-being**, and act as a **compassionate digital companion** — especially for the elderly, chronically ill, and isolated individuals. Inspired by *Baymax* from *Big Hero 6*, SevaAI brings empathy and functionality into a practical, real-world AI prototype.

---

## 🚀 Features

- 🎤 **Voice Input & Output** (Hindi/English)
- 💬 Understands user-reported symptoms using NLP
- 😟 Detects emotional tone in real-time conversations
- 🆘 Responds to emergency phrases with alerts
- 📋 Offers general well-being advice (rule-based)
- 🌐 Lightweight, offline-first design with potential for app/web integration

---

## 💡 Use Cases

- Elderly home care or companionship  
- First-response assistant in rural areas  
- Mental health support and emotional tracking  
- Health information tool for underserved communities  
- Voice-based interface for non-tech-savvy users

---

## ⚙️ Tech Stack

| Component          | Technology                      |
|--------------------|----------------------------------|
| Voice Recognition  | SpeechRecognition (Google API)   |
| Text-to-Speech     | pyttsx3 (local TTS)              |
| Emotion Detection  | HuggingFace Transformers (RoBERTa) |
| Symptom Checker    | Rule-based logic (can be upgraded to NLP/ML) |
| Language Support   | Multilingual (Hindi/English)     |



---

## 📌 How It Works

1. **User speaks** their symptoms or feelings.
2. SevaAI **transcribes the speech** to text using Google Speech API.
3. It detects **emotions using a pre-trained model** (e.g., "sad", "angry", "happy").
4. The assistant **analyzes keywords** to detect known symptoms (e.g., fever, headache).
5. If urgent terms like "emergency", "pain", or "help" are detected, it responds accordingly.
6. SevaAI **speaks back** a helpful or empathetic response in natural voice.

---

## 🔐 Disclaimer

> **SevaAI is not a substitute for professional medical advice.**  
Always consult a licensed physician or healthcare provider. This tool is for **informational purposes only**. In case of a medical emergency, call emergency services immediately.

---

## 📈 Future Improvements

- 📱 Android/iOS integration with Flutter or React Native  
- 🧠 ML-based dynamic symptom analysis (beyond rules)  
- 👨‍⚕️ Doctor/hospital API integration (e.g., telemedicine)  
- 🗂️ Session history and care reports  
- 🏥 Integration with health records (FHIR standard)

---

## 👥 Team

- **You (Richa Rana & Diya Patel)** – Concept, design, coding  
- Collaborators and mentors to be added

---

## 🤝 Contributing

Pull requests and feedback are welcome. If you'd like to contribute to SevaAI, feel free to fork the repository and propose new features!

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🏆 Submission

This project is developed for the **Maverick Effect AI Challenge 2025**, under the theme:  
**"Technology for Healthcare Access and Empathy."**
