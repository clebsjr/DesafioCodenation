import requests
import json
import hashlib
from cesar import Criptografia

#Requisição da API
link = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=4685586b01f8464d470a7f742bd6c1925916256e'
requisicao = requests.get(link)
modelo = json.loads(requisicao.text)

texto = modelo["cifrado"]
chave = modelo["numero_casas"]
alfa = "abcdefghijklmnopqrstuvwxyz"

cifra1 = Criptografia(texto, chave, alfa)

decifrado = cifra1.decifrar()

resumo = hashlib.sha1(decifrado.encode('utf-8'))
r = resumo.hexdigest()

dicionario = {
    "numero_casas":modelo["numero_casas"],
    "token":modelo["token"],
    "cifrado":modelo["cifrado"],
    "decifrado":decifrado,
    "resumo_criptografico":r,   
}

arquivo = open("answer.json", 'w')
arquivo.write(json.dumps(dicionario))

