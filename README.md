# Automação Web com Selenium 

O Automação Selenium é um script Python que utiliza o Selenium WebDriver para automatizar ações no navegador Google Chrome, como acesso a sites, preenchimento de formulários e interação com elementos dinâmicos em páginas web. O objetivo é demonstrar o uso prático de automação com Python em sites reais.

## ✨ Funcionalidades Principais

Abertura Automática do Navegador: Inicializa o Chrome e acessa automaticamente a URL definida.

Navegação entre Páginas: O script transita entre páginas diferentes dentro do mesmo navegador.

Interação com Elementos HTML: Localiza botões, links e campos de formulário por id e class name.

Preenchimento de Formulário: Insere automaticamente nome, e-mail e telefone nos campos da página.

Espera Dinâmica: Utiliza WebDriverWait e expected_conditions para aguardar elementos estarem prontos para interação.

Rolagem de Página (scroll): Garante que o botão de envio esteja visível antes de clicar.

Execução Segura: Implementa esperas e boas práticas para evitar erros de sincronização.

## 🚀 Tecnologias Utilizadas

Linguagem: `Python 3.8+`

Framework de Automação: `Selenium WebDriver`

Navegador: `Google Chrome`

Gerenciador de Driver: `WebDriver ` 

### Bibliotecas auxiliares:

`selenium.webdriver` — controle do navegador

`expected_conditions` — condições de espera

`time` — pausas temporárias (em segundos)
