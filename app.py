# app.py
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key="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") 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "write a haiku about ai"},
            {"role": "user", "content": question}
        ]
    )
    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
