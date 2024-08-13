import logging
import pyautogui as p
# from clickApi import click2 as c

from src.Model.clickApi import click2 as c
import traceback
# from src.Model.calculo_imposto import imposto_irrf

from datetime import timedelta, datetime, date
import traceback
import pyperclip as pyp
numeroDocumentoControlado = '5366153'

def get_liquidacao_spf():
    try :
        print("REALIZANDO LIQUIDACAO DE COMISSAO SPF")

        # SALVANDO NUMERO_LANCAMENTO 
        img = 'C:/RPA/arquivos/images/'
        p.press('Tab')
        p.sleep(1)
        creditos_debitos = p.locateCenterOnScreen(f'{img}creditos_ou_debitos.png', confidence=0.95)
        while creditos_debitos == None:
            p.sleep(0.5)
            print('   carregando pagina titutos')
        else:
            logging.info('  Erro ao processa varivael creditos_debitos')
        p.sleep(1)
        c(creditos_debitos.x,creditos_debitos.y)
        
        p.sleep(1)
        mensagem_saldo = p.locateCenterOnScreen(f'{img}erro_critico2.png', confidence=0.95)
        if mensagem_saldo != None:
            p.sleep(1)
            btn_bok_ok = p.locateCenterOnScreen(f'{img}ok100.png', confidence=0.90)
            if btn_bok_ok != None:
                c(btn_bok_ok.x, btn_bok_ok.y)
            else:
                print('    Erro ao processa variavel btn_bok_ok')
        else:
            logging.info('  Erro ao processa variavel erro_critico')
        p.sleep(2)
        print('COMPLEMENTO')
        logging.info('COMPLEMENTO')
        incluir = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if incluir != None:
            c(incluir.x,incluir.y)
        else:
            print('  Erro ao processo variavel incluir')

        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while creditos_debitos2 == None:
            p.sleep(0.5)
            print("  aguarade tela de inclusão aparace")
            creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        if creditos_debitos2 != None:
            c(creditos_debitos2.x+70, creditos_debitos2.y)

        else:
            logging.info('Erro ao processa variavel creditos_debitos2')
        
        
        print("  Selecioando tipo de Credito/Debito")
        logging.info("  Selecioando tipo de Credito/Debito")
        p.write("COMPLEMENTO TÍTULO AVULSO (+)(+)(X)")
        p.press('Enter')
        p.sleep(2)
        p.press("Tab") # buscando informaçoes
        p.sleep(1)
        p.press("Tab") # pula data movimento 
        p.sleep(1)
        p.press("Tab") # pula data de caixa
        p.sleep(1)
       
        p.sleep(0.5)
        p.hotkey('ctrl','shift','right')  
        p.press('backspace', presses=300)


        p.write('80,00')
        p.press("Tab")
        p.sleep(1)
        p.write('COMP')
    
        p.sleep(1)
        documento_tipo = p.locateCenterOnScreen(f'{img}documento_tipo.png', confidence=0.95)
        if documento_tipo != None:
            c(documento_tipo.x+50, documento_tipo.y)
        else:
            p.alert('Erro durante execucao')
        p.sleep(0.5)
        p.write('AV.LANCTO')
        p.sleep(0.5)
        p.press('Enter')
        p.sleep(2)


        btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
        if btn_ok02 !=None:
            c(btn_ok02.x, btn_ok02.y)
        else:
            logging.info('Erro ao processa variavel cancela')
            p.alert('ola')
        # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        # if cancelar != None:
        #     c(cancelar.x,cancelar.y)
        p.sleep(2)
        #SEGUNDO PASSO

        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while creditos_debitos2 != None:
            p.sleep(1)
            creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)

        incluir2 = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if incluir2 != None:
            c(incluir2.x, incluir2.y)
        
        p.sleep(1)

        incluir3 = p.locateCenterOnScreen(f'{img}incluir6.png', confidence=0.95)
        if incluir3 != None:
            c(incluir3.x,incluir3.y)
        else:
            print('  Erro ao processo variavel incluir')

        print("  Selecioando tipo de Credito/Debito")
        logging.info("  Selecioando tipo de Credito/Debito")
        p.write("IRRF RETIDO (-)(-)(31)")
        p.press('Enter')
        p.sleep(2)
        p.press("Tab") # buscando informaçoes
        p.sleep(1)
        p.press("Tab") # pula data movimento 
        p.sleep(1)
        p.press("Tab") # pula data de caixa
        p.sleep(1)

        print('  Inicializando calculo de Imposto')
        logging.info('  Inicializando calculo de Imposto')
   
        p.sleep(0.5)
        print("  Calculo realizado")
        logging.info("  Calculo realizado")
        p.hotkey('ctrl','shift','right')   
        p.press('backspace', presses=300)


        p.write('1,95')
        p.press("Tab")
        p.sleep(1)
        p.write('IRRF')
    
        p.sleep(1)
        documento_tipo = p.locateCenterOnScreen(f'{img}documento_tipo.png', confidence=0.95)
        if documento_tipo != None:
            c(documento_tipo.x+50, documento_tipo.y)
        else:
            p.alert('Erro durante execucao')
        p.sleep(0.5)
        p.write('AV.LANCTO')
        p.sleep(0.5)
        p.press('Enter')
        p.sleep(2)

        btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
        if btn_ok02 !=None:
            c(btn_ok02.x, btn_ok02.y)
        else:
            logging.info('Erro ao processa variavel cancela')
            p.alert('ola')
        
        # cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        # if cancelar != None:
        #     c(cancelar.x,cancelar.y)
