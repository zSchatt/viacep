from functions import voltar_programa, confirma_e_busca
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

print('===================================')
print('================CEP================')
print('===================================')

while True:
    opcao = int(input('\nDESEJA DIGITAR UM CEP?\n1. SIM\n2. NÃO\nDIGITE AQUI: '))
    if opcao == 1:
        ent_cep = input("\nDIGITE O SEU CEP: ")

        # VERIFICANDO SE A QUANTIDADE DE NÚMEROS PARA O CEP ESTÁ CERTA
        if len(ent_cep) != 8:
            print('\nQUANTIDADE DE NÚMEROS INVÁLIDA!')
             
            o_cep=int(input('\nDESEJA BUSCAR OUTRO CEP?\n1. SIM\n2. NÃO\nDIGITE AQUI: '))
            if o_cep == 1:
                voltar_programa()
            elif o_cep == 2:
                print('\nDESLIGANDO PROGRAMA...')
                break

        # ENDEREÇO VIACEP    
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
                break

        # CONFIRMA O CEP E BUSCA A ÁREA DA CIDADE 
        confirma_e_busca()
        
        # VOLTA O PROGRAMA DO INÍCIO
    elif opcao == 2:
        # SAINDO DO PROGRAMA
        print('\nDESLIGANDO PROGRAMA...')
        break
    else:
        print('\nCOMANDO NÃO IDENTIFICADO.')
