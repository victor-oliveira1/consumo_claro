#!/bin/python3
#Copyright © 2018 Victor Oliveira <victor.oliveira@gmx.com>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.

import urllib.request
import html.parser
import argparse

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        argparse.HTMLParser.__init__(self)
        self.data = list()
    def handle_data(self, data):
        data = data.strip()
        if data:
            self.data.append(data)

args_parser = argparse.ArgumentParser()
args_parser.add_argument('-n',
                        help='Exibe apenas o número',
                        action='store_true',
                        default=False)
args_parser.add_argument('-P',
                        help='Exibe apenas o plano contratado',
                        action='store_true',
                        default=False)
args_parser.add_argument('-f',
                        help='Exibe apenas o fechamento do ciclo',
                        action='store_true',
                        default=False)
args_parser.add_argument('-c',
                        help='Exibe apenas o total de consumo (MB)',
                        action='store_true',
                        default=False)
args_parser.add_argument('-p',
                        help='Exibe apenas a porcentagem de consumo',
                        action='store_true',
                        default=False)
args = args_parser.parse_args()

ua = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

req = urllib.request.Request('http://consumo.claro.com.br/crypto/redirect?target=informacao')
req.add_header('User-Agent', ua)
try:
    req = urllib.request.urlopen(req)
except urllib.error.URLError:
    print('É necessário um modem da Claro')
    exit(1)
html = req.read().decode()

html_parser = MyHTMLParser()
html_parser.feed(html)

numero = html_parser.data[14]
plano = html_parser.data[16]
fechamento = html_parser.data[18]
consumo = html_parser.data[20]
porcentagem = html_parser.data[10]

if args.n:
    print(numero)
elif args.P:
    print(plano)
elif args.f:
    print(fechamento)
elif args.c:
    print(consumo)
elif args.p:
    print(porcentagem)
else:
    print('Número: {}\n\
Plano contratado: {}\n\
Fechamento do ciclo: {}\n\
Total de consumo: {}\n\
Porcentagem de consumo: {}'.format(
        numero, plano, fechamento,
        consumo, porcentagem))
