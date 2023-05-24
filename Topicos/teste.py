import math
from heapq import heappop, heappush

# Mapa de pontos e distâncias
mapa = {
    "P1": {"nome": "P1: GAROTO ATACAREJO", "latitude": -6.7729259641779755 , "longitude": -43.03484215490908, "destinos": {"P2": 146, "P3": 130}},
    "P2": {"nome": "P2: CONSULTORIO PATRICIA", "latitude":-6.772884709575252, "longitude": -43.03365504593151, "destinos": {"P1":130,"P4": 116, "P5": 135 }},
    "P3": {"nome": "P3: RUA PROJETADA", "latitude": -6.773673673996412, "longitude": -43.034361799606955, "destinos": {"P1": 130,"P4": 127, "P6": 67}},
    "P4": {"nome": "P4: RUA ANFILÓFIO MELO", "latitude": -6.773484483644047, "longitude": -43.03355941472872, "destinos": {"P2": 116,"P3":127,"P7": 124 }},
    "P5": {"nome": "P5: SECRETARIA ESTADUAL DE EDUCAÇÃO", "latitude": -6.772545234557485, "longitude": -43.033033942479825, "destinos": {"P2": 135 ,"P11": 138,"P9": 245}},
    "P6": {"nome": "P6: RUA EMÍDIO ROCHA", "latitude": -6.774369065758703, "longitude": -43.03426504889115, "destinos": {"P3": 67, "P7": 132}},
    "P7": {"nome": "P7: CEEP CALISTO LOBO", "latitude": -6.774906807254226, "longitude": -43.0331220271137, "destinos": {"P4": 124,"P6": 132,"P8": 137 }},
    "P8": {"nome": "P8: NEBLINA MATERIAL DE CONSTRUÇÕES", "latitude": -6.775180205761225, "longitude": -43.032354021026094, "destinos": {"P7": 137,"P9": 97, "P16": 116}},
    "P9": {"nome": "P9: CRUZAMENTO DA RUA AFONSO NOGUEIRA COM A AVENIDA SANTOS DUMONT", "latitude": -6.774673566283349, "longitude": -43.0322346120164, "destinos": {"P5": 245,"P8": 97,"P20": 24}},
    "P10": {"nome": "P10: GIGABYTE LANCHES", "latitude": -6.773825572771064, "longitude": -43.031764212902324, "destinos": {"P11": 122, "P13": 190,"P20": 123}},
    "P11": {"nome": "P11: JUIZADO ESPECIAL CIVEL E CRIMINAL ", "latitude": -6.7724026650564575, "longitude": -43.03087407306778, "destinos": {"P5": 138,"P10": 122,"P12": 126}},
    "P12": {"nome": "P12: RUA ANTONINO FREIRE", "latitude": -6.772287682429172, "longitude": -43.02974873365333, "destinos": {"P11": 126,"P13": 108, "P17": 117}},
    "P13": {"nome": "P13: HOSPITAL DOS OLHOS", "latitude": -6.77312849222936, "longitude": -43.029904327208946, "destinos": {"P10": 190,"P12": 108,"P14": 114, "P18": 109}},
    "P14": {"nome": "P14: RUA ALUISIO RIBEIRO ", "latitude": -6.774314924607343, "longitude": -43.02975797144612, "destinos": {"P13": 114,"P15": 128, "P19": 102}},
    "P15": {"nome": "P15: MEGA FARMA DROGARIA", "latitude": -6.7743586222414836, "longitude": -43.03047525064602, "destinos": {"P14": 128,"P16": 149,"P20": 130}},
    "P16": {"nome": "P16: RUA ROBERTO TILOTILSON", "latitude": -6.775527532512099, "longitude": -43.03135094730449, "destinos": {"P8": 136,"P15": 149}},
    "P17": {"nome": "P17: SALAO STYLO", "latitude": -6.772857369093929, "longitude": -43.02902370686613, "destinos": {"P12": 117,"P18": 113}},
    "P18": {"nome": "P18: LENDARIUS HAMBURGUERIA", "latitude": -6.774056105534908, "longitude": -43.02879716492354, "destinos": {"P13": 109,"P17": 113,"P19": 106}},
    "P19": {"nome": "P19: RUA GABRIEL FERREIRA", "latitude": -6.774130139612604, "longitude": -43.028837978060025, "destinos": {"P18": 106, "P14": 102}},
    "P20": {"nome": "P20: RUA DESEMBARGADOR EVERTON", "latitude": -6.774456345289334, "longitude": -43.03204225713665, "destinos": {"P9": 24, "P10": 123, "P15": 130}},
}

