# The data types

name = "Milan"      # String - text
temperature = 0.7   # Float - AI model setting
max_tokens = 1000   # Integer - another AI model setting
is_active = True     # Boolean - on/off state

# F-strings
print(f"Model temperature is set to {temperature}")
print(f"Max output tokens: {max_tokens}\n")

# Lsts = ordered collections of items. Will use this to store conversation history
# With AI models - this is literally how ChatGPT memory works.

documents = [
    "AI is transforming software development.",
    "Python is the language of AI.",
    "Full-stack developers like me who are in high demand."
]

# Loop through and process each one
for i, doc in enumerate(documents):
    print(f"Document {i+1}: {doc}")
    print(f" Word count: {len(doc.split())}\n")
    
# A dictionary = key-value pairs. Useful for storing structured data.
# This is exactly the structure OpenAI's API uses for messages

message = {
    "role": "user",
    "content": "What is retrieval augmented generation?"
}

print(message["role"] + ": ", end="")
print(message["content"] + "\n")

# List of dictionaries - this IS the ChatGPT conversation format
conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
        {"role": "assistant", "content": "Hi! How can I help you?"}
]

for message in conversation_history:
    print(f"[{message['role'].upper()}]: {message['content']}")
    

# Functions = reusable blocks of code that perform a specific task. We will use these to create prompts and process responses.
# We'll wrap every AI call in a function.

def process_document(text, source="unknown"):
    word_count = len(text.split())
    char_count = len(text)
    
    return{
        "text" : text,
        "source": source,
        "word_count": word_count,
        "char_count": char_count
    }

# Call the function and print the result
result = process_document("AI is changing everything.", source="article_1")
print(result)
print(f"Words: {result ['word_count']}")