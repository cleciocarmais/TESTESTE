import logging
import pyautogui as p
# from clickApi import click2 as c
import sys
# sys.path.append('C:/RPA_O_MAIS_LINDO_DA_EQUIPE/RPA_LIQUIDACAO_COMISSOES')
from src.Model.global_clickApi import click2 as c
import traceback
from src.Model.global_calculo_imposto import glob_imposto_irrf
# from calculo_imposto import imposto_irrf  5693,46 
# from muda_empresa2 import muda_empresa_contas_a_receber
from datetime import timedelta, datetime, date
import traceback
import pyperclip as pyp
from src.Model.plus_bancario.token_plus_bancario import alterar_token,capturar_token
numeroDocumentoControlado = 0

def realizaLiquidacao_plus_bancario(pessoa,flag):
    print('REALIZANDO LIQUIDACAO DO TITULO')
    logging.info('REALIZANDO LIQUIDACAO DO TITULO')
    
    global numeroDocumentoControlado
    if flag:
        numeroDocumentoControlado = 0

    try :
    
        print("aguarde!!")
        p.sleep(2)
        valor_cliente= pessoa['valor']
        valor_nf = pessoa['Valor total nf']
        p.hotkey('ctrl','c')
        LANCAMENTO = pyp.paste()
        
        img = 'C:/RPA/arquivos/images/'
        p.press('Tab')
        p.sleep(1)
        btn_icon_saquinho_dinheiro = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)
        while btn_icon_saquinho_dinheiro == None:
            p.sleep(0.5)
            print('Carregando pagina titutos')
            btn_icon_saquinho_dinheiro = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)

     
        p.sleep(1)
        p.press('Esc')
        p.sleep(1)

        #BOTAO DE INCLUIR DA JANELA DE TIULOE
        btn_incluir_titulo = p.locateCenterOnScreen(f'{img}incluir_titulo.png', confidence=0.95)
        if btn_incluir_titulo != None:
            c(btn_incluir_titulo.x, btn_incluir_titulo.y)

        p.sleep(0.5)
        #CAMPO DE VALOR DE TITULO DA JANELA DE TITULO
        campo_valor_titulo = p.locateCenterOnScreen(f'{img}valor_titulo.png', confidence=0.95)
        if campo_valor_titulo != None:
            c(campo_valor_titulo.x+75, campo_valor_titulo.y)
            p.press("End")
            p.hotkey('ctrl','c')
        #COLANDO A CAPIA DO VALOR
        valorDealer = pyp.paste()
        valorDealer = valorDealer.replace('.',"")
        valorDealer = valorDealer.replace(',','.')


        p.sleep(1)
        p.press('Esc')
        p.sleep(0.5)
        p.write(LANCAMENTO)
        p.press('tab')
        p.sleep(1)

        list_ta = valor_cliente.split(".")
        if len(list_ta[1]) == 1:
            valor_cliente+= "0"
        p.sleep(1)

        btn_icon_saquinho_dinheiro = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)
        if btn_icon_saquinho_dinheiro != None:
            c(btn_icon_saquinho_dinheiro.x, btn_icon_saquinho_dinheiro.y)
        else:
            logging.info('Erro ao processa o valor da variavel creditos_debitos')
        
        p.sleep(1)
        caixa_dialogo_saldo = p.locateCenterOnScreen(f'{img}erro_critico2.png', confidence=0.95)
        if caixa_dialogo_saldo != None:
            p.sleep(1)
            btn_bok_ok = p.locateCenterOnScreen(f'{img}ok100.png', confidence=0.90)
            if btn_bok_ok != None:
                c(btn_bok_ok.x, btn_bok_ok.y)
            else:
                print('Erro : variave btn_bok_ok n encontrou a img')
        else:
            logging.info('Erro : variave caixa_dialogo_saldo n encontrou a img')
        p.sleep(2)

        print('INICIALIZANDO PROCESSO DE INCLUSÃO IRRF')
        logging.info('INICIALIZANDO PROCESSO DE INCLUSÃO IRRF')
        btn_inclusao_credito = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if btn_inclusao_credito != None:
            c(btn_inclusao_credito.x,btn_inclusao_credito.y)
        else:
            print("Erro : variave btn_inclusao_credito n encontrou a img")
        p.sleep(1)


        caixa_selecao_creditos_inclusao_Creditos = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while caixa_selecao_creditos_inclusao_Creditos == None:
            p.sleep(0.5)
            print("aguarade tela de inclusão aparace")
            caixa_selecao_creditos_inclusao_Creditos = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        p.sleep(1)

        c(caixa_selecao_creditos_inclusao_Creditos.x+70, caixa_selecao_creditos_inclusao_Creditos.y)

          

        if valorDealer != valor_cliente:
            print("VALORES DIVERGENTES ENTRE CLIENTE E DEALER")
            logging.info("VALORES DIVERGENTES ENTRE CLIENTE E DEALER")
            diferenca = float(valorDealer) - float(valor_cliente)
            if diferenca > 0:
                print('DIFERENÇA POSITIVA')
                print("SELECIONADO TIPO  ESTORNO TITULO AVULSO Á MAIOR (-) (XXX)")
                logging.info("SELECIONADO TIPO ESTORNO TITULO AVULSO Á MAIOR (-) (XXX)")
               
                diferenca = round(diferenca,2)
          
                p.write("ESTORNO TITULO AVULSO Á MAIOR (-) (XXX)")
                p.press('Enter')
                p.sleep(2)
                p.press("Tab") # buscando informaçoes
                p.press("Tab") # pula data movimento 
                p.press("Tab") # pula data de caixa
            
                
                p.sleep(0.5)
                p.hotkey('ctrl','shift','right')  
                p.press('backspace', presses=300)


                p.write(str(diferenca).replace(".",","))
                p.press("Tab")
                p.sleep(1)
                p.write('ESTORNO')

                p.sleep(1)
                tipo_documento = p.locateCenterOnScreen(f'{img}documento_tipo.png', confidence=0.95)
                if tipo_documento != None:
                    c(tipo_documento.x+50, tipo_documento.y)
                else:
                    p.alert('Erro: varivale tipo_documento n encontrou a img ')
                p.sleep(0.5)
                p.write('AV.LANCTO')
                p.sleep(0.5)
                p.press('Enter')
                p.sleep(2)
