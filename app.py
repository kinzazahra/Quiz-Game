from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load your Gemini API Key securely
genai.configure(api_key="AIzaSyDiOaJ2raDYnencw3qd_zncgXZvI6Qgcdc")

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-questions", methods=["POST"])
def generate_questions():
    try:
        prompt = """
        Generate 5 multiple-choice questions (with 4 options each, and 1 correct answer index) 
        based on random historical eras from Prehistoric to Future Tech. Return in JSON format like:
        [
          {
            "question": "What is ...?",
            "options": ["A", "B", "C", "D"],
            "correct": 1
          },
          ...
        ]
        """
        response = model.generate_content(prompt)
        text = response.text

        # Convert AI text to JSON
        import json, re
        match = re.search(r'\[\s*{.*}\s*\]', text, re.DOTALL)
        questions = json.loads(match.group()) if match else []

        return jsonify(questions)
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": "Failed to fetch questions."}), 500

if __name__ == "__main__":
    app.run(debug=True)
