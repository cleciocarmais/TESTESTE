import logging
import pyautogui as p
import traceback
import pyperclip as pyp
# from clickApi import click2 as c
from src.Model.clickApi import click2 as c
def pesquisar_titulo_comissao_spf(Nome_cliente,cpf):

    img = 'C:/RPA/arquivos/images/'
    print(f'*PESQUISADO TITULO  DE { Nome_cliente }')   
    logging.info(f'*PESQUISADO TITULO  DE { Nome_cliente }')
    p.sleep(0.5)
    p.hotkey('alt','u') #acessando titulos
    p.sleep(0.5)
    p.press('Enter')
    p.sleep(1 )
    print('    Busca informação do usuario')
    
    p.sleep(2)
    print('    Clicando em pesquisa por empresa')
    logging.info('  Clicando em pesquisa por empresa')
    ancora_titulo = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)
    while ancora_titulo == None:
        p.sleep(1)
        print(" aguarde")
        ancora_titulo = p.locateCenterOnScreen("C:/RPA/arquivos/images/titutlo_lancamento.png", confidence=0.95)

    if ancora_titulo != None:
        c(ancora_titulo.x+100, ancora_titulo.y)
    else:
        logging.info('  Erro na imagem ancora_titulo')
    p.sleep(1)

    empresa_tituto_consulta = p.locateCenterOnScreen(f'{img}empresa_consulta_titulo.png', confidence=0.95)
    if empresa_tituto_consulta != None:
        c(empresa_tituto_consulta.x+90, empresa_tituto_consulta.y)
        
    
    p.sleep(1)
    p.write('<NENHUMA>')
    p.press('Enter')
       


        
    p.sleep(1)
    print('    Clicando em pesquisa pelo endossado')  
    logging.info('  Clicando em pesquisa pelo endossado')
    ancora_endosado = p.locateCenterOnScreen(f'{img}endosado.png', confidence=0.95)
    print('    Inserindo nome do usuario')
    if ancora_endosado != None:
        c(ancora_endosado.x+80,ancora_endosado.y)
     
    else:
        print('ola')
    form_cpf = p.locateCenterOnScreen(f'{img}cpf.png', confidence=0.95)

    while form_cpf == None:
        p.sleep(1)
        form_cpf = p.locateCenterOnScreen(f'{img}cpf.png', confidence=0.95)
    c(form_cpf.x+45, form_cpf.y)
    p.press('backspace',presses=3000)
    cpf = cpf.zfill(11)
    p.write(cpf)
    p.press('Enter')
    p.sleep(4)
    sem_dados2 = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
    if sem_dados2 != None:
        p.press('Enter')
        p.sleep(2)
        p.hotkey('alt','c')
        p.sleep(2)
        p.hotkey('alt','c')

        fechar = p.locateCenterOnScreen(f'{img}fechar12.png', confidence=0.95)
        if fechar != None:
            c(fechar.x, fechar.y)
        return False
    p.press('Enter')
    p.sleep(2)
    p.press("Tab")
    print('    Inserindo Tipo do Titulo')
    logging.info('  Inserindo Tipo do Titulo')
    p.write('SP')
    p.press('Tab')
    print('    Esperando carregar informaçoes')
    logging.info('  Esperando carregar informaçoes')
    p.sleep(0.5)

    emAberto = p.locateCenterOnScreen(f'{img}em_aberto_liquidacao.png', confidence=0.95)
    if emAberto != None:
        c(emAberto.x,emAberto.y)
    else:
        logging.info('    Erro na variavel emAberto')
    p.sleep(1)

    # todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
    # if todos != None:
    #     c(todos.x, todos.y)
    # else:
    #    print("  Erro na variavel todos")
    
    print('    Clicando em confirma')
    logging.info('  Clicando em confirma')
    btn_ok = p.locateCenterOnScreen(f'{img}btn_ok_desmarcado.png', confidence=0.95)

    if btn_ok !=None:
        c(btn_ok.x,btn_ok.y)
    else:
        logging.info('  Erro ao processa Variavel btn_ok')
    print('    Esperando carregar infomaçoes')

    p.sleep(3)
    sem_dados = p.locateCenterOnScreen(f'{img}sem_dados_consulta.png', confidence=0.95)
    btn_ok = p.locateCenterOnScreen(f'{img}ok100.png', confidence=0.95)
    if sem_dados != None:
        print('    Titulo nãO Encontrado')
        logging.info('  Titulo nãO Encontrado')
        p.sleep(1)
        c(btn_ok.x,btn_ok.y)
        cancela = p.locateCenterOnScreen(f'{img}cancelar.png', confidence=0.95)
        if cancela !=None:
            c(cancela.x, cancela.y)
        p.sleep(0.5)
        fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        while fechar != None:
                c(fechar.x,fechar.y)
                p.sleep(1)
                fechar = p.locateCenterOnScreen('C:/RPA/arquivos/images/fechar12.png', confidence=0.95)
        
        return False
    else:
        print(" Titulo encontrado")
        todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
        while todos !=None:
            print("  carregando informaçoes!!!!")
            p.sleep(0.5)
            todos = p.locateCenterOnScreen(f'{img}todos_consulta_titulos.png', confidence=0.95)
            p.sleep(1)
        p.press('Enter')
        p.sleep(1)
      

        p.sleep(1)
        

        
        return True
    

if __name__ == '__main__':
   
    
    pesquisar_titulo_comissao_spf('','93401639315')
