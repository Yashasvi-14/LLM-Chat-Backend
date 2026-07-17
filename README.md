![Python](https://img.shields.io/badge/Python-3.x-blue)
![Gemini](https://img.shields.io/badge/LLM-Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-green)

# LLM Chat Backend

A modular Python backend for building LLM-powered conversational applications. The project focuses on clean software architecture, configurable prompts, conversation management, and provider abstraction, making it easy to integrate different Large Language Models while maintaining a scalable codebase.

---

## ✨ Features

- 🤖 Gemini API integration for conversational AI
- 💬 Conversation history management
- 📝 Configurable system prompts
- 🔄 Modular LLM provider abstraction
- ⚙️ Environment-based configuration
- 📋 Centralized logging
- 🧪 Unit testing with mock LLM implementations
- 📦 Clean and extensible project structure

---

## 🏗️ Project Architecture

```
                User Input
                     │
                     ▼
                 main.py
                     │
                     ▼
             Chatbot Controller
                     │
                     ▼
         Conversation Management
                     │
                     ▼
          LLM Provider Interface
                     │
          ┌──────────┴──────────┐
          │                     │
      Gemini Provider      Future Providers
```

The project is designed around abstraction, allowing additional LLM providers (OpenAI, Claude, etc.) to be integrated with minimal changes.

---

## 📂 Project Structure

```
LLM-Chat-Backend/
│
├── chatbot/          # Chat orchestration and conversation handling
├── config/           # Environment configuration
├── llm/              # Provider abstraction and Gemini implementation
├── prompts/          # System prompts
├── tests/            # Test utilities and mock implementations
├── utils/            # Logging utilities
│
├── main.py           # Application entry point
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- python-dotenv
- Logging
- Object-Oriented Programming (OOP)

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/Yashasvi-14/LLM-Chat-Backend.git

cd LLM-Chat-Backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file.

Example:

```env
GOOGLE_API_KEY=your_api_key
MODEL_NAME=gemini-2.5-flash
LOG_LEVEL=INFO
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📌 Current Capabilities

- Interactive chat with Gemini
- Conversation context management
- Configurable system prompts
- Provider abstraction for future extensibility
- Structured logging

---

## 🔮 Future Improvements

- FastAPI REST API
- Multi-provider support (OpenAI, Claude)
- Streaming responses
- Authentication & Authorization
- Persistent conversation storage
- Docker support
- Unit and integration tests
- Deployment on Render / Railway

---

## 📚 Learning Objectives

This project was built to explore:

- Large Language Model integration
- Backend software architecture
- Provider abstraction
- Conversation management
- Modular Python application design
- Configuration management

---

## 👨‍💻 Author

**Yashasvi Tekriwal**

DTU | Backend & AI Engineering Enthusiast

GitHub: https://github.com/Yashasvi-14
