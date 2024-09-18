'''
Numa determinada escolinha o número de alunos foi reduzido de um ano para o outro 
e uma lista foi entregue pela secretaria dos alunos rematrículados do ano 2023 
(Ana, Leonardo, Rubem, Agenor, Giovanna, Gilberto). Porém não se sabe quais foram os alunos que permaneceram na escolinha para 
o próximo ano e quais foram as novas matriculas conforme nova listagem (Ana, Tuila, Rubem, Agenor, Julia)
'''
alunos_2023 = {"Ana", "Leonardo", "Rubem", "Agenor", "Giovanna", "Gilberto"}
nova_lista = {"Ana", "Tuila", "Rubem", "Agenor", "Julia"}

#Alunos que permaneceram na escolinha

print("\nAlunos rematriculados: ")
print(alunos_2023 & nova_lista)

#Alunos novos
print("\nNovos alunos matriculados: ")
print(nova_lista - alunos_2023)