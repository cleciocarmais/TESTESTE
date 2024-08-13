Dados = []


def armazenaInfor(infor,status):
    global Dados
    Dados.append({
           'nome': infor['nome'],
            'cpf_cpjn' : infor['cpfs_cnpj'].replace(" ",""),
            'valor': infor['valor'],
            'Valor total nf': infor['Valor total nf'],
            'Empresa': infor['Empresa'],
            'datas': infor['datas'],
            'Status' : status
})
    
def buscarInfor():

    global Dados
    return Dados
def resertaInfor():
    global Dados
    Dados = []

