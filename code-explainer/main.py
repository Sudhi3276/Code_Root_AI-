import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import threading
from backend.explain import explain_code_with_ollama


def run_explanation():
    """Triggered when the 'Explain Code' button is clicked."""
    code = code_input.get("1.0", tk.END).strip()
    model = model_var.get()

    if not code:
        messagebox.showwarning("Input Required", "Please enter some code to explain.")
        return

    # Disable button & show loading message
    explain_button.config(state="disabled")
    output.delete("1.0", tk.END)
    output.insert(tk.END, "⏳ Generating explanation using LLM...")
    app.update()

    # Run in background thread (to avoid UI freezing)
    def background_task():
        explanation = explain_code_with_ollama(code, model)
        output.delete("1.0", tk.END)
        output.insert(tk.END, explanation)
        explain_button.config(state="normal")

    threading.Thread(target=background_task).start()


def save_output():
    """Save generated explanation to a text file."""
    text = output.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Nothing to Save", "No explanation generated yet.")
        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        messagebox.showinfo("Saved", f"Explanation saved to {filepath}")

# ---------------------------
# 🪟 GUI Layout Setup
# ---------------------------

app = tk.Tk()
app.title("🧠 Code Explainer using Local LLM (NLP Project)")
app.geometry("900x650")
app.config(bg="#f8f9fa")

# --- Title ---
tk.Label(
    app, text="Code Explainer - NLP powered by Local LLM",
    font=("Arial", 16, "bold"), bg="#f8f9fa", fg="#212529"
).pack(pady=10)

# --- Model Selection ---
frame_top = tk.Frame(app, bg="#f8f9fa")
frame_top.pack(pady=5)
tk.Label(frame_top, text="Model:", font=("Arial", 12, "bold"), bg="#f8f9fa").pack(side="left", padx=5)
model_var = tk.StringVar(value="codellama")
tk.OptionMenu(frame_top, model_var, "codellama").pack(side="left")

# --- Code Input ---
tk.Label(app, text="Paste Your Code Below:", font=("Arial", 12, "bold"), bg="#f8f9fa").pack(anchor="w", padx=10, pady=5)
code_input = scrolledtext.ScrolledText(app, height=14, font=("Courier", 11))
code_input.pack(fill="both", expand=True, padx=10, pady=5)

# --- Buttons ---
frame_buttons = tk.Frame(app, bg="#f8f9fa")
frame_buttons.pack(pady=8)
explain_button = tk.Button(frame_buttons, text="🔍 Explain Code", font=("Arial", 12, "bold"), command=run_explanation, bg="#007bff", fg="white")
explain_button.pack(side="left", padx=10)
tk.Button(frame_buttons, text="💾 Save Explanation", font=("Arial", 12, "bold"), command=save_output, bg="#198754", fg="white").pack(side="left", padx=10)

# --- Output ---
tk.Label(app, text="Explanation:", font=("Arial", 12, "bold"), bg="#f8f9fa").pack(anchor="w", padx=10, pady=5)
output = scrolledtext.ScrolledText(app, height=14, font=("Arial", 11))
output.pack(fill="both", expand=True, padx=10, pady=5)

# --- Footer ---
tk.Label(app, text="Developed as an NLP Project using Ollama + LLMs", bg="#f8f9fa", fg="#6c757d", font=("Arial", 9)).pack(side="bottom", pady=5)

# Run App
app.mainloop()