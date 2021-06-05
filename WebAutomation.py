from selenium import webdriver

navegador = webdriver.Firefox()
navegador.get("https://www.youtube.com/")

caixa_de_texto = navegador.find_element_by_xpath('//*[@id="search"]')
caixa_de_texto.send_keys('gtm iot robot arena control ')

botao_de_pesquisa = navegador.find_elements_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon')
botao_de_pesquisa.click()
