print("====================================")
print("      MEU PAINEL DE DADOS           ")
print("====================================")

# 1. Entrada de Dados
nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")
qtd = int(input("Quantas tarefas você vai cadastrar? "))

print("====================================")
print("      CADASTRO DE TAREFAS           ")
print("====================================")

# 2. Criação e preenchimento da lista
tarefas = []

for i in range(qtd):
    tarefa = input(f"Digite a tarefa {i+1}: ")
    tarefas.append(tarefa)

print("====================================")
print("      TAREFAS CADASTRADAS           ")
print("====================================")

# 3. Exibição das tarefas cadastradas
print("Tarefas cadastradas:")
for t in tarefas:
    print(f"- {t}")

print("\n")

# 4. Decisão final do programa
if len(tarefas) == 0:
    status_rotina = "Nenhuma tarefa cadastrada."
elif len(tarefas) <= 3:
    status_rotina = f"{nome} de {cidade}: rotina leve hoje!"
else:
    status_rotina = f"{nome} de {cidade}: rotina cheia! Organize prioridades."

print(status_rotina)
