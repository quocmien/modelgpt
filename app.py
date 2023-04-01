from flask import Flask, request, jsonify
from dotenv import load_dotenv

import openai
import os
load_dotenv()  # Load các biến môi trường từ file .env


app = Flask(__name__)

# Khởi tạo API key cho OpenAI
API_KEY = os.getenv("API_KEY")  # Lấy giá trị của biến API_KEY trong file .env

# Tạo function để thực hiện inference trên GPT model
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=60
    )
    message = completions.choices[0].text
    return message.strip()

# Xử lý request POST đến server
@app.route("/chat", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    message = generate_text(prompt)
    response = {"message": message}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
