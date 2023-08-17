import vercel_ai
from flask import Flask,request,jsonify

app=Flask(__name__)
client = vercel_ai.Client()


@app.route('/chat',methods=['POST'])
def chat():
    if request.method == "POST":

        data=request.json
        print(data)
        response = ""

        for chunk in client.chat("openai:gpt-3.5-turbo", data["messages"], params=data["params"]):

            response=response+chunk
            print(response)

        return jsonify(response)

@app.route('/generate',methods=['POST'])
def generate():
    if request.method == "POST":

        data=request.json
        print(data)
        response = ""

        for chunk in client.generate("openai:gpt-3.5-turbo", data["prompt"], params=data["params"]):

            response=response+chunk
            print(response)

        return jsonify(response)

@app.route('/List_models',methods=['GET'])
def models():
    if request.method == "GET":
        return jsonify(client.models)

@app.route('/')
def home():
    return 'Hello, World!'

