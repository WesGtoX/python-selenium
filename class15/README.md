# Aula 15 - Selenium Docker

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2315.pdf)

## Docker?

- Fazer download para a máquina da imagem do Docker Hub:
```bash
docker pull selenium/standalone-firefox-debug:3.141.59
```

- Rodar imagem do selenium debug versão 3.141.59:
```bash
docker run -d -p 4444:4444 -p 5900:5900 selenium/standalone-firefox-debug:3.141.59
```


## Selenium grid

- Criar conexão para conectar máquinas:
```bash
docker network create grid
```

- Rodar imagem do docker hub:
```bash
docker run -d -p 4444:4444 --net grid --name selenium-hub selenium/hub:3.141.59
```

- Rodar imagem do docker node para um navegador específico:
```bash
docker run -d --net grid -e HUB_HOST=selenium-hub selenium/node-firefox:3.141.59
docker run -d --net grid -e HUB_HOST=selenium-hub selenium/node-chrome:3.141.59
docker run -d --net grid -e HUB_HOST=selenium-hub selenium/node-opera:3.141.59
```

- Rodar imagem co cinco instâncias de node.
```bash
docker run -d --net grid -e HUB_HOST=selenium-hub -e NODE_MAX_INSTANCES=5 selenium/node-chrome:3.141.59
```


## Docker compose com selenium grid
`docker-compose.yml`
```ỳaml
version: '3'

services:
    selenium-hub:
        image: selenium/hub:3.141.59
        container_name: selenium-hub
        ports:
            - "4444:4444"

    chrome:
        image: selenium/node-chrome:3.141.59
        environment:
            - HUB_HOST=selenium-hub
            - NODE_MAX_INSTANCES=5

    firefox:
        image: selenium/node-firefox:3.141.59
        environment:
            - HUB_HOST=selenium-hub

    opera:
        image: selenium/node-opera:3.141.59
        environment:
            - HUB_HOST=selenium-hub
```

- Subir o container de com as configurações do arquivo `docker-compose.yml`:
```bash
docker-compose up --build
```

- Escalar uma imagem através do comando de subir o container:
```bash
docker-compose up scale chrome=3
docker-compose up scale firefox=5
```


## Nem tudo são flores!

### Problemas

- Consumo do grid web:
  - Cada container exige ~150MB para ficar em modo de espera
  - Um container conectado consome ~300MB
  - \+ xxxMB da abertura da página

- Não é tolerante a falhas
- Não tem gerenciamento de usuários

```bash
docker-compose up scale firefox=50
```


## Selenoid

É um projeto iniciado em 2017, pela Aerokube, que fornece uma poderosa implementação em Go do Selenium hub original. Com as mesmas chamadas, porém gerenciando os containers para você.

[Selenoid](https://aerokube.com/cm/latest/)

```bash
curl -s https://aerokube.com/cm/bash | bash && ./cm selenoid start --vnc
```

```python
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=ff_capabilities
)
```

Tem uma UI maneira e moderna

```bash
./cm selenoid-ui start
```

```python
from selenium import webdriver

        
capabilities = {
    "browserName": "firefox",
    "version": "80.0",
    "enableVNC": True,
    "enableVideo": False
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities
)
```


## Integração contínua

[GitLab CI](https://github.com/WesGtoX/python-selenium/tree/master/class15/class15_ci)
