import random

# Função para iniciar o jogo + declaração de variáveis
def novo_jogo():
    escolha_usuario = []
    escolha_correta = 0

    # Embaralha as matérias para selecionar aleatoriamente
    materias = list(questoes.keys())
    random.shuffle(materias)

    for materia in materias:
        print("---------------------------------------------------------------------")
        print(f"Categoria: {materia}")

        # Seleciona a primeira pergunta da matéria
        questao, resposta_certa = random.choice(list(questoes[materia].items()))
        print(questao)
        
        # Exibe as opções correspondentes
        numero_questao = list(questoes[materia].keys()).index(questao)
        for opcao in opcoes[materias.index(materia)][numero_questao]:
            print(opcao)
        
        # Algoritmo para a escolha de respostas e ganho de pontos
        escolha = input("Resposta?: ")
        escolha = escolha.upper()
        escolha_usuario.append(escolha) 
        
        escolha_correta += resposta(questao, escolha, resposta_certa)

    pontos(escolha_correta)

# Algoritmo para averiguar a resposta certa e calcular o total de pontos
def resposta(questao, escolha, resposta_certa):
    if resposta_certa == escolha:
        print("CORRETO!")
        return 1
    else:
        print("Resposta Errada :(")
        return 0

# Algoritmo de resultado final com base nas escolhas do usuário
def pontos(escolha_correta):
    print("---------------------------------------------------------------------")
    print("Resultados")
    print("---------------------------------------------------------------------")
    
    score = int((escolha_correta / len(questoes)) * 100)
    print("Sua pontuação é de: " + str(score) + "%")

# Algoritmo para reiniciar o jogo
def jogar_dnv():
    response = input("Você deseja jogar de novo? (sim/nao): ")
    response = response.upper()
    return response == "SIM"

# Questões do jogo em seguida de sua resposta
questoes = {
    "Matemática": {
        "Qual é o resultado de 7 x 8?: ": "B",
        "Qual é a raiz quadrada de 81?: ": "C",
        "Qual é a fórmula da área de um círculo?: ": "A",
        "Qual é o valor de pi?: ": "B"
    },
    "Física": {
        "Qual é a fórmula da segunda lei de Newton?: ": "C",
        "Qual é a unidade de medida da resistência elétrica?: ": "C",
        "A luz é um exemplo de que tipo de onda?: ": "B",
        "Qual é a velocidade da luz no vácuo?: ": "A"
    },
    "Química": {
        "Qual é o símbolo químico do ouro?: ": "B",
        "Qual é o número atômico do oxigênio?: ": "B",
        "Qual é o gás mais abundante na atmosfera?: ": "B",
        "Qual é o nome da tabela que organiza os elementos químicos?: ": "A"
    },
    "Português": {
        "Qual é a classe gramatical da palavra 'feliz'?: ": "C",
        "Qual das frases está correta?: ": "B",
        "Qual é o sujeito da frase: 'Os meninos jogaram bola'?: ": "A",
        "Qual é o plural de 'cidadão'?: ": "B"
    },
    "Inglês": {
        "Qual é o plural de 'child'?: ": "B",
        "Qual é o verbo 'to be' no passado para 'I'?: ": "B",
        "Como se diz 'cão' em inglês?: ": "B",
        "Qual é o significado de 'beautiful'?: ": "B"
    }
}

# Opções de resposta correspondentes
opcoes = [
    [  # Matemática
        ["A. 54", "B. 56", "C. 58", "D. 60"],
        ["A. 7", "B. 8", "C. 9", "D. 10"],
        ["A. πr²", "B. 2πr", "C. πd", "D. 2r"],
        ["A. 3.12", "B. 3.14", "C. 3.16", "D. 3.18"]
    ],
    [  # Física
        ["A. F = m/a", "B. F = m*v", "C. F = m*a", "D. F = v/t"],
        ["A. Ampere", "B. Volt", "C. Ohm", "D. Watt"],
        ["A. Longitudinal", "B. Transversal", "C. Mecânica", "D. De choque"],
        ["A. 300.000 km/s", "B. 150.000 km/s", "C. 450.000 km/s", "D. 500.000 km/s"]
    ],
    [  # Química
        ["A. Ag", "B. Au", "C. Hg", "D. Pt"],
        ["A. 6", "B. 8", "C. 10", "D. 12"],
        ["A. Oxigênio", "B. Nitrogênio", "C. Hidrogênio", "D. Dióxido de carbono"],
        ["A. Tabela Periódica", "B. Tabela Linear", "C. Tabela Atômica", "D. Tabela Molecular"]
    ],
    [  # Português
        ["A. Verbo", "B. Substantivo", "C. Adjetivo", "D. Advérbio"],
        ["A. Nós vamos ir no cinema", "B. Nós iremos ao cinema", "C. Nós vamos para o cinema", "D. Nós foi no cinema"],
        ["A. Os meninos", "B. Jogaram", "C. Bola", "D. Nenhum"],
        ["A. Cidadões", "B. Cidadãos", "C. Cidadães", "D. Cidades"]
    ],
    [  # Inglês
        ["A. Childs", "B. Children", "C. Childes", "D. Childrens"],
        ["A. Am", "B. Was", "C. Were", "D. Been"],
        ["A. Cat", "B. Dog", "C. Mouse", "D. Horse"],
        ["A. Feio", "B. Bonito", "C. Grande", "D. Pequeno"]
    ]
]

# Iniciar o quiz
print("Bem-vindo ao Quiz de Conhecimentos Gerais!")
novo_jogo()

while jogar_dnv():
    novo_jogo()

print("Obrigado por jogar!")
