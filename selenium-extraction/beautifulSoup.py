from bs4 import BeautifulSoup
import sys

# Leia o HTML do arquivo
# with open(html_file_path, "r", encoding="utf-8") as file:
#     html = file.read()


class Beautifulsoup:

    # Parseie o HTML usando BeautifulSoup
    def __init__(self, html, checkin, checkout):
        self.run(html, checkin, checkout)

    def run(self, html, checkin, checkout):
        self.checkin = checkin
        self.checkout = checkout

        resultado = []

        for i in html:
            self.soup = BeautifulSoup(i, "html.parser")
            resultado.append(list(self.extract(self.soup)))

        # Caminho do arquivo CSV
        output_csv_path = "resultado.csv"

        # Abra o arquivo para escrita
        with open(output_csv_path, "w", encoding="utf-8") as file:
            # Escreva os dados
            file.write("Hotel,Cidade,Preço,Checkin,Checkout,Dist_centro,Dist_praia\n")

            for itens in resultado:
                for item in itens:
                    file.write(
                        f"{item['Hotel']},{item['Cidade']},{item['Preço']},{item['Checkin']},{item['Checkout']},{item['Dist_centro']},{item['Dist_praia']}\n"
                    )

    def extract(self, soup):

        # Encontre os elementos desejados e extraia informações
        for hotel in soup.find_all(
            "div",
            class_="c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 c6710787a4",
        ):
            try:
                nome = hotel.find("div", class_="f6431b446c a15b38c233").text.replace(
                    ",", ""
                )
                preco = hotel.find(
                    "span", class_="f6431b446c fbfd7c1165 e84eb96b1f"
                ).text.replace("R$", "")
                distance_centro = hotel.find("span", attrs={"data-testid": "distance"})

                if distance_centro:
                    distance_centro = distance_centro.text.replace(",", ".").replace(
                        " km do centro", ""
                    )

                distance_praia = hotel.find("span", class_="abf093bdfe b058f54b9a")

                if distance_praia:
                    distance_praia = distance_praia.text.replace(
                        " m da praia", ""
                    ).replace(",", ".")

                cidade = hotel.find("h1", class_="af8fbdf136 d5f78961c3")

                if cidade:
                    cidade = cidade.text.split(":", 1)[0]
                yield {
                    "Hotel": nome,
                    "Preço": float(preco),
                    "Cidade": cidade,
                    "Checkin": self.checkin,
                    "Checkout": self.checkout,
                    "Dist_centro": distance_centro,
                    "Dist_praia": distance_praia,
                }

            except NameError as e:
                print(e)
