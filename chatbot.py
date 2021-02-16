from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "<Mensagens>"
        self.grupos = ["<lista de grupos>"]
        opitions = webdriver.ChromeOptions()
        opitions.add_argument('lang=pt-br')
        # Essa linha faz o ChromeDriverManager baixar o driver correto para a versão do chrome instalada
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def EnviarMensagens(self):
        # abre o navegador no link do whatsapp
        self.driver.get('http://web.whatsapp.com')
        time.sleep(10)
        for grupo in self.grupos:    
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(2)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(2)
            chat_box.click()
            time.sleep(2)
            chat_box.send_keys(self.mensagem)
            chat_box.send_keys(Keys.RETURN)
            time.sleep(2)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(2)
            botao_enviar.click()
            time.sleep(2)
        self.driver.quit()

bot = WhatsappBot()
bot.EnviarMensagens()