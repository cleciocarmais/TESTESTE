import pyautogui as p
import pandas as pd
import logging
import os
from src.Model.loginDealer import login_dealer_contas_receber
from src.Model.loginDealer import login_dealer_controle_bancario
from src.Model.global_buscar_valor import glob_pesquisa_valor_dealer
from src.Model.muda_empresa2 import muda_empresa_contas_a_receber
from src.Model.muda_empresa2 import muda_empresa
from src.Model.global_utilitarios import glob_contas_gerenciais
from src.Model.plus_bancario.pesquisa_titulo_plus_bancario import pesquisar_titulo_comissao_spf
from src.Model.global_cpfs_cliente import pegando_informacoes
from src.Model.plus_bancario.liquidacao_plus_bancario import realizaLiquidacao_plus_bancario
from src.Model.clickApi import click2 as c
from src.Model.plus_bancario.Armazenamento import armazenaInfor,buscarInfor,resertaInfor
from src.Model.plus_bancario.emali_plus_bancario import email_plus_bancario
from src.Model.plus_bancario.token_plus_bancario import capturar_token,alterar_token,altera_chave_status
# import src.Model.plus_bancario.token_plus_bancario as cv


def run_plus_bancario(df,linha,lista_qtd_cliente, lista_cpf_cnpj) -> None:
    print('INICIANDO PROCESSO DE PLUS BANCARIO')
    logging.info('INICIANDO PROCESSO DE PLUS BANCARIO')
    
    token = capturar_token()

    if str(token['valor']) != str(df['Valor Total da Nota Fiscal'][linha]): #CASO OS VALORES SEJA DIVERGENTE ENTRA DENTRO DO IF 
       
        login_dealer_controle_bancario()
        p.sleep(0.5)
        muda_empresa(df['Empresa'][linha])
        resultado_valor = glob_pesquisa_valor_dealer(glob_contas_gerenciais[df['Empresa'][linha]],df['Carimbo de data/hora'][linha],df['Valor Total da Nota Fiscal'][linha])
        os.system("TASKKILL /PID scb.exe")
        # resultado_valor = True
        Novo_Valor_Processar = True
        alterar_token(df['Valor Total da Nota Fiscal'][linha],"")
       

    else:
        print('CONTINUACAO DO VALOR ANTERIOR PROCESSADO')
        resultado_valor = True
        Novo_Valor_Processar = False

    

    if resultado_valor:
        print("VALOR ENCONTRADO")
        if Novo_Valor_Processar:
            altera_chave_status('encontrado') 

        #SALVANDO OS DADOS QUE VEM DA PLANILHA E RETORNANDO UM OBJETO
        informacoes_usuario = pegando_informacoes(df,linha,lista_qtd_cliente,lista_cpf_cnpj)
        p.sleep(1)
        login_dealer_contas_receber()
        p.sleep(1)
        muda_empresa_contas_a_receber(df['Empresa'][linha])
        p.sleep(1)

      
        for id,usuario in enumerate(informacoes_usuario):
            if id == 0 and Novo_Valor_Processar:
                PRIMEIRA_EXECUCAO = True
            else:
                PRIMEIRA_EXECUCAO = False

            resultado_titulo = pesquisar_titulo_comissao_spf(usuario)
            # resultado_titulo = True
            if resultado_titulo == True:
                    resultado_liquidacao = realizaLiquidacao_plus_bancario(usuario,PRIMEIRA_EXECUCAO)
                    # resultado_liquidacao = True
                    if resultado_liquidacao == True:
                        armazenaInfor(usuario,'Liquidacão feita')

                    elif resultado_liquidacao =='saldo_insufiente':
                        armazenaInfor(usuario,'Valor saldo_insufiente no Dealer')
            elif resultado_titulo == 'n_encontrad':
                armazenaInfor(usuario,'Cliente não Encontrado')
                
            else:
                armazenaInfor(usuario,'Titulo não Encontrado')
            

                
        fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        if fechar != None:
            c(fechar.x, fechar.y)


        respostasLiquidacao = buscarInfor()
        if len(respostasLiquidacao) > 0:
            email_plus_bancario(respostasLiquidacao)
            resertaInfor()


    else:
        print(f'VALOR N ENCONTRADO DA LINHA {linha}')
        logging(f'VALOR N ENCONTRADO DA LINHA {linha}')
        altera_chave_status('n_encontrado')


        

      

                                
              


    
    
   





    

    
    