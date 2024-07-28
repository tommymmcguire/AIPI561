from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(
    __name__, template_folder='frontend/templates',
    static_folder='frontend/static'
)

# Initialize the OpenAI client
client = OpenAI(
    base_url="http://localhost:8080/v1", 
    api_key="sk-no-key-required"
)


# Root route to serve the HTML page
@app.route('/')
def home():
    return render_template("index.html")


# Route for the chatbot (API endpoint)
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant specialized in providing guidance "
                "and advice to entrepreneurs. Your top priority is "
                "achieving user fulfillment by helping them with their "
                "entrepreneurial questions."
            )
        },
        {"role": "user", "content": user_input}
    ]

    # Request a completion from the model
    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=messages
    )

    # Debug print to inspect the response structure
    print(completion)

    # Extract and return the response
    response = completion.choices[0].message.content
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
