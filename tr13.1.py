from selenium import webdriver
import random

def GeraAleat(qtdd_caract):
    conj = 'abcdefghijklmnopqrstuvwxyz0123456789ghijklmno55544dd5pqrstuv'
    result = ''
    for x in range(qtdd_caract):
        a = random.choice(conj)
        result += a
    return result

while True:
    try:
        driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
        break
    except:
        loc_driver = input('o arquivo chromedriver.exe não foi encontrado. cole a localização do arquivo: ')
        driver = webdriver.Chrome(executable_path='{}'.format(loc_driver))
        break





driver.implicitly_wait(5)

aleat = 'abcdefghijklmnopqrstuvwxyz0123456789ghijklmno55544dd5pqrstuv'

id_nome = 'id_fullname'
id_email = 'email--1'
id_senha = 'password'
id_bt = 'submit-id-submit'
nome = '{} {}'.format(GeraAleat(10),GeraAleat(10))
email = '{}@gmail.com'.format(GeraAleat(22))
senha= 'vfkvfdlkvldvld'
driver.get('https://www.udemy.com/join/signup-popup/?locale=pt_BR&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F')
input_nome = driver.find_element_by_id(id_nome)
input_email = driver.find_element_by_id(id_email)
input_senha = driver.find_element_by_id(id_senha)
bt = driver.find_element_by_id(id_bt)
input_nome.send_keys(nome)
input_email.send_keys(email)
input_senha.send_keys(senha)
bt.click()
