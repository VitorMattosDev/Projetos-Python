alunos = {
    "aluno1": {
        "nome": "Joao",
        "nota": 9.8
    },
    "aluno2": {
        "nome": "Maria",
        "nota": 9.9
    },
    "aluno3": {
        "nome": "Pedro",
        "nota": 8.5
    }
}

maior_nota = 0
aluno_maior_nota = ""

for aluno, dados in alunos.items():
    if dados["nota"] > maior_nota:
        maior_nota = dados["nota"]
        aluno_maior_nota = dados["nome"]

print(f"Aluno com maior nota: {aluno_maior_nota} - Nota: {maior_nota}")

