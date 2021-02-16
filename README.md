### Introdução:

Muitos desenvolvedores Python já ouviram falar sobre o termo ChatBot e automação de serviços de mensagens, na verdade para um bom uso de ChatBots eu recomendo utilização de APIs do mensageiro que se deseja utilizar, porém, fazendo uso de algumas bibliotecas Python é possível criar um mensageiro automático para envio de mensagens em escala.

## Principais Ferramentas:

Selenium: O selenium na verdade é uma biblioteca simples e que geralmente é utilizada em testes funcionais e de aceitação em sistemas Web. Vamos utiliza-lo para carregar a página de acesso web do whatsapp e enviar mensagens utilizando o próprio padrão de comando da biblioteca.
webdriver_manager: Para que o selenium carregue o nevagador é necessário baixar os drivers do mesmo, na documentação isso estará mais explicado, o webdriver_manager é um pacote python para encontrar e baixar o driver correto de acordo com o navegador e a versão do navegador instalado em sua máquina.

## Vantagens:

Não é necessário nenhum serviço externo a sua estação de trabalho, e isso não gera custo, como mencionei, para utilização de boas práticas na criação de chatbots é necessário fazer uso de APIs previamente disponibilizadas pelos serviços de mensagens, esses serviços tem um custo, mesmo para aplicações em modo de teste e desenvolvimento.
Com poucas linhas de código um celular com o whatsapp instalado e internet é possível criar um padrão de mensagens e contatos para envio das mensagens.

## Desvantagens: 

É um pouco mais complicado fazer o controle de entrada e saída, e também de interação de uma inteligencia artificial para respostas automáticas e funções úteis.

## Criando Chatbot

É necessário ter o Python 3 instalado em seu computador, em sistemas Linux nesse caso estarei utilizando o Ubuntu 20.10 o python já vem instalado por padrão em sua versão 3. Em arquitetura Windows ou MAC é necessário baixar pelo seguinte link: https://www.python.org/downloads/
Baixar a biblioteca selenium:

```pip install selenium```

3. Baixar a biblioteca webdriver_manager:

```pip install webdriver_manager```

4. Criar a aplicação: chatbot.py

```from selenium import webdriver
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
```
5. Iniciar a aplicação:

```python3 chatbot.py```

## Conclusão:

O artigo abordou de forma rápida o desenvolvimento de um chatbot funcional com a intenção de disparos de mensagem em massa para uma determinada lista de contatos, também da uma ideia de como criar testes de aceitação com a biblioteca selenium.

## Referencias

https://selenium-python.readthedocs.io/

https://pypi.org/project/webdriver-manager/

https://www.ufsm.br/pet/sistemas-de-informacao/2018/09/15/automatizacao-e-testes-com-selenium/

