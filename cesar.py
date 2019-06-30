class Criptografia:
    def __init__(self, texto, chave, alfa):
        self.texto = texto
        self.chave = chave
        self.alfa = alfa
    
    def decifrar(self):
        texto_cifrado = ''
        for letra in self.texto:
            if letra in self.alfa:
                num = self.alfa.find(letra)
                num -= self.chave
                if num >= len(self.alfa):
                    num -= len(self.alfa)
                elif num < 0:
                    num += len(self.alfa)
                texto_cifrado += self.alfa[num]
            else:
                texto_cifrado += letra
        return texto_cifrado