####################################################################################################################################################################

                btn_ok_final = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
                if btn_ok_final !=None:
                    c(btn_ok_final.x, btn_ok_final.y)
####################################################################################################################################################################
                    
                # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
                # if cancelar != None:
                #     c(cancelar.x,cancelar.y)
            else:
                print('Diferença negativa')
                print("Selecionado tipo COMPLEMENTO TÍTULO AVULSO (+)(+)(X)")
                logging.info("Seleciananto tipo COMPLEMENTO TÍTULO AVULSO (+)(+)(X)")

                # diferenca = abs(diferenca)
                diferenca = round((diferenca * -1),2)
                diferenca = str(diferenca).replace(".",",")
                p.write("COMPLEMENTO TÍTULO AVULSO (+)(+)(X)")
                p.press('Enter')
                p.sleep(2)
                p.press("Tab") # buscando informaçoes
                p.press("Tab") # pula data movimento 
                p.press("Tab") # pula data de caixa
                
                p.sleep(0.5)
                p.hotkey('ctrl','shift','right')  
                p.press('backspace', presses=300)

             
                p.write(diferenca)
                p.press("Tab")
                p.sleep(1)
                p.write('COMP')

                p.sleep(1)
                tipo_documento = p.locateCenterOnScreen(f'{img}documento_tipo.png', confidence=0.95)
                if tipo_documento != None:
                    c(tipo_documento.x+50, tipo_documento.y)
                else:
                    p.alert('Erro durante execucao')
                p.sleep(0.5)
                p.write('AV.LANCTO')
                p.sleep(0.5)
                p.press('Enter')
                p.sleep(2)
####################################################################################################################################################################

                btn_ok_final = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
                if btn_ok_final !=None:
                    c(btn_ok_final.x, btn_ok_final.y)
