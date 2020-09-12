# Rodando Selenium no GitLab CI

Vamos usar o [selenium-docker](https://github.com/SeleniumHQ/docker-selenium) que fornece as imagens oficiais do selenium no [docker hub](https://hub.docker.com/u/selenium).


## Selenium docker

O selenium docker disponibiliza várias imagens stadalone. Ou seja, podemos usar o selenium grid como um serviço isolado no gitlab-ci


## Arquivo gitlab-ci explicado

Caso você nunca tenha usado o gitlab-ci, aqui vão algumas explicações básicas sobre o arquivo:
```yml
default:                                                    # definição do padrão de todos os stages do build
  image: python:3.8.3                                       # imagem padrão para os stages

  before_script:                                            # rodará antes de todos os `scripts` em cada stage
    - pip install selenium

  services:                                                 # Serviço esterno que podera ser usado no stage
    - name: selenium/standalone-firefox:3.141.59-20200525   # imagem do selenium-docker presente no docker hub
      alias: grid                                           # grid é o nome que o host poderá ser acessado

stages:                                                     # lista de stages
  - test                                                    # nome de um stage

test:                                                       # stage
  script:                                                   # script que rodará na imagem default
    - python app/ci.py                                      # script que rodará na imagem
```


## License

Distributed under the MIT License. See [LICENSE](LICENSE.md) for more information.

---

Made with ♥ by [Wesley Mendes](https://wesleymendes.com.br/) :wave:
