# Aula 14 - Selenium Grid

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2314.pdf)

## Selenium Grid
O Selenium Grid eleva o WebDriver a outro nível, executando testes em muitas máquinas ao mesmo tempo, reduzindo o tempo necessário para testar em vários navegadores e sistemas operacionais

- Suporta vários navegadores, versões e sistemas operacionais
- Reduzir o tempo de execução.
- Paraleliza execuções.


## HUB

- [Selenium Server (Grid)](https://www.selenium.dev/downloads/)
- [Setting up your own grid](https://www.selenium.dev/documentation/en/grid/grid_3/setting_up_your_own_grid/)


### Deixando o hub disponível

```bash
java -jar ./selenium-server-standalone-3.141.59.jar -role hub
```


### Onde o server fica disponível?

- http://localhost:4444/

```python
from selenium.webdriver import Remote


capabilities = {
    'browserName': 'internet explorer'
}

browser = Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=capabilities
)
```


### Deixando o node disponível
```bash
java -jar ./selenium-server-standalone-3.141.59.jar -role node
```


### Capabilities para servir (básico essencial)
```json
{
	"capabilities": [
		{
			"browserName": "opera",
			"maxInstances": 5,
			"seleniumProtocol": "WebDriver"
		}
	],
	"port": 5555,
	"hub": "http://localhost:4444",
	"role": "node"
}
```


### Capabilities para servir (básico essencial)

- Arquivo de configurações: `node_config.json`

```bash
java -jar ./selenium-server-standalone-3.141.59.jar -role node-nodeConfig node_config.json
```


## Nem tudo são flores!

1. Não existe uma maneira programática de montar essa arquitetura.
   - Instalar o java
   - Baixar o selenium
   - Baixar os web drivers
   - Desempacotar os web drivers
   - Instalar todas as versões de browsers correspondentes

   Repetir operação em todos os nodes com SOs diferentes

2. Browsers sem foco

3. Custo para manter a infra

4. Não suporta bem mobile*
