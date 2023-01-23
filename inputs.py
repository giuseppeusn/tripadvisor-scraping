from messages import fail
import os
import re


def input_url():
  while True:
    url = input("URL para scraping: ")

    if not url.startswith("https://www.tripadvisor.com.br/"):
      print(fail("URL inválida"))
    else:
      break
  
  return url


def input_name_file():
  while True:
    name_file = input("Nome do arquivo: ")

    if not len(name_file):
      print(fail("Informe um nome válido"))
    elif not re.match("^[A-Za-z0-9-_]*$", name_file):
      print(fail("Nome do arquivo não pode conter caracteres especiais"))
    elif os.path.isfile(f"./data/{name_file}.xls"):
      print(fail("Arquivo já existe"))
    else:
      break

  return name_file


def input_num_comments():
  while True:
    num_comments = input("Número de comentários: ")

    if not len(num_comments) or not num_comments.isdigit():
      print(fail("Informe um número válido"))
    else:
      break

  return int(num_comments)