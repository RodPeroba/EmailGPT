from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

def call_openai_api(messsage):
    response = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[
        {
        "role": "user",
        "content": messsage
        }
    ]
    )
    return response

def main():
    print("Processando arquivo...")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="<OPENROUTER_API_KEY>",
        )


if __name__=="__main__":
    main()
