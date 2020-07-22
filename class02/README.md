# Aula 2 - O que é Selenium

- [**SLIDE**](https://raw.githubusercontent.com/dunossauro/curso-python-selenium/master/slides/Aula%20%2302.pdf)

Biblioteca de software livre sob licença Apache 2.0 que te ajuda a resolver trabalhos manuais e repetitivos usando o browser.  

- Biblioteca: conjunto de ferramentas, feitas com código.  
- Software Livre: que garante com que sua liberdade seja protegida.  
- Apache 2.0: licença que garante a sua liberdade, a burocracia dos direitos autorais.  
- Browser: seu navegador de internet.  


## Selenium

O projeto selenium nasceu em 2004 com ideia de usar browsers como um usuário faria.  

- Simples e conciso.  
- É compatível com a maioria dos browsers.  
- É a recomendação da W3C (World Wide Web Consortium).  


## Para que serve o Selenium?

- Automação de testes de software.  
- Criação de bots.  
- Redução de trabalho "repetitivos".  
- *Raspar dados da internet*  


## História do Selenium

Selenium foi criado por Jason Huggins, em 2004 para testar uma aplicação de T&E criada em Python e Plone.  
Eles estavam tendo vários problemas por adicionar JavaScript nos projetos.  
"JavaScriptTestRunner"  
A ferramenta se tornou livre no mesmo ano da criação.  

Em 2006, no Japão, Shinya Kasatani, se interessou pelo projeto e criou o Selenium-IDE.  
Uma extensão para o Firefox.  

Simon Stwart, em 2007, nos laboratórios da ThoughtWorks. Melhorou a maneira de interação do Selenium com os navegadores.  
Assim nasceu a versão 2.0 e o Selenium WebDriver.  

Em 2008, Philippe Hanrigou, também na ThoughtWorks, criou o selenium GRID, maneira de paralelizar testes.  

Sobre a criação do selenium Jason Huggins, disse em uma entrevista:  
"Se existisse uma ferramenta para fazer isso [automatizar]. certamente não teria criado essa ferramenta."  
Depois alguns anos, foi criada uma ferramenta concorrente chamada "Mercury" [Mercúrio].  
Como piada eles apelidaram o "JavaScriptTestRunner" para Selenium. Pois Selenium [Selênio] é usado para curar envenenamento por mercúrio.  


## Selenium IDE

Selenium IDE é um plugin para o browser que permite que você faça a sua automação "gravando" o que faz o navegador e ele as reproduz.  
Com isso é possível automatizar tarefas mesmo sem entender programação.  


## Selenium WebDriver

É como um servidor que comunicara com o código e o browser.  


## Selenium GRID

Permite com que roda vários browsers ao mesmo tempo.  
Ele é dividido em duas coisas, HUB e Nodes.  
Serve para paralelizar testes e desacoplar quem de fato vai rodar o teste.  
Plus do GRID: Pode ser rodado em várias versões dos navegadores divergentes.  
