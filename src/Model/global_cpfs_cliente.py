import logging
from src.Model.global_utilitarios import formatando_cpfs_cpns



def pegando_informacoes(df,i,lista_qtd_cliente,lista_cpfs_cpjns):
    lista_clinte = []
    inicio = (15 - int(lista_qtd_cliente)) + 1
    for j in range(inicio,16):
        nome = [str(x) for x in df[f'Nome do Cliente {j}']][i]
        valor = [str(x) for x in df[f'Valor {j}']][i]
         

        lista_clinte.append({
            "nome" : nome,
            'valor' : valor
        })
    nova_lista_cpfs_cnpj = lista_cpfs_cpjns.split("|")
    for posicao,cliente in enumerate(lista_clinte):
            cliente['cpfs_cnpj'] = formatando_cpfs_cpns(nova_lista_cpfs_cnpj[posicao])
            cliente['Valor total nf'] = df['Valor Total da Nota Fiscal'][i]
            cliente['Empresa'] = df['Empresa'][i]
            cliente['datas'] = df['Carimbo de data/hora'][i]
            cliente['tipo_bonificao'] = df['Tipo de Bonificação'][i]
    return lista_clinte