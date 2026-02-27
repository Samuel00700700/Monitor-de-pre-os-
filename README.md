# 📊 Monitor de Preços

Script Python que monitora diariamente o preço de um produto 
e salva o histórico automaticamente em Excel.

## 🛠️ Tecnologias
- Python 3
- Requests
- BeautifulSoup4
- OpenPyXL

## ⚙️ Como usar

1. Clone o repositório
2. Instale as dependências:
pip install -r requirements.txt
3. Abra o arquivo `base_monitor.xlsx` e configure o nome do produto na célula A1
4. Execute:
python monitor.py

> O script utiliza o `base_monitor.xlsx` como base e vai adicionando
> uma nova linha com o preço e a data a cada dia automaticamente.

## 📸 Resultado

![resultado](screenshot.png)
