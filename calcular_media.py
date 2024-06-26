def solicitar_nota(numero):
while True:
try:
nota = float(input(f"Digite a nota {numero} (0 a 10): "))
if 0 <= nota <= 10:
return nota
else:
print("Nota inválida! A nota deve estar entre 0 e 10.")
except ValueError:
print("Entrada inválida! Por favor, digite um número.")

Solicita as 3 notas do aluno
nota1 = solicitar_nota(1)
nota2 = solicitar_nota(2)
nota3 = solicitar_nota(3)

Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

Verifica se o aluno passou ou ficou em recuperação
if media >= 7:
print(f"O aluno passou com média {media:.2f}")
else:
print(f"O aluno ficou em recuperação com média {media:.2f}")
