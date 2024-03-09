import openai 
from dotenv import load_dotenv
import os 

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def traducao(texto, idioma_origem, idioma_destino):
    response = openai.Completion.create(
        engine= "gpt-3.5-turbo-instruct",
        prompt=f"Traduza o seguinte texto do idioma {idioma_origem} para o idioma {idioma_destino}: {texto}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )

    return response['choices'][0]['text'].strip()

while True:
    print("\n____________________________\n")
    texto = input("Digite o texto que deseja traduzir (ou 'parar' para sair): ")
    if texto.lower() == "parar":
        break
    idioma_destino = input("Para qual idioma? ")
    if idioma_destino.lower() == "parar":
        break
    print(traducao(texto, "portugues", idioma_destino ))

