from selenium import webdriver

navegador = webdriver.Edge()

navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element_by_xpath('//[@id="owl-destaques"]/div[1]/div/div[4]/div/a/img').click()
navegador.find_element_by_xpath('//[@id="D6OClzrGtocpQRELDA4Klw=="]').click()