import requests as rq
from bs4 import BeautifulSoup as BS
import json
from openpyxl import load_workbook
from datetime import datetime
import time
import sys

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = 'https://www.kabum.com.br/produto/955187/notebook-lenovo-ideapad-slim-3-amd-ryzen-7-7735hs-16gb-ram-amd-radeon-graphics-ssd-512gb-15-3-wuxga-linux-luna-grey-83mms00000'

ultimo_dia = None

#Loop que verifica se o dia ja passou para criar a nova linha com o preço mais atual do produto
while True:
    semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    hoje = datetime.now()
    dia_sem = hoje.weekday()
    diac = hoje.strftime('%d/%m/%Y')
    
    if diac != ultimo_dia:
        try:
            req = rq.get(url, headers=headers)
        except Exception as e:
            print(f'Erro de conexão: {e}')
            sys.exit(1)

        if req.status_code != 200:
            print(f'Erro na requisição: {req.status_code}')
            sys.exit(1)
        
        soup = json.loads(BS(req.text, 'html.parser').find('script', type="application/ld+json").string)['offers']
        
        preco = f'R$ {soup["price"]}'
        
        wb = load_workbook('base_monitor.xlsx')
        ws = wb.active
        
        ws.append([f'{diac}', preco, f'{semana[dia_sem]}'])
        
        wb.save('base_monitor.xlsx')
        ultimo_dia = diac
    time.sleep(3600)