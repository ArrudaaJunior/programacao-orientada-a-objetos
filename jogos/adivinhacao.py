import random as r

print("*********************************")
print("Bem Vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_aleatorio= r.randrange(0, 101)
numero_secreto = numero_aleatorio
dificuldade = int(input("\nEscolha a dificuldade:\n(1) Facil\n(2) Medio\n(3) Dificil\n"))

if(dificuldade == 1):
	total_tentativas = 20

elif(dificuldade == 2):
	total_tentativas = 10

elif(dificuldade == 3):
	total_tentativas = 5	


pontuacao = 100		

for rodada in range(1,total_tentativas+1):
	print("Rodada {} de {}".format(rodada,total_tentativas))
	chute_str = input("Digite o seu número: ")
	print("Você digitou: ",chute_str)
	chute = int(chute_str)

	if(chute <1 or chute > 100):
		print("Digite um numero de 1 a 100")
		continue

	acertou = numero_secreto == chute
	maior = chute > numero_secreto
	menor = chute < numero_secreto

	if (acertou):
		print("Você Acertou!")
		break
	else:
		if (maior):
			print("Você errou: O seu chute foi maior que o número secreto")
			pontuacao = pontuacao -abs(numero_secreto-chute)
		elif (menor):
			print("Você errou: O seu chute foi menor que o número secreto")
			pontuacao = pontuacao -abs(numero_secreto-chute)
print("Fim do jogo") 