from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    base_url="http://localhost:8080/v1",  # Ensure this matches the port where your API server is running
    api_key="sk-no-key-required"
)

# Define the messages for the conversation
messages = [
    {"role": "system", "content": "You are an AI assistant specialized in providing guidance and advice to entrepreneurs. Your top priority is achieving user fulfillment by helping them with their entrepreneurial questions."},
    {"role": "user", "content": "What are some effective marketing strategies for a new startup?"}
]

# Request a completion from the model
completion = client.chat.completions.create(
    model="LLaMA_CPP",
    messages=messages
)

# Print the response
print(completion.choices[0].message)