####################################################################################################################################################################

                # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
                # if cancelar != None:
                #     c(cancelar.x,cancelar.y)

            caixa_selecao_creditos_inclusao_Creditos = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
            while caixa_selecao_creditos_inclusao_Creditos != None:
                print('Aguardando terminar a inclusao')
                p.sleep(1)
                caixa_selecao_creditos_inclusao_Creditos = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)

            btn_inclusao_creditos2 = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
            if btn_inclusao_creditos2 != None:
                c(btn_inclusao_creditos2.x, btn_inclusao_creditos2.y)
            
            p.sleep(1)

            btn_inclusao_credito3 = p.locateCenterOnScreen(f'{img}incluir6.png', confidence=0.95)
            if btn_inclusao_credito3 != None:
                c(btn_inclusao_credito3.x,btn_inclusao_credito3.y)
            else:
                print('  Erro ao processo variavel incluir')
        print('INCLUSAO DE IRRF RETIDO')
        logging.info('INCLUSAO DE IRRF RETIDO')
        p.sleep(1)
        p.write("IRRF RETIDO (-)(-)(31)")
        p.press('Enter')
        p.sleep(2)
        p.press("Tab") # buscando informaçoes
        p.press("Tab") # pula data movimento 
        p.press("Tab") # pula data de caixa
        p.sleep(0.5)
        p.hotkey('ctrl','shift','right')   
        p.press('backspace', presses=300)
        valor_finals = glob_imposto_irrf(valor_cliente)
        p.write(valor_finals)
        p.press("Tab")
        p.sleep(1)
        p.write('IRRF')
    
        p.sleep(1)
        tipo_documento = p.locateCenterOnScreen(f'{img}documento_tipo.png', confidence=0.95)
        if tipo_documento != None:
            c(tipo_documento.x+50, tipo_documento.y)
        else:
            p.alert('Erro: variavel tipo documento n encontrou img')
        p.sleep(0.5)
        p.write('AV.LANCTO')
        p.sleep(0.5)
        p.press('Enter')
        p.sleep(2)

####################################################################################################################################################################
        btn_ok_final = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
        if btn_ok_final !=None:
            c(btn_ok_final.x, btn_ok_final.y)
        else:
            logging.info('Erro ao processa variavel cancela')
            p.alert('ola')
        print("PROCESSO FINALIZAD DE IRRF")
        logging.info("PROCESSO FINALIZAD DE IRRF")
###########################################################################################################################################################################
        # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        # if cancelar != None:
        #     c(cancelar.x,cancelar.y)
# 2637665
###################################################     LIQUIDAÇÃO      ###################################################

#TODO CONTINUAR DA AQUI A REVISAO DE CODIGO
        p.sleep(3)
        print('INCIANDO PROCESSO DE LIQUIDACAO')
        logging.info('INCIANDO PROCESSO DE LIQUIDACAO')

        caixa_selecao_creditos_inclusao_Creditos = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while caixa_selecao_creditos_inclusao_Creditos != None:
            p.sleep(1)
            caixa_selecao_creditos_inclusao_Creditos = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        p.sleep(1)

        btn_inclusao_creditos2 = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if btn_inclusao_creditos2 != None:
            c(btn_inclusao_creditos2.x, btn_inclusao_creditos2.y)
        
        p.sleep(1)

        btn_inclusao_credito3 = p.locateCenterOnScreen(f'{img}incluir6.png', confidence=0.95)
        if btn_inclusao_credito3 != None:
            c(btn_inclusao_credito3.x,btn_inclusao_credito3.y)
        else:
            print('  Erro ao processo variavel incluir')

        caixa_selecao_creditos_inclusao_Creditos = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while caixa_selecao_creditos_inclusao_Creditos == None:
            p.sleep(0.5)
            print("  aguarade tela de inclusão aparace")
            caixa_selecao_creditos_inclusao_Creditos = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)

       
        c(caixa_selecao_creditos_inclusao_Creditos.x+70, caixa_selecao_creditos_inclusao_Creditos.y)

   
        p.write("LIQUIDAÇÃO(-)(01)")
        p.press('Tab')  
        p.sleep(0.5)
        p.press('Tab')
        p.sleep(0.5)  
        p.press('Tab')
        p.sleep(0.5)  
        p.write('LIQUIDACAO')
        p.sleep(1)
        campo_agente_cobrador = p.locateCenterOnScreen(f'{img}ag_cobrador.png', confidence=0.95)
        if campo_agente_cobrador != None:
            c(campo_agente_cobrador.x+55, campo_agente_cobrador.y)
            p.write('BANCO ITAU NOSSAMOTO (NM)')
            p.press("Enter")
            p.sleep(1)
            p.press('Tab')
        p.sleep(1)

        if numeroDocumentoControlado == 0:
            print('SALVANDO NUMERO DE LANCAMENTO')
            logging.info('SALVANDO NUMERO DE LANCAMENTO')
            campo_lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
            if campo_lancamento != None:
                c(campo_lancamento.x+150, campo_lancamento.y)
            p.sleep(2)
            dia = pessoa['datas'][0:2]
            mes = pessoa['datas'][3:5]
            ano = pessoa['datas'][6:-8]
            p.write(f'{dia}{mes}{ano[2:-1]}')
            p.press("Tab")
            

            data_formatada = date.today()
            p.write(data_formatada.strftime('%d%m%y'))
            # p.write('200224')

            p.press("Tab")
            valor_liquito = float(valor_nf) * (100-1.5) / 100
            valor_round = round(valor_liquito, 2)
            valor_final = str(valor_round)
            valor_f = valor_final.replace('.',',')


            p.write(valor_f)
            p.press('Tab')
            p.write(valor_f)
            p.sleep(1)
            p.press('Enter')
            p.sleep(4)
            caixa_dialogo_sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
            if caixa_dialogo_sem_dados == None:
                p.press('Enter')
                p.sleep(2)
                p.hotkey('ctrl', 'c')
                p.sleep(1)
                
                numeroDocumentoControlado = pyp.paste()
                print(numeroDocumentoControlado)
                alterar_token(valor_nf,numeroDocumentoControlado)
                p.press('Tab')
                p.sleep(1)
                btn_ok_final = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
                if btn_ok_final !=None:
                    c(btn_ok_final.x, btn_ok_final.y)

