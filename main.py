import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input>")
        sys.exit(1)

    input_text = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=input_text)]),
    ]

    print("Hello from ai-agent!")
    answer = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(answer.text)
    print(f"Prompt tokens: {answer.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {answer.usage_metadata.candidates_token_count}")
if __name__ == "__main__":
    main()
