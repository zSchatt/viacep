from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

def confirma_e_busca(cep):

    # ENDEREÇO VIACEP    
    url = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    end_dados = url.json()

    # MOSTRANDO AS INFORMAÇÕES DO CEP
    print('\nDESEJA VER AS INFORMAÇÕES COLETADAS DESTE CEP?')
    comando = int(input('1. SIM\n2. NÃO\nDIGITE AQUI: '))
    if comando == 1:
        print('\nAS INFORMAÇÕES DO CEP {} SÃO:'.format(end_dados['cep']))
        print('\nSIGLA DO ESTADO: {}'.format(end_dados['uf']))
        print('NOME DA CIDADE: {}'.format(end_dados['localidade']))
        print('NOME DO BAIRRO: {}'.format(end_dados['bairro']))
        print('NOME DA RUA: {}'.format(end_dados['logradouro']))
        print('NÚMERO IBGE: {}'.format(end_dados['ibge']))
        print('DDD: {}'.format(end_dados['ddd']))
        print('SIAFI: {}'.format(end_dados['siafi']))

    # BUSCANDO A ÁREA DA CIDADE
    driver.get("https://www.google.com/")
    time.sleep(1.5)
    pesquisa = driver.find_element(By.TAG_NAME, 'input')
    pesquisa.send_keys('Cidade IBGE ', end_dados['localidade'])
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1.5)
    driver.find_elements(By.CSS_SELECTOR, 'h3.LC20lb.DKV0Md')[1].click()
    time.sleep(1.5)
    a_cid = driver.find_elements(By.TAG_NAME, 'p')[9].text

    # MOSTRANDO A INFORMAÇÃO DA ÁREA 
    print('\nDESEJA SABER A SOMA DOS ALGARISMOS DA ÁREA DA CIDADE?')
    saber_algarismos = int(input('1. SIM\n2. NÃO\nDIGITE AQUI: '))
    if saber_algarismos == 1:
        soma = int(a_cid[0]) + int(a_cid[1]) + int(a_cid[2]) + int(a_cid[4]) + int(a_cid[5]) + int(a_cid[6])
        print(f'\nA SOMA DOS ALGARISMOS É IGUAL A {soma}')

    elif saber_algarismos == 2:
        print('\nDESLIGANDO PROGRAMA...')
        exit()
    else:
        print('\nCOMANDO NÃO IDENTIFICADO.')


def voltar_programa():
    ent_cep = input("\nDIGITE O SEU CEP: ")

    # VERIFICANDO SE A QUANTIDADE DE NÚMEROS PARA O CEP ESTÁ CERTA
    while len(ent_cep) != 8:     
        print('\nNÃO FOI POSSÍVEL IDENTIFICAR.')
        o_cep=int(input('\nDESEJA BUSCAR OUTRO CEP?\n1. SIM\n2. NÃO\nDIGITE AQUI: '))
        if o_cep == 1:
            voltar_programa()
        elif o_cep == 2:
            print('\nDESLIGANDO PROGRAMA...')
            exit()
        else:
            print('')
                
    url = requests.get('http://viacep.com.br/ws/{}/json/'.format(ent_cep))
    end_dados = url.json()

    # VERIFICANDO SE O CEP É VÁLIDO
    if 'erro' in end_dados:
        print('\n{} É UM CEP INVÁLIDO'.format(ent_cep))
        o_cep=int(input('\nDESEJA BUSCAR OUTRO CEP?\n1. SIM\n2. NÃO\nDIGITE AQUI: '))
        if o_cep == 1:
            voltar_programa()
        elif o_cep == 2:
            print('\nDESLIGANDO PROGRAMA...')
            exit()

    # MOSTRANDO AS INFORMAÇÕES DO CEP
    print('\nDESEJA VER AS INFORMAÇÕES COLETADAS DESTE CEP?')
    comando = int(input('1. SIM\n2. NÃO\nDIGITE AQUI: '))
    if comando == 1:
        print('AS INFORMAÇÕES DO CEP {} SÃO:'.format(end_dados['cep']))
        print('SIGLA DO ESTADO: {}'.format(end_dados['uf']))
        print('NOME DA CIDADE: {}'.format(end_dados['localidade']))
        print('NOME DO BAIRRO: {}'.format(end_dados['bairro']))
        print('NOME DA RUA: {}'.format(end_dados['logradouro']))
        print('NÚMERO IBGE: {}'.format(end_dados['ibge']))
        print('DDD: {}'.format(end_dados['ddd']))
        print('SIAFI: {}'.format(end_dados['siafi']))
        
    # BUSCANDO A ÁREA DA CIDADE
    driver.get("https://www.google.com/")
    time.sleep(1.5)
    pesquisa = driver.find_element(By.TAG_NAME, 'input')
    pesquisa.send_keys('Cidade IBGE ', end_dados['localidade'])
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1.5)
    driver.find_elements(By.CSS_SELECTOR, 'h3.LC20lb.DKV0Md')[1].click()
    time.sleep(1.5)
    a_cid = driver.find_elements(By.TAG_NAME, 'p')[9].text

    # MOSTRANDO A INFORMAÇÃO DA ÁREA 
    print('\nDESEJA SABER A SOMA DOS ALGARISMOS DA ÁREA DA CIDADE?')
    saber_algarismos = int(input('1. SIM\n2. NÃO\nDIGITE AQUI: '))
    if saber_algarismos == 1:
        soma = int(a_cid[0]) + int(a_cid[1]) + int(a_cid[2]) + int(a_cid[4]) + int(a_cid[5]) + int(a_cid[6])
        print(f'\nA SOMA DOS ALGARISMOS É IGUAL A {soma}')

    elif saber_algarismos == 2:
        print('\nDESLIGANDO PROGRAMA...')
        exit()
    else:
        print('\nCOMANDO NÃO IDENTIFICADO.')
