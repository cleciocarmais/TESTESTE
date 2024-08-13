import pyautogui as p
import logging 
import os
import traceback
import pandas as pd
from src.Model.loginDealer import login_dealer_contas_receber
from src.Model.muda_empresa2 import muda_empresa_contas_a_receber
from Model.comissaoSPF.emali_comissa_spf import email_comissa_spf
from Model.comissaoSPF.pesquisa_titulo_spf import pesquisar_titulo_comissao_spf
from Model.comissaoSPF.liquidacaoSPF import get_liquidacao_spf
from Model.comissaoSPF.emali_comissa_spf import email_comissa_spf



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

df = pd.read_excel('C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_NOSSAMOTO\planilha7.xlsx', dtype=str)


try:
        login_dealer_contas_receber()
        p.sleep(1)
        muda_empresa_contas_a_receber("NOSSAMOTO MATRIZ")
        for i in range(len(df.index)):
                resultado = pesquisar_titulo_comissao_spf(df['NOME'][i],df['CPF'][i])
                if resultado:
                      get_liquidacao_spf()
                      df['Status'][i] = 'Feito'
                else:
                      df['Status'][i] = 'Titulo nao Encontrado'
                df.to_excel('C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_NOSSAMOTO\planilha7.xlsx',index=False)
                logging.info(f"ULTIMO CPF FEITO {df['CPF'][i]}")
                logging.info(f'ULTIMA LINHA FEITA {i}')
      
except:
        mgs = traceback.format_exc()
        logging.info(mgs)
        print(mgs)

finally:
        os.system('TASKKILL /PID sof.exe')
        df.to_excel('C:\RPA_O_MAIS_LINDO_DA_EQUIPE\RPA_LIQUIDACAO_NOSSAMOTO\planilha7.xlsx',index=False)




    
