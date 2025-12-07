🌱 CodeRoot AI — Local Code Explanation Engine
Powered by Ollama + CodeLlama

CodeRoot AI is a privacy-focused, offline code explanation engine that uses CodeLlama through Ollama to interpret and explain code instantly. It ensures that your code stays on your machine, offering fast, secure, and intelligent analysis without depending on cloud services.

🧩 Project Description

CodeRoot AI is designed to help developers understand unfamiliar or complex code by generating clear, human-readable explanations directly from their local machine. With its modular architecture and simple command-line interface, it delivers fast, private, and offline code intelligence using open-source LLM models.
Built for students, developers, and researchers, CodeRoot AI combines portability, performance, and complete code privacy.

🚀 Features

🧠 AI-powered code understanding using CodeLlama

🔒 Fully offline — code never leaves your machine

⚡ Fast and lightweight

🖥️ CLI-based simple interface

📦 Modular and extensible architecture

🧩 Works on Windows, macOS, and Linux

🛠️ Requirements
1. Python 3.10+

Check if Python is installed:

python --version

2. Install Ollama

Download and install Ollama from:
🔗 https://ollama.com/download

Verify the installation:

ollama --version

3. Download CodeLlama Model

Before running CodeRoot AI:

ollama pull codellama

📥 Installation

Clone the repository:

git clone https://github.com/Sudhi3276/code-explainer.git
cd code-explainer


Create a virtual environment:

python -m venv venv


Activate it:

.\venv\Scripts\activate       # Windows
source venv/bin/activate      # macOS/Linux


Install dependencies:

pip install -r requirements.txt

▶️ How to Run CodeRoot AI

Start the program:

python main.py


You will be prompted to paste your code snippet, and CodeRoot AI will generate a detailed explanation using CodeLlama.
