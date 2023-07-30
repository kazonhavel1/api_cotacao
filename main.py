import requests
import json

cotacaodesejada = input(f'Selecione a moeda desejada (Somente a Sigla EX: USD): ')

cotacoes = requests.get(f"https://economia.awesomeapi.com.br/json/last/{cotacaodesejada}-BRL")
cotacoes = cotacoes.json()


if 'CoinNotExists' in str(cotacoes):
    print ("Moeda não encontrada")
else:
    cotacaorecebida = float(cotacoes[f'{cotacaodesejada}BRL']['bid'])
    print (f'A cotação da moeda {cotacaodesejada} é R$ {round(cotacaorecebida,2)}.')