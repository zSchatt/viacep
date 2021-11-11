# VIACEP


## SOBRE O PROJETO
Este projeto tem a função de explicar as informações de uma cidade, 
cujo cep é fornecido pelo usuário, e dizer quantos algarismos possui a área da cidade.


## NECESSÁRIO PARA UTILIZAR
Para iniciar este projeto foram importadas algumas bibliotecas do python, são elas:
>>> requests

>>> selenium


## FUNCIONAMENTO DO PROJETO
Por primeira parte, o programa pergunta se o usuário deseja digitar um cep,
se o usuário digitar que sim, pede o cep e, a partir disso,
ele filtra para ver se o cep é válido em questões de: tamanho do cep e
se ele existe ou não. Após o usuário informar o cep, o programa abre
uma página web em modo headless e pesquisa o cep no site VIACEP e 
pegando todas as suas informações. Depois de coletar as informações, 
o programa pergunta ao usuário se ele deseja ver as informações e, se
a resposta for não, segue adiante e pesquisa a área da cidade
do cep informado e pergunta ao usuário se ele deseja saber a área. Então
o programa pergunta ao usuário se ele deseja obter informações de outro cep,
se a resposta for não, o programa chega ao fim.
