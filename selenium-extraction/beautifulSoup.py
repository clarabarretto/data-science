from bs4 import BeautifulSoup
import sys

# Leia o HTML do arquivo
# with open(html_file_path, "r", encoding="utf-8") as file:
#     html = file.read()
class Beautifulsoup():
# Parseie o HTML usando BeautifulSoup
    def __init__(self, html, checkin, checkout):
        self.soup = BeautifulSoup(html, "html.parser")
        self.checkin = checkin
        self.checkout = checkout
        self.run()

    def extract(self, soup):
    # Encontre os elementos desejados e extraia informações
        for hotel in soup.find_all("div", class_="c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 c6710787a4"):
            try:
                nome = hotel.find("div", class_="f6431b446c a15b38c233").text.replace(',', '')
                preco = hotel.find("span", class_="f6431b446c fbfd7c1165 e84eb96b1f").text.replace('R$', '')
                yield {
                    "Hotel": nome,
                    "Preço": float(preco),
                    "Checkin": self.checkin,
                    "Checkout": self.checkout,
                }
            except:
                pass
    def run(self):
        resultado = list(self.extract(self.soup))

        # Caminho do arquivo CSV
        output_csv_path = "resultado.csv"

        # Abra o arquivo para escrita
        with open(output_csv_path, "w", encoding="utf-8") as file:
        # Escreva os dados
            file.write("Hotel,Preço,Checkin,Checkout\n")

            for item in resultado:
                file.write(f"{item['Hotel']},{item['Preço']},{item['Checkin']},{item['Checkout']}\n")