# 2637665
###################################################     LIQUIDAÇÃO      ###################################################


        p.sleep(2)
        print('INCIANDO PROCESSO DE LIQUIDACAO')
        logging.info('INCIANDO PROCESSO DE LIQUIDACAO')

        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while creditos_debitos2 != None:
            p.sleep(1)
            creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)

        incluir2 = p.locateCenterOnScreen(f'{img}incluir5.png', confidence=0.95)
        if incluir2 != None:
            c(incluir2.x, incluir2.y)
        
        p.sleep(1)

        incluir3 = p.locateCenterOnScreen(f'{img}incluir6.png', confidence=0.95)
        if incluir3 != None:
            c(incluir3.x,incluir3.y)
        else:
            print('  Erro ao processo variavel incluir')

        creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        while creditos_debitos2 == None:
            p.sleep(0.5)
            print("  aguarade tela de inclusão aparace")
            creditos_debitos2 = p.locateCenterOnScreen(f'{img}credito_debito2.png', confidence=0.95)
        if creditos_debitos2 != None:
            c(creditos_debitos2.x+70, creditos_debitos2.y)

        else:
            logging.info('  Erro ao processa variavel creditos_debitos2')  

        print("  Selecioando tipo de Credito/Debito")
        logging.info("  Selecioando tipo de Credito/Debito")
        p.write("LIQUIDAÇÃO(-)(01)")
        p.press('Tab')  
        p.sleep(0.5)
        p.press('Tab')
        p.sleep(0.5)  
        p.press('Tab')
        p.sleep(0.5)  
        p.write('CRED')
        p.sleep(1)
        ag_cobrador = p.locateCenterOnScreen(f'{img}ag_cobrador.png', confidence=0.95)
        if ag_cobrador != None:
            c(ag_cobrador.x+55, ag_cobrador.y)
            p.write('ITAU NOSSAMOTO - CC.:31066-7 (67)')
            p.press("Enter")
            p.sleep(1)
            p.press('Tab')
        p.sleep(1)

        if numeroDocumentoControlado == 0:
            print('Primeira consulta do grupo')
            lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
            if lancamento != None:
                c(lancamento.x+150, lancamento.y)
            p.sleep(1)
            # dia = pessoa['datas'][0:2]
            # mes = pessoa['datas'][3:5]
            # ano = pessoa['datas'][6:-8]
            # p.write(f'{dia}{mes}{ano[2:-1]}')
            # p.press("Tab")
            # data_atual = date(int(ano),int(mes),int(dia))
            # data_futura = data_atual + timedelta(days=3)
            # data_formatada = data_futura
            # p.write(data_formatada.strftime('%d%m%y'))
            # p.write('200224')

            # p.press("Tab")
            # valor_liquito = float(valor_nf) * (100-1.5) / 100
            # valor_round = round(valor_liquito, 2)
            # valor_final = str(valor_round)
            # valor_f = valor_final.replace('.',',')


            # print(' Calculo realizado')
            # logging.info(' Calculo realizado')

            # print(' Inserindo valor liquido')
            # logging.info(' Inserindo valor liquido')
            # p.write(valor_f)
            # p.press('Tab')
            # p.write(valor_f)
            # p.sleep(1)
            # p.press('Enter')
            # p.sleep(4)
            # sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
            # if sem_dados == None:
            #     p.press('Enter')
            # p.sleep(2)
            # # lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
            # # if lancamento != None:
            # p.hotkey('ctrl', 'c')
            # p.sleep(1)
            
            # numeroDocumentoControlado = pyp.paste()
            # print(numeroDocumentoControlado)
            # p.press('Tab')
            # p.sleep(1)

            # btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
            # if btn_ok02 !=None:
            #     c(btn_ok02.x, btn_ok02.y)
            p.sleep(2)
            excessao_titulo = p.locateCenterOnScreen(f'{img}excessao_titulo.png', confidence=0.95)
            print(" Conferir se tem excessao")
            logging.info("  Conferir se tem excessao")
            if excessao_titulo != None:
                print(" Execessao encontrada")
                logging.info('  Excessao encontrada')
                p.press('Enter')

            cancelar = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
            if cancelar != None:
                c(cancelar.x,cancelar.y)
            
            p.sleep(2)
        else:
            lancamento = p.locateCenterOnScreen(f'{img}Lancamento38.png', confidence=0.95)
            if lancamento != None:
                c(lancamento.x+55, lancamento.y)
                p.write(numeroDocumentoControlado)
                p.press('Tab')

            btn_ok02 = p.locateCenterOnScreen(f'{img}ok_fiat.png', confidence=0.95)
            if btn_ok02 !=None:
                c(btn_ok02.x, btn_ok02.y)
            p.sleep(1.5)
            excessao_titulo = p.locateCenterOnScreen(f'{img}excessao_titulo.png', confidence=0.95)
            if excessao_titulo != None:
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
            p.sleep(1)
            fechar = p.locateCenterOnScreen(f'{img}fechar38.png',confidence=0.95)
        
        p.sleep(1)
        
        return True

        
    except:
        erro = traceback.format_exc()
        print(erro)
        return False
if __name__=='__main__':
    p.sleep(4)
    get_liquidacao_spf()
    
   
   
   
    









