from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import torch
import re

app = Flask(__name__)

# ⬇️ *** MODIFICATION: Specify allowed origins *** ⬇️
CORS(app, origins=[
    "http://localhost:3000",
    "https://aura-sync-868565811629.us-central1.run.app"
]) 
# --------------------------------------------------------

# --- GPU Check ---
print("🖥 CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("🧠 Using device:", torch.cuda.get_device_name(0))
else:
    print("⚠ No GPU detected. Falling back to CPU.")

# --- Initialize the generator ---
print("🔄 Loading TinyLlama model... please wait.")
generator = pipeline(
    'text-generation',
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.float16,  # Use float16 for better compatibility
    device=0,  # Force GPU usage
    model_kwargs={"low_cpu_mem_usage": True}
)
print("✅ Model loaded successfully!")

# --- Arduino Code Generator ---
def generate_arduino_code(user_prompt: str) -> str:
    full_prompt = f"""<|system|>
You are an expert Arduino programmer. Write a simple, complete, and correct Arduino sketch based on the user's request. Only return the C++ code (no explanations).</s>
<|user|>
{user_prompt}</s>
<|assistant|>
"""

    sequences = generator(
        full_prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )

    generated_text = sequences[0]['generated_text']
    assistant_response = generated_text.split('<|assistant|>')[1].strip()

    # Extract only code from markdown if present
    code_match = re.search(r"c\+\+(.*?)", assistant_response, re.DOTALL)
    if code_match:
        return code_match.group(1).strip()
    else:
        return assistant_response.strip()

# --- Endpoint ---
@app.route("/generate", methods=["POST"])
def generate_code():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "").strip()

        if not user_prompt:
            return jsonify({"error": "Prompt cannot be empty"}), 400

        print(f"🧠 Generating code for prompt: {user_prompt}")
        code = generate_arduino_code(user_prompt)
        print("✅ Code generated successfully.")
        return jsonify({"code": code})
    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 500

# --- Run Server ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)