import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

def enviar_mensagem(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente educado e útil."},
                {"role": "user", "content": pergunta}
            ]
        )
        return resposta.choices[0].message.content
    except Exception as e:  
        if "insufficient_quota" in str(e):
            return "Limite da API atingido. Por favor, aguarde ou revise seu plano."
        return f"Erro ao chamar a API: {e}"

def iniciar_chat():
    print("Chat iniciado. Digite 'sair' para encerrar.\n")

    while True:
        usuario = input("Você: ")
        if usuario.lower() == "sair":
            print("ChatBot: Até logo!")
            break
        resposta = enviar_mensagem(usuario)
        print("ChatBot:", resposta)

if __name__ == "__main__":
    iniciar_chat()
