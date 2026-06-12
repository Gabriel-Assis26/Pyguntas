import requests, html, random
from deep_translator import GoogleTranslator

def buscar_perguntas():
    url = "https://opentdb.com/api.php?amount=2" 
    resposta = requests.get(url)
    return resposta.json()['results']

def traduz(texto):
    texto = html.unescape(texto)
    return GoogleTranslator(
            source='en',
            target='pt'
        ).translate(texto)

def embaralha_respostas(perg):
    listaPerguntas = []
    listaPerguntas.append((traduz(perg['correct_answer']),0))
    for i,text in enumerate(perg['incorrect_answers']):
        i+=1
        listaPerguntas.append((traduz(text),i))
    random.shuffle(listaPerguntas)
    return listaPerguntas

