import logging
import pyautogui as p
import traceback
import pyperclip as pyp
# from clickApi import click2 as c
from src.Model.plus_bancario.clickApi import click2 as c
def pesquisar_titulo_comissao_spf(Nome_cliente):

    img = 'C:/RPA/arquivos/images/'
    print(f'--PESQUISADO TITULO  DE { Nome_cliente }')   
    logging.info(f'--PESQUISADO TITULO  DE { Nome_cliente }')
    cpf = Nome_cliente['cpfs_cnpj']
    #ATALHOS PARA ACESSAR TITULOS 
    p.sleep(0.5)
    p.hotkey('alt','u') #acessando titulos
    p.sleep(0.5)
    p.press('Enter')
   
    p.sleep(2)
    
    campo_lancamento = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)
    while campo_lancamento == None:
        p.sleep(1)
        print(" aguarde")
        campo_lancamento = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)

    if campo_lancamento != None:
        c(campo_lancamento.x+100, campo_lancamento.y)
    else:
        logging.info('  Erro na imagem ancora_titulo')
    p.sleep(1)

    caixa_selecao_empresa_consulta_titulos = p.locateCenterOnScreen(f'{img}empresa_consulta_titulo.png', confidence=0.95)
    if caixa_selecao_empresa_consulta_titulos != None:
        c(caixa_selecao_empresa_consulta_titulos.x+90, caixa_selecao_empresa_consulta_titulos.y)
    p.sleep(1)
    p.write('<NENHUMA>')
    p.press('Enter')
    p.press("tab") #pulando para sacado
    p.write("0048438")
    p.press("Tab")
       
    p.sleep(1)
 
    campo_endossado_Consulta_titulos = p.locateCenterOnScreen(f'{img}endosado.png', confidence=0.95)
    if campo_endossado_Consulta_titulos != None:
        c(campo_endossado_Consulta_titulos.x+80,campo_endossado_Consulta_titulos.y)
     
    else:
        print('ola')
    
    campo_cpf_consulta_Cliente = p.locateCenterOnScreen(f'{img}cpf.png', confidence=0.95)
    while campo_cpf_consulta_Cliente == None:
        p.sleep(1)
        campo_cpf_consulta_Cliente = p.locateCenterOnScreen(f'{img}cpf.png', confidence=0.95)
    c(campo_cpf_consulta_Cliente.x+45, campo_cpf_consulta_Cliente.y)

    p.press('backspace',presses=3000)
    cpf = str(cpf)
    cpf = cpf.zfill(11)
    p.write(cpf)
    p.press('Enter')
    p.sleep(4)
    caixa_dialogo_sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
    if caixa_dialogo_sem_dados != None:
        print("CLIENTE NÃO ENCONTRADO")
        logging.info("CLIENTE NÃO ENCONTRADO")
        p.press('Enter')
        p.sleep(2)
        p.hotkey('alt','c')
        p.sleep(2)
        p.hotkey('alt','c')
        btn_fechar = p.locateCenterOnScreen(f'{img}fechar12.png', confidence=0.95)
        if btn_fechar != None:
            c(btn_fechar.x, btn_fechar.y)
        #CLIENTE N ENCONTRADO ---
        return 'n_encontrado'
    
    p.press('Enter')
    p.sleep(2)
    p.press("Tab")
    p.write('PB')
    p.press('Tab')
    p.sleep(0.5)

    radio_btn_aberto = p.locateCenterOnScreen(f'{img}em_aberto_liquidacao.png', confidence=0.95)
    if radio_btn_aberto != None:
        c(radio_btn_aberto.x,radio_btn_aberto.y)
    else:
        logging.info('Erro na variavel emAberto')
    p.sleep(1)

    # todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
    # if todos != None:
    #     c(todos.x, todos.y)
    # else:
    #    print("  Erro na variavel todos")
    

    btn_ok = p.locateCenterOnScreen(f'{img}btn_ok_desmarcado.png', confidence=0.95)
    if btn_ok !=None:
        c(btn_ok.x,btn_ok.y)
    
    p.sleep(4)
    caixo_dialogo_sem_dados2 = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
    btn_ok = p.locateCenterOnScreen(f'{img}ok100.png', confidence=0.95)
    if caixo_dialogo_sem_dados2 != None:
        print('TITULO NAO ENCONTRADO')
        logging.info('TITULO NAO ENCONTRADO ')
        p.sleep(1)
        c(btn_ok.x,btn_ok.y)
        btn_cancela = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        if btn_cancela !=None:
            c(btn_cancela.x, btn_cancela.y)
        p.sleep(0.5)
        btn_fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        while btn_fechar != None:
                c(btn_fechar.x,btn_fechar.y)
                p.sleep(1)
                btn_fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        
        return False
    else:
        print("TITULO ENCONTRADO COM SUCESSO!!")
        logging.info("TITULO ENCONTRADO COM SUCESSO!!")
        radio_btn_todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
        while radio_btn_todos !=None:
            print("  carregando informaçoes!!!!")
            p.sleep(0.5)
            radio_btn_todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
            p.sleep(1)
        p.press('Enter')
        p.sleep(1)
    
        p.sleep(1)
        # cancela = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        # if cancela !=None:
        #     c(cancela.x, cancela.y)
        # p.sleep(0.5)
        # fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        # while fechar != None:
        #         c(fechar.x,fechar.y)
        #         p.sleep(1)
        #         fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        

        
        return True
    

if __name__ == '__main__':
   
    
    pesquisar_titulo_comissao_spf('','93401639315')
