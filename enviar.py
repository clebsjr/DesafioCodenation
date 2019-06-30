import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=4685586b01f8464d470a7f742bd6c1925916256e"
answer = {'answer':open('answer.json','rb')}
enviar = requests.post(url, files=answer)
print(enviar.status_code)
print(enviar.json())