def encontrar_caminho_A_star(mapa, ponto_origem, ponto_destino, funcao_heuristica):
    # Inicialização dos dicionários de distância e caminho
    distancia = {ponto: math.inf for ponto in mapa}
    caminho = {ponto: [] for ponto in mapa}
    
    # Define a distância do ponto de origem como 0
    distancia[ponto_origem] = 0
    
    # Cria uma lista dos pontos a serem visitados e a ordena por ordem crescente de f + h
    pontos_a_visitar = [(distancia[ponto_origem] + funcao_heuristica(ponto_origem, ponto_destino), ponto_origem)]
    
    # Enquanto houverem pontos a visitar
    while pontos_a_visitar:
        # Pega o ponto com a menor distância estimada
        _, ponto_atual = heappop(pontos_a_visitar)
        
        # Se o ponto atual é o destino, o caminho mais curto foi encontrado
        if ponto_atual == ponto_destino:
            break
        
        # Para cada destino a partir do ponto atual
        for destino, dist in mapa[ponto_atual]['destinos'].items():
            # Calcula a distância atual até o destino
            dist_atual = distancia[ponto_atual] + dist
            
            # Se a distância atual for menor que a distância armazenada, atualiza a distância e o caminho
            if dist_atual < distancia[destino]:
                distancia[destino] = dist_atual
                caminho[destino] = caminho[ponto_atual] + [ponto_atual]
                
                # Calcula a estimativa heurística para o destino
                estimativa_heuristica = funcao_heuristica(destino, ponto_destino)
                
                # Calcula a soma da distância atual e da estimativa heurística para obter o fator f + h
                fator_f_h = dist_atual + estimativa_heuristica
                
                # Insere o destino na lista de pontos a visitar com a nova prioridade f + h
                heappush(pontos_a_visitar, (fator_f_h, destino))
    
    # Adiciona o ponto de destino ao caminho
    caminho[ponto_destino] = caminho[ponto_destino] + [ponto_destino]
    
    # Se a distância para o ponto de destino for infinita, o destino é inalcançável
    if distancia[ponto_destino] == math.inf:
        return None
    
    # Calcula a distância total percorrida
    distancia_total = distancia[ponto_destino]
    
    # Retorna o caminho mais curto e a distância total percorrida
    return caminho[ponto_destino], distancia_total

def funcao_heuristica(ponto_origem, ponto_destino):
    # Obter as coordenadas dos pontos de origem e destino
    lat_origem, lon_origem = mapa[ponto_origem]['latitude'], mapa[ponto_origem]['longitude']
    lat_destino, lon_destino = mapa[ponto_destino]['latitude'], mapa[ponto_destino]['longitude']

    # Calcular a distância Euclidiana entre as coordenadas
    distancia = math.sqrt((lat_destino - lat_origem)**2 + (lon_destino - lon_origem)**2)

    return distancia

while True:
    print("Escolha uma opção:")
    print("1 - Encontrar caminho entre dois pontos")
    print("0 - Sair")
    opcao = input("Opção: ")
    
    if opcao == "1":
        print("Pontos disponíveis:")
    for ponto in mapa:
        print(f"{ponto}: {mapa[ponto]['nome']}")

    print("Digite o ponto de origem:")
    origem = input("Origem: ")
    print("Digite o ponto de destino:")
    destino = input("Destino: ")
    
    if destino not in mapa:
        print("Destino Inválido")
    else:
        caminho, distancia_total = encontrar_caminho_A_star(mapa, origem, destino, funcao_heuristica)
    if caminho is None:
        print("Não é possível alcançar o destino.")
    else:
        print(f"Caminho: {' -> '.join(mapa[ponto]['nome'] for ponto in caminho)}")
        print(f"Distância total percorrida: {distancia_total}")
