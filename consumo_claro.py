#!/bin/python3
from urllib.request import urlopen, Request
from re import findall

ua = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

req = Request('http://consumo.claro.com.br/crypto/redirect?target=informacao')
req.add_header('User-Agent', ua)
req = urlopen(req)
html = req.read().decode()

consumo = findall('<div class="col-xs-6 izqbold">(.*?)<', html)[1]
numero = findall('<div class="col-xs-6 izqbold">(.*?)<', html)[0]
fechamento = findall('\d{2}/\d{2}/\d{4}', html)[0]
plano = findall('<div class="col-xs-1 text-right">(.*?)<', html)[0]
porcentagem = findall('<span class="new-indicator">(.*?)<', html)[0]

ddd = numero[0:2]
n1 = numero[2:7]
n2 = numero[7:]

numero = '{} {}-{}'.format(ddd, n1, n2)

print('Número: {}\nConsumo: {}/{}\nPorcentagem de consumo: {}\nFechamento: {}'.format(numero, consumo, plano, porcentagem, fechamento))
