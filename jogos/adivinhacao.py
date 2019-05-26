print("*********************************")
print("Bem Vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3 

for rodada in range(1,total_tentativas+1):
print("Rodada {} de {}".format(rodada, total_tentativas))
chute_str = input("Digite o seu número: ")
print("Você digitou: ",chute_str)
chute = int(chute_str)

if(chute <1 or chute > 100):
continue

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
print("Você Acertou!")
break
else:
if (maior):
print("Chute maior que o numero_secreto")
elif (menor):
print("Chute menor")

print("Fim do jogo") 