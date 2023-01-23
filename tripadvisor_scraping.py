from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from write_xlsx import write_headers, write_reviews, write_services, write_comments, save_file
from inputs import input_url, input_name_file, input_num_comments
from messages import loading, fail, success
from time import sleep


def initial_setup(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print(loading("Iniciando..."))

    try:
        global driver
        driver = webdriver.Chrome(options=options)
        driver.get(url)
    except:
        print(fail("Erro ao iniciar o navegador, certifique-se\
 de que possui o Chrome instalado no computador"))
        sleep(3)
        raise SystemExit

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
        cookie = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie.click()
    except TimeoutException:
        print(fail("Tempo limite excedido, tente novamente"))
        sleep(3)
        raise SystemExit


def get_inputs():
    url = input_url()
    name_file = input_name_file()
    num_comments = input_num_comments()

    return url, name_file, num_comments


def get_comments(num_comments):
    comments = []

    while len(comments) < num_comments:
        try:
            comments_section = driver.find_elements(By.CLASS_NAME, "YibKl")
        except:
            print(fail("Erro ao coletar comentários, certifique-se de que a URL é de um estabelecimento"))
            sleep(3)
            raise SystemExit

        for comment in comments_section:
            print(loading(f"Coletando comentários... {len(comments) + 1} de {num_comments}"))

            name = comment.find_element(By.CLASS_NAME, "ui_header_link").get_attribute("innerText")
            title = comment.find_element(By.CLASS_NAME, "KgQgP").get_attribute("innerText")
            review = comment.find_element(By.CLASS_NAME, "QewHA").get_attribute("innerText")
            date = comment.find_element(By.CLASS_NAME, "teHYY").get_attribute("innerText")

            comments.append({
                "name": name,
                "title": title,
                "review": review,
                "date": date
            })

            if len(comments) == num_comments:
                break

        try:
            next_page = driver.find_element(By.CLASS_NAME, "ui_button.nav.next.primary")
            next_page.click()
            sleep(3)
        except:
            break
    
    if num_comments:
        write_comments(comments)


def get_services():
    try:
        services = driver.find_elements(By.CSS_SELECTOR, ".fBoia .yplav")
        write_services(services)

        close_btn = driver.find_element(By.CLASS_NAME, "zPIck")
        close_btn.click()
    except:
        print(fail("Erro ao coletar os serviços, certifique-se de que a URL é de um estabelecimento"))
        sleep(3)
        raise SystemExit

    sleep(3)


def get_reviews():
    print(loading("Coletando avaliações..."))

    try:
        title = driver.find_element(By.CLASS_NAME, "jvqAy").get_attribute("innerText")
        score = driver.find_element(By.CLASS_NAME, "uwJeR").get_attribute("innerText")
        avaliacoes = driver.find_element(By.CLASS_NAME, "hkxYU").get_attribute("innerText")
    except:
        print(fail("Erro ao coletar as avaliações, certifique-se de que a URL é de um estabelecimento"))
        sleep(3)
        raise SystemExit

    sleep(2)
    
    print(loading("Coletando serviços..."))

    try:
        more_services = driver.find_element(By.CLASS_NAME, "Wmdmb")
        more_services.click()
    except:
        print(fail("Erro ao coletar os serviços, certifique-se de que a URL é de um estabelecimento"))
        sleep(3)
        raise SystemExit

    sleep(2)

    write_reviews(title, score, avaliacoes)

def close(name_file):
    again = input("Deseja fazer outro scraping? (s/n): ")

    if again == "s":
        main()
    elif again == "n":
        raise SystemExit
    else:
        print(fail("Opção inválida"))
        close(name_file)

def main():
    url, name_file, num_comments = get_inputs()
    initial_setup(url)

    write_headers(num_comments)
    get_reviews()
    get_services()
    get_comments(num_comments)

    save_file(name_file)
    print(loading("Finalizando..."))

    driver.quit()
    print(success(f"Arquivo gerado com sucesso no caminho ./data/{name_file}.xls!"))

    close(name_file)


if __name__ == "__main__":
    main()