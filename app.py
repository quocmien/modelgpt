from flask import Flask, jsonify, request
import openai
import os

app = Flask(__name__)

# Khởi tạo OpenAI API

API_KEY = os.environ.get('API_KEY')


# Chọn model để sinh ra text response
model_engine = "davinci" # ví dụ

# Tạo route để nhận request từ client
@app.route('/generate', methods=['POST'])
def generate():
    # Lấy input text từ request của client dưới dạng JSON
    request.json = request.get_json()
    prompt = request.json['text']

    # Thực hiện sinh text response bằng OpenAI API
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()

    # Trả về response dưới dạng JSON cho client
    res = {'message': message}
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000,use_reloader=True)
