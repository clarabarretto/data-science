from bs4 import BeautifulSoup
import datetime
import sys
import os
import  glob

# Leia o HTML do arquivo
# with open(html_file_path, "r", encoding="utf-8") as file:
#     html = file.read()

meses = {
    "janeiro": "01",
    "fevereiro": "02",
    "março": "03",
    "abril": "04",
    "maio": "05",
    "junho": "06",
    "julho": "07",
    "agosto": "08",
    "setembro": "09",
    "outubro": "10",
    "novembro": "11",
    "dezembro": "12"
}

data = datetime.datetime.now()

class Beautifulsoup:

    # Parseie o HTML usando BeautifulSoup
    def __init__(self, html, checkin, checkout):
        self.run(html, checkin, checkout)

    def run(self, html, checkin, checkout):

        resultado = []

        for i in range(len(html)):
            self.soup = BeautifulSoup(html[i], "html.parser")
            resultado.append(list(self.extract(self.soup, checkin[i], checkout[i])))

        # Caminho do arquivo CSV
        output_csv_path = "resultado.csv"

        # Abra o arquivo para escrita
        with open(output_csv_path, "w", encoding="utf-8") as file:
            # Escreva os dados
            file.write("hotel,cidade,preço,checkin,checkout,dist_centro,dist_praia,avaliacao,qtnd_avaliacoes,data_extracao\n")

            for itens in resultado:
                for item in itens:
                    file.write(
                        f"{item['Hotel']},{item['Cidade']},{item['Preço']},{item['Checkin']},{item['Checkout']},{item['Dist_centro']},{item['Dist_praia']},{item['Avaliação']},{item["Num_de_avaliacoes"]},{item['Data_extracao']}\n"
                    )

    def extract(self, soup, checkin, checkout):
        # Encontre os elementos desejados e extraia informações
        for hotel in soup.find_all(
            "div",
            class_="c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 c6710787a4",
        ):
            try:
                list_check = []
                nome = hotel.find("div", class_="f6431b446c a15b38c233").text.replace(
                    ",", ""
                )
                preco = hotel.find(
                    "span", class_="f6431b446c fbfd7c1165 e84eb96b1f"
                ).text.replace("R$", "").replace('.', '')
                distance_centro = hotel.find("span", attrs={"data-testid": "distance"})

                if distance_centro:
                    distance_centro = distance_centro.text.replace(",", ".").split(' km')
                    if len(distance_centro) > 1:
                        distance_centro = float(distance_centro[0])
                    else:
                        distance_centro = float(f'0.{distance_centro[0].split(" m")[0]}')

                distance_praia = hotel.find("span", class_="abf093bdfe b058f54b9a")

                if distance_praia:
                    distance_praia = distance_praia.text.replace(",", ".").split(' km')
                    if len(distance_praia) > 1:
                        distance_praia = float(distance_praia[0])
                    elif distance_praia[0] == "Beira-mar":
                        distance_praia = float(0)
                    else:
                        distance_praia = f'{distance_praia[0].split(" m")[0].replace('.', '')}'
                        if distance_praia != 1.0:
                            distance_praia = float(f'0.{distance_praia}')
                        else:
                            distance_praia = float(distance_praia)

                cidade = soup.find("h1", class_="af8fbdf136 d5f78961c3")

                if cidade:
                    cidade = cidade.text.split(":", 1)[0]

                avaliacao = hotel.find("div", class_="a3b8729ab1 d86cee9b25")
                if avaliacao:
                    avaliacao = float(avaliacao.text.replace('"', '').replace(',', '.').split('Com nota ')[0])
                
                num_de_avaliacoes = hotel.find("div", class_="abf093bdfe f45d8e4c32 d935416c47")
                if num_de_avaliacoes:
                    num_de_avaliacoes = int(num_de_avaliacoes.text.split(' ', 1)[0].replace('.', ''))

                # for check in soup.find_all("span", class_="a8887b152e"):
                #     list_check.append(check.text)

                # checkin = list_check[0]

                # if checkin:
                #     checkin = checkin.split(", ")[1].split(" de ")
                #     dia = checkin[0].replace("º", "")
                #     mes = meses[checkin[1]]
                #     ano = checkin[2]
                #     checkin = f'{ano}-{mes}-{dia}'
                
                # checkout = list_check[1]
                # if checkout:
                #     checkout = checkout.split(", ")[1].split(" de ")
                #     dia = checkout[0]
                #     mes = meses[checkout[1]]
                #     ano = checkout[2]
                #     checkout = f'{ano}-{mes}-{dia}'
                
                yield {
                    "Hotel": nome,
                    "Preço": int(preco),
                    "Cidade": cidade,
                    "Checkin": checkin,
                    "Checkout": checkout,
                    "Dist_centro": distance_centro,
                    "Dist_praia": distance_praia,
                    "Avaliação": avaliacao,
                    "Num_de_avaliacoes": num_de_avaliacoes,
                    "Data_extracao": f"{data.year}-{data.month}-{data.day}"
                }

            except NameError as e:
                print(e)


# Lista para armazenar os conteúdos dos arquivos HTML
# html_contents = []
# directory = 'c:/Users/extre/OneDrive/Documentos/ciencia de dados/selenium-extraction/html'

# # Padrão para encontrar todos os arquivos HTML na pasta especificada
# pattern = os.path.join(directory, 'page_2024-06-01_Recife.html')
# print(pattern)

# # Iterar sobre todos os arquivos HTML encontrados
# for html_file in glob.glob(pattern):
#     with open(html_file, 'r', encoding='utf-8') as file:
#         # Ler o conteúdo do arquivo e adicionar à lista
#         html_contents.append(file.read())

# soup = Beautifulsoup(html_contents, 0, 0)