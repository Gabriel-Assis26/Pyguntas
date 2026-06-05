import requests

def buscar_perguntas():
    url = "https://opentdb.com/api.php?amount=10" 
    resposta = requests.get(url)
    return resposta.json()['results']