import json




caminho = 'token.json'
informacoes = ''


def capturar_token():
    global caminho
    global informacoes
    with open(caminho, 'r') as file:
        informacoes = json.load(file)
        file.close()
        return  informacoes
    
    
def alterar_token(valor,numero_lanc):
    global informacoes
    global caminho
    informacoes['valor'] = valor
    informacoes['numero_lancamento'] = numero_lanc
    with open('token.json', 'w') as file:
        json.dump(informacoes, file, ensure_ascii=False, indent=4)
def altera_chave_status(chave):
    global informacoes
    global caminho
    informacoes['chave'] = chave
    with open('token.json', 'w') as file:
        json.dump(informacoes, file, ensure_ascii=False, indent=4)

        
    


# numero_lancamento = capturar_token.numero_lancamento
# print(numero_lancamento)

# alterar_token("457",'857458')

# print(capturar_token()['numero_lancamento'])