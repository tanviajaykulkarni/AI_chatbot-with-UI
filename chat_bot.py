from groq import Groq
from dotenv import load_dotenv
import os
# from flask import *
from flask import Flask, render_template, request, jsonify

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("API key not found.")
    exit(1)

chatbot = Groq(api_key=api_key)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("user_query", "").strip()

    if not user_query:
        return jsonify({"response": "please enter a query"})

    try:

        chat_completion = chatbot.chat.completions.create(
            messages=[{"role": "user", "content": user_query}],
            model="llama-3.3-70b-versatile",
        )

        response_text = chat_completion.choices[0].message.content

    except Exception as e:

        response_text = f"Error: {str(e)}"

    return jsonify({"response": response_text})


if __name__ == "__main__":
    app.run(debug=True)
