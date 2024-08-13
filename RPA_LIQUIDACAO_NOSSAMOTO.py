import gspread
import logging
import pandas as pd
import pyautogui as p
import traceback
import os 
from src.Controller.Controller_plus_bancario import run_plus_bancario
from src.Model.plus_bancario.token_plus_bancario import capturar_token



with open('C:/RPA/Credenciais/pid_bot_running.txt', 'r') as file:
    pid_bot_anterior = file.readlines()[0] # Lendo o conteudo do arquivo - Numero do processo do bot anterior
    os.system('taskkill /PID  ' + pid_bot_anterior +  '   /F') # Forcando o encerramento do bot anterior

# Gravando o n�mero do processo do bot atual no arquivo pid_bot_running.txt
with open('C:/RPA/Credenciais/pid_bot_running.txt', 'w') as file:
    file.write(str(os.getpid())) # sobrescrevendo o numero do PID

    
with open(r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_NOSSAMOTO\log_RPA_LIQUIDACAO_NOSSAMOTO.txt', 'w') as f:
        pass

logging.basicConfig(filename=r'C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_NOSSAMOTO\log_RPA_LIQUIDACAO_NOSSAMOTO.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p')
print("ACESSANDO INFORMAÇOES!!")
CHAVE_ACESSO = 'C:/RPA/Credenciais/service_account.json'
gs = gspread.service_account(CHAVE_ACESSO)
sh = gs.open('Comissão Financiamento Nossamoto (respostas)')
sh = sh.worksheet("Respostas ao formulário 1")
df = pd.DataFrame(sh.get_all_records())
print("Informações baixada com sucesso!!!")
LISTA_QTD_CLIENTE = [str(x) for x in df['Quantidade de Clientes']]
LISTA_CPFS_CNPJ = [str(x) for x in df['CPF/CNPJ']]


os.system("TASKKILL /PID scb.exe")
os.system("TASKKILL /PID scr.exe")


#TODO LEMBRA DE INCLUIR SALDO PENDENTE NO BUSCAR VALOR O MESMO ESTA COMENTADO 
for linha in range(len(df.index)):
    if df['Liquidado'][linha] == "":

        if df['Tipo de Bonificação'][linha] == 'Plus Bancário':

            if str(df['Valor Total da Nota Fiscal'][linha]) == str(capturar_token()['valor']) and capturar_token()['status'] != 'encontrado':
                continue
            else:
                run_plus_bancario(df,linha,LISTA_QTD_CLIENTE[linha], LISTA_CPFS_CNPJ[linha])

            os.system("TASKKILL /PID scb.exe")
            os.system("TASKKILL /PID scr.exe")
    else:
         print('ja foi ')












