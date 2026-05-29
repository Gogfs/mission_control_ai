import random

dados_missao = [
    [21.5, 95, 100, 98, 92],  # Ciclo 1: Lançamento perfeito. Tudo em níveis normais.
    [22.8, 88, 94, 95, 87],   # Ciclo 2: Órbita estável. Consumo nominal de recursos.
    [31.2, 75, 88, 92, 80],   # Ciclo 3: Aquecimento leve na fuselagem externa (Atenção).
    [35.8, 62, 81, 89, 73],   # Ciclo 4: Temperatura atinge nível Crítico! Sistemas em Atenção.
    [26.4, 22, 74, 84, 65],   # Ciclo 5: Radiação solar afeta antenas. Comunicação Crítica!
    [18.9, 55, 38, 81, 52],   # Ciclo 6: Correção de órbita. Sistema de energia entra em Atenção.
    [14.2, 68, 25, 78, 28],   # Ciclo 7: Entrada na sombra do planeta. Temp, Energia e Estabilidade Críticas!
    [17.1, 72, 45, 65, 48],   # Ciclo 8: Reativação dos geradores. Oxigênio cai para nível Crítico.
    [20.5, 82, 68, 85, 74],   # Ciclo 9: Protocolos de emergência aplicados com sucesso. Recuperação.
    [22.1, 90, 85, 94, 88]    # Ciclo 10: Missão totalmente estabilizada e segura.
]

areas_monitoradas = [
"Temperatura interna",
"Comunicação com a base",
"Sistema de energia",
"Suporte de oxigênio",
"Estabilidade operacional"
]
pontuacao_riscos = []

def analisar_temperatura(ciclo):
    if dados_missao[ciclo][0] < 16:
        return "CRÍTICO"

    elif dados_missao[ciclo][0] >= 16 and dados_missao[ciclo][0] < 20:
        return "ATENÇÃO"

    elif dados_missao[ciclo][0] >= 20 and dados_missao[ciclo][0] <= 30:
        return "NORMAL"

    elif dados_missao[ciclo][0] > 30 and dados_missao[ciclo][0] <= 35:
        return "ATENÇÃO"

    elif dados_missao[ciclo][0] > 35:
        return "CRÍTICO"

def analisar_comunicacao(ciclo):
    if dados_missao[ciclo][1] < 30:
        return "CRÍTICO"
    elif dados_missao[ciclo][1] >= 30 and dados_missao[ciclo][1] <= 70:
        return "ATENÇÃO"
    elif dados_missao[ciclo][1] > 70:
        return "NORMAL"

def analisar_energia(ciclo):
    if dados_missao[ciclo][2] < 30:
        return "CRÍTICO"
    elif dados_missao[ciclo][2] >= 30 and dados_missao[ciclo][2] <= 40:
        return "ATENÇÃO"
    elif dados_missao[ciclo][2] > 40:
        return "NORMAL"

def analisar_oxigenio(ciclo):
    if dados_missao[ciclo][3] < 70:
        return "CRÍTICO"
    elif dados_missao[ciclo][3] >= 70 and dados_missao[ciclo][3] <= 90:
        return "ATENÇÃO"
    elif dados_missao[ciclo][3] > 90:
        return "NORMAL"

def analisar_estabilidade(ciclo):
    if dados_missao[ciclo][4] < 30:
        return "CRÍTICO"
    elif dados_missao[ciclo][4] >= 30 and dados_missao[ciclo][4] <= 70:
        return "ATENÇÃO"
    elif dados_missao[ciclo][4] > 70:
        return "NORMAL"

def avaliar_ciclo(ciclo):
    return [analisar_temperatura(ciclo),
         analisar_comunicacao(ciclo),
         analisar_energia(ciclo),
         analisar_oxigenio(ciclo),
         analisar_estabilidade(ciclo)
         ]

def exibir_ciclo(ciclo):
    print(f"CICLO {ciclo + 1}")
    print("-" * 60)
    status_ciclo = avaliar_ciclo(ciclo)

    for i in range(len(areas_monitoradas)):
        if i == 0:
            print(f"{areas_monitoradas[i]}: {dados_missao[ciclo][i]}ºC | {status_ciclo[i]}")
        else:
            print(f"{areas_monitoradas[i]}: {dados_missao[ciclo][i]}% | {status_ciclo[i]}")

    print("")
    calcular_pontuacao(ciclo)

    recomendacao = gerar_recomendacao(status_ciclo)
    print(f"Recomendação: {recomendacao}")
    print("")

def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        print("Classificação do ciclo: MISSÃO ESTAVEL")
    elif pontuacao >= 3 and pontuacao <= 5:
        print("Classificação do ciclo: MISSÃO EM ATENÇÃO")
    else:
        print("Classificação do ciclo: MISSÃO CRÍTICA")

def calcular_pontuacao(ciclo):
    status_ciclo = avaliar_ciclo(ciclo)
    pontuacao_risco_ciclo = []

    for i in range(len(status_ciclo)):
        if status_ciclo[i] == "CRÍTICO":
            pontuacao_risco_ciclo.append(2)
        elif status_ciclo[i] == "ATENÇÃO":
            pontuacao_risco_ciclo.append(1)
        else:
            pontuacao_risco_ciclo.append(0)

    pontuacao_riscos.append(pontuacao_risco_ciclo)
    pontuaca_total_ciclo = sum(pontuacao_risco_ciclo)

    print(f"Pontuação de risco do ciclo: {pontuaca_total_ciclo}")
    classificar_ciclo(pontuaca_total_ciclo)


