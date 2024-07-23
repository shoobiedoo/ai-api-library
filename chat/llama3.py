import os
from together import Together

class Llama3Client:
    def __init__(self, api_key):
        self.client = Together(api_key=api_key)

    def get_response(self, prompt, stream=False):
        if stream:
            # Streaming mode
            stream_response = self.client.chat.completions.create(
                model="meta-llama/Llama-3-70b-chat-hf",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )

            # Print streaming response
            for chunk in stream_response:
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
        else:
            # Non-streaming mode
            response = self.client.chat.completions.create(
                model="meta-llama/Llama-3-70b-chat-hf",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            # Return non-streaming response content
            return response.choices[0].message['content']

def llama3(prompt, api_key, stream=False):
    client = Llama3Client(api_key)
    return client.get_response(prompt, stream)
