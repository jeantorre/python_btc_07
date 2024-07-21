import csv

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    '''
    Função que lê um arquivo .csv e o transforma numa lista de dicionários
    '''
    lista = []
    with open(nome_arquivo_csv, mode = 'r', encoding = 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    
    return lista

def filtrar_produto_nao_entregue(lista: list[dict]) -> list[dict]:
    '''
    Função que filtra produtos entregues
    '''
    lista_produtos_entregues = []
    for produto in lista: 
        if produto.get('entregue') == 'True':
            lista_produtos_entregues.append(produto)
                
    return lista_produtos_entregues

def somar_valor_produto_entregue(lista: list[dict]) -> list[dict]:
    '''
    Função que soma os valores dos produtos que foram entregues
    '''
    valor_total: float = 0
    for produto in lista:
        valor_total += int(produto.get('price'))
                
    return valor_total