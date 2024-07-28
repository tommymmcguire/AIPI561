from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Initialize the OpenAI client
client = OpenAI(
    base_url="http://localhost:8080/v1",  # Ensure this matches the port where your API server is running
    api_key="sk-no-key-required"
)

# Route for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    messages = [
        {"role": "system", "content": "You are an AI assistant specialized in providing guidance and advice to entrepreneurs. Your top priority is achieving user fulfillment by helping them with their entrepreneurial questions."},
        {"role": "user", "content": user_input}
    ]

    # Request a completion from the model
    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=messages
    )

    # Extract and return the response
    response = completion.choices[0].message
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
