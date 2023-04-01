from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Khởi tạo API key cho OpenAI
API_KEY = os.environ.get('API_KEY')

# Tạo function để thực hiện inference trên GPT model
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=60
    )
    message = completions.choices[0].text
    return message.strip()

# Xử lý request POST đến server
@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    message = generate_text(prompt)
    response = {"message": message}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
