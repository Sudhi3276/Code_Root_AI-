<h1 align="center">🌱 CodeRoot AI — Local Code Explanation Engine</h1>
<p align="center">Powered by <b>Ollama + CodeLlama</b></p>
<p align="center"> CodeRoot AI is a privacy-focused, offline code explanation engine that uses <b>CodeLlama</b> through <b>Ollama</b> to interpret and explain code instantly.<br> It ensures complete data privacy by running fully on your local machine — no cloud, no external API, and no data sharing. </p>
<h2>🧩 Project Description</h2>

CodeRoot AI helps developers understand unfamiliar or complex code by generating clear, human-readable explanations directly from their local machine.
Using open-source LLM models, it provides:

Fast code interpretation

Secure offline processing

Simple CLI interaction

Extensible modular design

It is ideal for students, developers, educators, and researchers who want a reliable and private AI code assistant.

<h2>🚀 Features</h2>

🧠 AI-powered code understanding using CodeLlama

🔒 100% offline — code never leaves your device

⚡ Lightweight & fast execution

🖥️ Simple CLI interface for ease of use

📦 Modular and extensible Python architecture

🧩 Compatible with Windows, macOS, and Linux

<h2>🛠️ Requirements</h2>
1. Python 3.10+

Check Python version:

python --version

2. Install Ollama

Download Ollama:
🔗 https://ollama.com/download

Verify installation:

ollama --version

3. Download CodeLlama

Pull the model locally:

ollama pull codellama

<h2>📥 Installation</h2>

Clone the repository:

git clone https://github.com/Sudhi3276/code-explainer.git
cd code-explainer


Create a virtual environment:

python -m venv venv


Activate environment:

.\venv\Scripts\activate       # Windows
source venv/bin/activate      # macOS/Linux


Install dependencies:

pip install -r requirements.txt

<h2>▶️ How to Run CodeRoot AI</h2>

Run the main script:

python main.py


Paste your code snippet, and CodeRoot AI will generate a clean, structured explanation using CodeLlama.
