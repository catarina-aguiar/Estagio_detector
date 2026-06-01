from flask import Flask, request, jsonify, render_template
from groq import Groq
from prompt import SYSTEM_PROMPT
import os

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Nenhuma questão fornecida."}), 400

    try:
        response = client.chat.completions.create(
            model="model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Analisa esta questão: {question}"}
            ],
            temperature=0.2,  # Low temperature for consistent, analytical responses
        )

        result = response.choices[0].message.content
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
