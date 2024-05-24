import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from beautifulSoup import Beautifulsoup

# Função para gerar datas de check-in e check-out
def generate_check_in_out_dates():
    dates = []

    #Processar meses de janeiro a maio para o ano de 2025
    for month in range(1, 7):
        year = 2025
        start_date = pd.Timestamp(year=year, month=month, day=1)
        end_date = start_date + pd.offsets.MonthEnd(0)
        date_range = pd.date_range(start_date, end_date, freq="7D")

        for check_in in date_range:
            check_out = check_in + pd.Timedelta(days=7)
            if check_out.month == month:
                if check_in == pd.Timestamp(year=2025, month=5, day=22):
                    dates.append(
                        (check_in.strftime("%Y-%m-%d"), check_out.strftime("%Y-%m-%d"))
                    )

    # Processar meses de junho a dezembro para o ano de 2024
    for month in range(6, 13):
        year = 2024
        start_date = pd.Timestamp(year=year, month=month, day=1)
        end_date = start_date + pd.offsets.MonthEnd(0)
        date_range = pd.date_range(start_date, end_date, freq="7D")

        for check_in in date_range:
            check_out = check_in + pd.Timedelta(days=7)
            if check_out.month == month:
                if check_in == pd.Timestamp(year=2025, month=1, day=1):
                    dates.append(
                        (check_in.strftime("%Y-%m-%d"), check_out.strftime("%Y-%m-%d"))
                    )

    return dates

# Inicialize o driver do Chrome
driver = webdriver.Chrome()

cidades = [
    # "Recife",
    # "Sydney",
    # "Atenas",
    # "Paris",
    # "Nova York",
    # "Tokyo",
    # "Cidade do Cabo",
    "Lisboa"
]
cidades_destid = [
    # "-665520", 
    # "-1603135",
    # "-814876",
    # "-1456928",
    # "20088325",
    # "-246227",
    # "-1217214",
    "-2167973"
]

# Gerar datas de check-in e check-out
checkin_checkout_dates = generate_check_in_out_dates()

html = []
checkin_data = []
checkout_data = []

for i in range(len(cidades)):
    for checkin, checkout in checkin_checkout_dates:
        # Abra a página que deseja raspar
        driver.get(
            f"https://www.booking.com/searchresults.pt-br.html?label=gx1-br-booking-booking-sd-nptd&sid=a77533c6921c5bf28c165cc6b7a6d38d&aid=348858&ss=Recife%2C+Pernambuco%2C+Brasil&ssne=Arcoverde&ssne_untouched=Arcoverde&lang=pt-br&src=searchresults&dest_id={cidades_destid[i]}&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=xb&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=79a11d850e0f0110&ac_meta=GhA3OWExMWQ4NTBlMGYwMTEwIAAoATICeGI6BlJlY2lmZUAASgBQAA%3D%3D&checkin={checkin}&checkout={checkout}&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
        )

        # Espere alguns segundos para garantir que a página seja carregada completamente
        time.sleep(7)

        try:
            button = driver.find_element(
                By.XPATH, '//button[@aria-label="Ignorar informações de login."]'
            )
            button.click()
        except:
            pass

        # Rolar a página e carregar mais resultados
        previous_height = driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # Role a página para baixo
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            try:
                button = driver.find_element(
                    By.XPATH,
                    '//button[@class="a83ed08757 c21c56c305 bf0537ecb5 f671049264 deab83296e af7297d90d"]',
                )
                button.click()
                time.sleep(2)
            except:
                pass

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == previous_height:
                break
            previous_height = new_height

        # Capture o HTML após rolar para baixo várias vezes
        html.append(driver.page_source)
        file_name = f'selenium-extraction/html/page_{checkin}_{cidades[i]}.html'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html[-1])
        checkin_data.append(checkin)
        checkout_data.append(checkout)

# Feche o navegador
driver.quit()

# soup = Beautifulsoup(html, checkin_data, checkout_data)