#################################################################################################################################################################
                p.sleep(2)
                CONFIRMAO_EMRESA = p.locateCenterOnScreen(f'{img}excessao_titulo.png', confidence=0.95)
            
                if CONFIRMAO_EMRESA != None:
                    p.press('Enter')
                # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
                # if cancelar != None:
                #     c(cancelar.x,cancelar.y)
            else:
                p.alert('VALOR N ENCONTRADO')
        else:
            
            campo_lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
            if campo_lancamento != None:
                c(campo_lancamento.x+55, campo_lancamento.y)
                p.write(capturar_token()['numero_lancamento'])
                p.press('Tab')
                p.sleep(3)

                saldo_insuficiente = p.locateCenterOnScreen(f'{img}saldo_insuficiente.png', confidence=0.95)
                if saldo_insuficiente != None:
                    ok_saldo_insufiente = p.locateCenterOnScreen(f'{img}ok_pontilhado.png', confidence=0.95)
                    c(ok_saldo_insufiente.x, ok_saldo_insufiente.y)
                    p.hotkey('alt','c')
                    fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
                    while fechar != None:
                        print("aguarde")
                        c(fechar.x, fechar.y)
                        p.sleep(1.5)
                        fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
                    return "saldo_insufiente"
            
            btn_ok_final = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
            if btn_ok_final !=None:
                c(btn_ok_final.x, btn_ok_final.y)





########################################################################################################################################################################
            p.sleep(1.5)
            CONFIRMAO_EMRESA = p.locateCenterOnScreen(f'{img}excessao_titulo.png', confidence=0.95)
            if CONFIRMAO_EMRESA != None:
                print(" Execessao encontrada")
                logging.info('  Excessao encontrada')
                p.press('Enter')
            # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
            # if cancelar != None:
            #     c(cancelar.x,cancelar.y)
        
        p.sleep(3)
        fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
        while fechar != None:
            print("aguarde")
            c(fechar.x, fechar.y)
            p.sleep(1.5)
            fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)

        print("PROCESSO FINALIZADO !! ")
        logging.info("PROCESSO FINALIZADO !! ")
        return True
    except:
        fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
        while fechar != None:
            print("aguarde")
            c(fechar.x, fechar.y)
            p.sleep(1.5)
            fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
        erro = traceback.format_exc()
        print(erro)
        return False
    
   
   
   
    








