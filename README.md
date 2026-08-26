<h1 align="center">Fluxo encomendas internacionais</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=9cccf4&message=Python&color=grey&style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/static/v1?label=%20&labelColor=fcbe96&message=Jupyter&color=grey&style=for-the-badge&logo=jupyter&logoColor=black"/>
</p>

<p align="center">
  <a href="#motivacao">Motivação</a> •
  <a href="#inicio-rapido">Início Rápido</a> •
  <a href="#configuracao">Configuração</a> •
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#estrutura-do-projeto">Estrutura</a>
</p>

<p align="center">
Projeto para simplificar o acompanhamento de status de encomendas internacionais entre diferentes etapas: 'compra', 'importação', 'taxação' e 'entrega' sobre uma única interface.
</p>

---

<h2 id="motivacao">Motivação</h2>

Este projeto nasceu para facilitar meu acompanhamento de encomendas em diferentes proxies e lojas internacionais sem que eu precisasse ativamente me recordar do que comprei em cada lugar.

---

<h2 id="inicio-rapido">Início Rápido</h2>

### 1️⃣ Pré-requisitos

- [Python](https://www.python.org/downloads/) 3.10 ou superior
- Suporte a Jupyter Notebook no seu editor (ex: extensão [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) do [Visual Studio Code](https://code.visualstudio.com/))

### 2️⃣ Clonar o Projeto

Clone o repositório:

```bash
git clone https://github.com/NicolasChirazawa/fluxo-encomendas-internacionais.git
```

Ou baixe o arquivo `.zip` diretamente pelo GitHub.

### 3️⃣ Instalação de dependências

O projeto possui um arquivo `requirements.txt` na raiz contendo as dependências necessárias.

Execute:

```bash
pip install -r requirements.txt
```

---

<h2 id="configuracao">Configuração</h2>

Existem dois arquivos que são configuráveis no projeto.

- `src/application/configuration/configuration.json`
- `src/application/database/database.json`

<h3>configuration.json</h3>

```json
{
    "format": "dd/mm/yyyy",
    "separator": "/",
    "compilation": "full",
    "language": "pt-br"
}
```

- **format**: Formato que as datas do projeto devem respeitar. O separador definido em `separator` deve ser o mesmo usado aqui;
- **separator**: Separador utilizado para dar `split()` nas datas;
- **compilation**: Abas geradas no Excel — `simple` (abas individuais por etapa), `complete` (aba com dados de todas as etapas), `full` (ambas anteriores combinadas);
- **language**: A língua utilizada no Excel. Valores disponíveis: `pt-br` e `eng`;

<h3>database.json</h3>

```json
{
    "ZEN001": {
        "Nome_Figure": "Saya",
        "MFC_Link": "https://myfigurecollection.net/item/3054167",
        "Marca": "Good Smile Company",
        "Linha": "Nendoroid",
        "Escala": "Nendoroid",

        "Compra": {
            "Local_da_Compra": "Zenmarket",
            "Pais_Local": "Japao",
            "Data_do_Pagamento": "25/02/2026",
            "Metodo_Pagamento": "Nubank Credito",
            "Custos": {
                "Preco": "6651",
                "Taxa": "500"
            }
        },

        "Frete": {
            "Data_Limite_Pagamento": "09/09/2026",
            "Pais_Local": "Japao",
            "Data_do_Frete": "19/08/2026",
            "Metodo_Pagamento": "Nubank Credito",
            "Custos": {
                "Preco": "2553",
                "Taxa": "0"
            }
        },

        "Imposto": {
            "Data_Limite_Pagamento": "09/09/2026",
            "Data_do_Imposto": "03/09/2026",
            "Preco_Imposto": "200"
        },

        "Entrega": {
            "Data_da_Entrega": "09/09/2026"
        }
    }
}
```

---

<h2 id="funcionalidades">Funcionalidades</h2>

- Controle por etapas: Criação de diversos modelos de dados baseado no fluxo de uma encomenda;
- Exportação de Excel: Geração de um Excel com base no tipo de compilação escolhida pelo usuário;
- Tipos de compilação: Usuário pode escolher quais abas serão geradas no Excel conforme o seu interesse;
- Mais de uma língua: O sistema fornece a geração do Excel com colunas em diferentes linguagens;
- Conversão de moeda: É feito a conversão de moedas com base nos dados fornecidos pela Frankfurter API;

<h2 id="estrutura-do-projeto">Estrutura</h2>

O projeto está dividido em módulos:

- **Product**          → Responsável pela construção dos dados do produto;
- **Purchase**         → Responsável pela construção dos dados de compra;
- **Shipping**         → Responsável pela construção dos dados do envio;
- **Tax**              → Responsável pela construção dos dados de taxas;
- **Delivery**         → Responsável pela construção dos dados de entrega;
- **Summarize**        → Responsável pelo resumo do status da encomenda com base nos dados fornecidos;
- **Compilation Data** → Responsável pela compilação dos dados gerais em blocos de objetos;
- **Create Tab**       → Responsável pela criação de modelos de aba de Excel;
- **Create Report**    → Responsável pela criação do Excel;

## Licença

Não especificada.

## Contribuição

PRs e sugestões são bem-vindos — abra uma issue para discutir antes de mudanças maiores.

<h2>Dúvidas</h2>

Caso haja qualquer dúvida, pode abrir uma issue no projeto por [aqui](https://github.com/NicolasChirazawa/fluxo-encomendas-internacionais/issues/new).
