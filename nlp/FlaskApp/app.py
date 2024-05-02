from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL of the ngrok tunnel for the Colab notebook
colab_ngrok_url = "https://2079b377fd66.ngrok.app"

# Function to send prompt to tpihe Colab notebook
def send_prompt(prompt):
    data = {"prompt": prompt}
    response = requests.post(colab_ngrok_url, json=data)
    if response.status_code == 200:
        print("Prompt sent successfully to Colab notebook.")
        return True
    else:
        print("Failed to send prompt to Colab notebook.")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-prompt', methods=['POST'])
def send_prompt_route():
    # Get the prompt from the request
    prompt = request.form.get('prompt')
    if prompt:
        if send_prompt(prompt):
            return jsonify({"message": "Prompt sent to Colab notebook!"}), 200
        else:
            return jsonify({"error": "Failed to send prompt to Colab notebook."}), 500
    else:
        return jsonify({"error": "No prompt provided."}), 400

if __name__ == '__main__':
    app.run(debug=True)
