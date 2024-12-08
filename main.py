import ollama
response = ollama.chat(model = 'llama3', messages = [
    {
        'role': 'user',
        'content': '''summarize text''',
    },
])
print(response['message']['content'])
