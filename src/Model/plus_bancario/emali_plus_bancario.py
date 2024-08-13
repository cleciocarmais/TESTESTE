
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from datetime import datetime
import pyautogui as p

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Model.global_utilitarios import escreva
from src.Model.global_calculo_imposto import glob_calculo_valor
    
chave_de_acesso_Email = open(r'C:\RPA\credenciais\credenciais_gmail.txt', 'r')
chaves = chave_de_acesso_Email.readlines()
chave_de_acesso_Email.close()


sender = chaves[0][:-1]
password = chaves[1]
data_atual = datetime.now().strftime('%d/%m/%Y')


def email_plus_bancario(informacoes):
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.ehlo()
    servidor.login(sender, password)

    receiver = ('morgana.sousa@carmais.com.br,contasareceber_veiculos@carmais.com.br,daniel@carmais.com.br,fcoventura@carmais.com.br,alan.estevao@carmais.com.br')
    # receiver = ("francisco.clecio@carmais.com.br")
    body = ""
    print("ENVIANDO EMAIL DE PLUS BANCARIO ")
    logging.info("ENVIANDO EMAIL DE PLUS BANCARIO ")
    mgs = MIMEMultipart('related')
    mgs['From'] = sender
    mgs['To'] = receiver
    mgs['Subject'] = f'RPA - LIQUIDAÇÃO NOSSAMOTO -  {data_atual} '

    mgsAlternativa = MIMEMultipart('alternative')
    mgs.attach(mgsAlternativa) 
    for dado in informacoes:
       
        if dado['Status'] == 'Titulo não Encontrado' or dado['Status'] == 'Cliente não Encontrado' or dado['Status'] == 'Valor Divergente no Dealer':
            nome =  f"❌ {dado['nome']}"

        else:
            nome =  f" ✅ {dado['nome']}"
        tipo = 'CPF' if len(dado['cpf_cpjn']) == 11 else 'CNPJ'
        infor = f"{dado['cpf_cpjn'][0:3]}.{dado['cpf_cpjn'][3:6]}.{dado['cpf_cpjn'][6:9]}-{dado['cpf_cpjn'][9:11]}" if tipo == "CPF" else  f"{dado['cpf_cpjn'][0:2]}.{dado['cpf_cpjn'][2:5]}.{dado['cpf_cpjn'][5:8]}/{dado['cpf_cpjn'][8:12]}-{dado['cpf_cpjn'][12:14]}"
        
        body = body + f'''<h3> {nome}</h3>
        <b> {tipo}:</b> {infor}<br>
        <b>Empresa do Financiamento:</b> {dado['Empresa']} <br>
        <b>Valor Total da Notal Fiscal:</b> R$ {glob_calculo_valor(dado['Valor total nf'])}<br>
        <b>Valor do Cliente:</b> R$ {dado['valor'].replace(".",",")}<br>
        <b>Status:</b> {escreva(dado['Status'])}

        
'''

    mgsText = MIMEText(body,  'html')
    mgsAlternativa.attach(mgsText)

    text = mgs.as_string()
    servidor.sendmail(sender,receiver.split(','),text)
    print('EMAIL ENVIANDO COM SUCESSO!!')
    logging.info('EMAIL ENVIANDO COM SUCESSO!!')






# dados = [
# {
# 'nome' : 'ARITUZA TIMBO FREITAS',
# 'valor' : '450,00',
# 'Emp fandi' : 'NOVALUZ WS',
# 'Valor total nf' : 4826.5,
# 'Empresa' : 'NOVALUZ WS',
# 'datas': '23/04/2024 17:29:42',
# 'Status' : 'Liquidacão feita'

# },
# {     'nome' : 'SANDRO RIOS SILVEIRA',
#     'valor' : '240.0',
#     'Emp fandi' : 'NOVALUZ WS',
#     'Valor total nf' : 5780.16,
#     'Empresa' : 'NOVALUZ WS',
#     'datas': '23/04/2024 17:29:42',
#     'Status' : 'Liquidacão feita'},
# {     
#     'nome' : 'RONALDO DO NASCIMENTO FERREIRA',
#     'valor' : '3118.29',
#     'Emp fandi' : 'NOVALUZ WS',
#     'Valor total nf' : 5780.16,
#     'Empresa' : 'NOVALUZ WS',
#     'datas': '23/04/2024 17:29:42',
#     'Status' : 'Liquidacão feita'}
# ]
# email_plus_bancario(dados)

                    

    
