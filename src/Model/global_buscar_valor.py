import pyautogui as p
import logging
from src.Model.global_clickApi import click2 as c
from datetime import timedelta, datetime, date
from src.Model.global_calculo_imposto import glob_calculo_valor

#MODULO ACESSA CONTROLE BANCARIO E PESQUISA VALOR COM DESCONTO DO IMPOSTO

def glob_pesquisa_valor_dealer(conta,data,valor):
    """
        RETORNA TRUE CASO VALOR SEJA ENCONTRADO 
        CASO NÃO SEJA ENCONTRADO RETORNA FALSE

--------- PARAMENTROS ----------------\n
        CONTA GERENCIAL\n
        DATA INICIAL ENTRADA DO VALOR\n 
        VALOR TOTAL DA NOTA FISCAL \n
    """
    print("BUSCANDO VALOR VALOR")
    logging.info("BUSCANDO  VALOR")

    print("aguarde!!")
    print(data)
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:-8]
    
  
   
    #INSERINDO NUMERO DA CONTA GERANCIAL DA NOSSAMOTA MATRIZ
    lanca = p.locateCenterOnScreen('C:/RPA/arquivos/images/lancamentos_scb.png', confidence=0.95)
    if lanca != None:
        c(lanca.x, lanca.y)
    p.sleep(2)
    p.write(conta)
    p.press("Tab")
    #INSERINDO  DATA DE ENTRADA DO VALOR ATE DATA ATUAL
    p.write(f'{dia}{mes}{ano[2:-1]}') 
    p.press('Tab')
    data_futura = date.today()
    data_atual = data_futura.strftime('%d%m%y')
    p.write(data_atual)
    p.press("Tab")
    p.sleep(2)


    tela_de_espera_1 = p.locateCenterOnScreen('C:/RPA/arquivos/images/tabela_branco.png', confidence=0.95)
    while tela_de_espera_1 != None:
        p.sleep(2)
        print("Aguarde")
        tela_de_espera_1 = p.locateCenterOnScreen('C:/RPA/arquivos/images/tabela_branco.png', confidence=0.95)
    p.sleep(2)

    # saldos_pendentes = p.locateCenterOnScreen('C:/RPA/arquivos/images/saldos_pendentes.png', confidence=0.95)
    # if saldos_pendentes != None:
    #     c(saldos_pendentes.x, saldos_pendentes.y)
    # else:
    #     print('Erro ao processar variavel saldo_pendentes')
    #     logging.info('Erro ao processar variavel saldo_pendentes')
        
    p.sleep(2)
    tela_espera_2 = p.locateCenterOnScreen('C:/RPA/arquivos/images/tabela_branco.png', confidence=0.95)
    while tela_espera_2 != None:
        p.sleep(2)
        print("Aguarde")
        tela_espera_2 = p.locateCenterOnScreen('C:/RPA/arquivos/images/tabela_branco.png', confidence=0.95)
    p.sleep(1)

    

    caixa_entrada_valor = p.locateCenterOnScreen('C:/RPA/arquivos/images/valor_entre.png', confidence=0.95)
    if caixa_entrada_valor != None:
        c(caixa_entrada_valor.x+40, caixa_entrada_valor.y)
    else:
        logging.info('Erro ao processa variavel valor_entre')
    valor_com_desconto_de_imposto = glob_calculo_valor(valor)
    p.write(valor_com_desconto_de_imposto)
    p.press('Tab')
    p.write(valor_com_desconto_de_imposto)
    p.sleep(1)
    p.press("Tab")
    p.sleep(3)
    #SE CAIXA DE VALORES N FOR ENCONTRADO TEM VALOR NA CONTA
    caixas_de_valores = p.locateCenterOnScreen('C:/RPA/arquivos/images/reseultado_lancamentos.png', confidence=0.95)
    if caixas_de_valores == None:
        return True
    else:
        return False

    




if __name__=='__main__':
    glob_pesquisa_valor_dealer('41160','08/01/2024 16:21:11','10314.55')