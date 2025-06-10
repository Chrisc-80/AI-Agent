import os
from google import genai
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get(curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }')
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    print("Prompt tokens:", response.usage_meatadata.prompt_token_count)
    print("Response tokens:", response.usage_meatdata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()