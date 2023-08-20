import vercel_ai
from flask import Flask,request,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app,origins=["https://compare-frontend.vercel.app"])

client = vercel_ai.Client()


@app.route('/chat',methods=['POST'])
def chat():
    if request.method == "POST":

        data=request.json

        response = ""

        for chunk in client.chat(data["modelname"], data["messages"], params=data["params"]):

            response=response+chunk


        return jsonify(response)

@app.route('/generate',methods=['POST'])
def generate():
    if request.method == "POST":

        data=request.json

        response = ""

        for chunk in client.generate(data["modelname"], data["prompt"], params=data["params"]):

            response=response+chunk


        return jsonify(response)

@app.route('/List_models',methods=['GET'])
def models():
    if request.method == "GET":
        return jsonify(client.models)

@app.route('/')
def home():
    return 'Hello, World!'


if __name__ == '__main__':
   app.run(debug=True)
