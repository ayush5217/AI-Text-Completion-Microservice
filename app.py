from flask import Flask, render_template, request, jsonify
from ctransformers import AutoModelForCausalLM

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/v1/yourchosenmodel/completions',methods=["POST"])
def completions():
    data = request.get_json()
    input_text = data['text']
    llm = AutoModelForCausalLM.from_pretrained("model", model_file="mistral-7b-instruct-v0.1.Q2_K.gguf", model_type="mistral", gpu_layers=0)
    res = llm(input_text, temperature=1, max_new_tokens=5, stop='.')
    return jsonify({"completed_text": input_text + res})