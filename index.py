import random
import webbrowser

tentativas = 5
pontos = 0
sorteio = random.randint(1, 10)
chrome = webbrowser.get('chrome')

for tentativa in range(tentativas):
    igual = int(input('Digite o seu palpite: '))
    
    if igual == sorteio:
        pontos = 100
        print(f'Você acertou! Sua pontuação é de 100 pontos.')
        chrome.open('https://www.youtube.com/watch?v=PEHMVJ3XpM0')    
        break
    else:
        print(f'Errou! O número era {sorteio}. Você tem {tentativas - tentativa - 1} tentativas restantes.')

print(f'Sua pontuação final é de {pontos} pontos.')
