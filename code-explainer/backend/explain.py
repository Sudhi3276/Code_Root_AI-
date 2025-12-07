import subprocess

def explain_code_with_ollama(code: str, model: str = "codellama") -> str:
    """
    This function performs an NLP-based task: converting source code into
    natural language explanations using a locally hosted Large Language Model (LLM).
    The LLM (via Ollama) interprets the semantics of the code and generates
    a descriptive explanation.

    Args:
        code (str): The source code snippet to explain.
        model (str): The local LLM model to use (default: 'codellama').

    Returns:
        str: The model's generated explanation or an error message.
    """
    prompt = f"Explain this code in detail and in simple terms:\n{code}"
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return f"Ollama error:\n{result.stderr.strip()}"
        return result.stdout.strip()
    except FileNotFoundError:
        return "⚠️ Error: 'ollama' not found. Please ensure it is installed and added to your system PATH."
