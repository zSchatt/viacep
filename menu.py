from functions import voltar_programa, confirma_e_busca
from functions import driver
import requests

print('===================================')
print('================CEP================')
print('===================================')

while True:
    opcao = int(input('\nDESEJA DIGITAR UM CEP?\n1. SIM\n2. NÃO\nDIGITE AQUI: '))
    if opcao == 1:
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


        # ENDEREÇO VIACEP    
        url = requests.get('http://viacep.com.br/ws/{}/json/'.format(ent_cep))
        end_dados = url.json()

        # VERIFICANDO SE O CEP É VÁLIDO
        if 'erro' in end_dados:
            print('\n{} É UM CEP INVÁLIDO'.format(ent_cep))
            
            o_cep=int(input('\nDESEJA BUSCAR OUTRO CEP?\n1. SIM\n2. NÃO\nDIGITE AQUI: '))
            if o_cep == 1:
                driver.close()
                voltar_programa()
            elif o_cep == 2:
                print('\nDESLIGANDO PROGRAMA...')
                driver.close()
                exit()

        # CONFIRMA O CEP E BUSCA A ÁREA DA CIDADE 
        confirma_e_busca(ent_cep)
        
        # VOLTA O PROGRAMA DO INÍCIO
    elif opcao == 2:
        # SAINDO DO PROGRAMA
        print('\nDESLIGANDO PROGRAMA...')
        exit()
    else:
        print('\nCOMANDO NÃO IDENTIFICADO.')
