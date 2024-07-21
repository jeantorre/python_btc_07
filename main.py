from etl import ler_csv, filtrar_produto_nao_entregue, somar_valor_produto_entregue

path_arquivo = 'vendas.csv'
lista_itens: list[dict] = ler_csv(path_arquivo)
lista_produtos_entregues: list[dict] = filtrar_produto_nao_entregue(lista_itens)
valor_venda: float = somar_valor_produto_entregue(lista_produtos_entregues)
print(valor_venda)