def gerar_recomendacao(status_ciclo):
    # Dicionário mapeando o índice da área para sua respectiva recomendação crítica
    recomendacoes_criticas = {
        0: "Verificar controle térmico da missão.",
        1: "Tentar restabelecer contato com a base.",
        2: "Ativar modo de economia de energia.",
        3: "Acionar protocolo de suporte à vida.",
        4: "Reduzir operações não essenciais."
    }

    alertas_criticos = []
    alertas_atencao = []

    # Identifica o que está em CRÍTICO ou ATENÇÃO no ciclo atual
    for i in range(len(status_ciclo)):
        if status_ciclo[i] == "CRÍTICO":
            alertas_criticos.append(recomendacoes_criticas[i])
        elif status_ciclo[i] == "ATENÇÃO":
            alertas_atencao.append(i)  # Guarda o índice da área em atenção

    # REGRA DE DECISÃO (Prioridades):
    # 1. Se houver qualquer sistema em CRÍTICO, prioriza os protocolos de emergência
    if alertas_criticos:
        # Se houver mais de um crítico (como no Ciclo 5 do exemplo), combina as ações
        if len(alertas_criticos) >= 3:
            return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
        return " ".join(alertas_criticos)

    # 2. Se não houver crítico, mas houver sistemas em ATENÇÃO
    elif alertas_atencao:
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    # 3. Se tudo estiver NORMAL
    else:
        return "Manter operação normal e continuar monitoramento."


def calcular_medias():
    medias = []
    num_areas = len(dados_missao[0])  # Representa as 5 colunas (áreas monitoradas)
    total_ciclos = len(dados_missao)  # Representa as linhas (quantidade de ciclos)

    for coluna in range(num_areas):
        soma = 0
        for linha in range(total_ciclos):
            soma += dados_missao[linha][coluna]

        # Calcula a média da coluna e arredonda para 2 casas decimais
        medias.append(round(soma / total_ciclos, 2))

    return medias

def gerar_relatorio(ciclos):
    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)

    print("Missão: ARES I")
    print("Equipe: Equipe Argos")

    print(f"\nQuantidade de ciclos analisados: {ciclos} \n")

    medias = calcular_medias()

    print(f"Média de temperatura: {medias[0]}ºC")
    print(f"Média de comunicação: {medias[1]}%")
    print(f"Média de energia: {medias[2]}%")
    print(f"Média de oxigênio: {medias[3]}%")
    print(f"Média de estabilidade: {medias[4]}% \n")

    print(f"Ciclo mais crítico: {pontuacao_riscos.index(max(pontuacao_riscos, key=sum)) + 1}")
    print(f"Maior pontuação de riscos: {sum(max(pontuacao_riscos, key=sum))}")

    # Cálculo do risco da missão
    soma_total_risco = 0
    for i in pontuacao_riscos:
        soma_total_risco += sum(i)
    media_missao = round(soma_total_risco / ciclos, 2)
    print(f"Risco médio da missão: {media_missao}")

    # Encontrando a quantidade de ciclos críticos
    ciclos_criticos = 0
    for i in pontuacao_riscos:
        if sum(i) >= 6:
            ciclos_criticos += 1
    print(f"Quantidade de ciclos críticos: {ciclos_criticos} \n")

    # DEFININDO A TENDÊNCIA DA MISSÃO
    risco_primeiro_ciclo = sum(pontuacao_riscos[0])
    risco_ultimo_ciclo = sum(pontuacao_riscos[-1])
    print("Tendência da missão:")
    if risco_ultimo_ciclo > risco_primeiro_ciclo:
        print("A missão apresentou tendência de piora. \n")
    elif risco_ultimo_ciclo < risco_primeiro_ciclo:
        print("A missão apresentou tendência de melhora. \n")
    else:
        print("A missão permaneceu estável em relação ao início. \n")

    # Calculando a pontuação acumulada de cada área
    print("Pontuação acumulada por área:")
    pontuacao_por_area = [0, 0, 0, 0, 0]

    for coluna in range(len(areas_monitoradas)):
        for linha in range(ciclos):
            pontuacao_por_area[coluna] += pontuacao_riscos[linha][coluna]

        print(f"{areas_monitoradas[coluna]}: {pontuacao_por_area[coluna]} pontos")

    # Identifica o índice com a maior pontuação
    indice_pior_area = pontuacao_por_area.index(max(pontuacao_por_area))

    print("\nÁrea mais afetada:")
    print(f"{areas_monitoradas[indice_pior_area]} \n")

    # Exibe a classificação final da missão
    print("Classificação final da missão:")
    if media_missao <= 2:
        print("MISSÃO ESTAVEL")
    elif media_missao >= 3 and media_missao <= 5:
        print("MISSÃO EM ATENÇÃO")
    else:
        print("MISSÃO CRÍTICA")


ciclos = len(dados_missao)

print("="*60)
print("MISSION CONTROL AI")
print("="*60)

for i in range(ciclos):
    exibir_ciclo(i)

gerar_relatorio(ciclos)
