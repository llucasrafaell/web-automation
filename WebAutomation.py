from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

search = navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search.click()
search.send_keys('previsão do tempo')
button_search = navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
button_search.click()

