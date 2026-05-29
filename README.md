# Web Proxy

Um proxy web com painel de administração, desenvolvido em Python com Flask. Permite navegar em sites através do proxy com filtragem de conteúdo — bloqueando domínios e censurando palavras configuráveis — além de registrar um log de todas as requisições.

## Funcionalidades

- **Proxy de requisições** — busca e retorna o conteúdo de qualquer URL via rota `/<url>`
- **Bloqueio de domínios** — sites bloqueados retornam uma página de acesso negado
- **Filtragem de palavras** — substitui palavrões por versões censuradas diretamente no HTML retornado
- **Painel de administração** — interface web para gerenciar a lista de sites bloqueados e palavras filtradas (adicionar, editar e remover)
- **Log de requisições** — registra cada acesso com status `allowed`, `blocked` ou `filtered`

## Tecnologias

- Python 3
- Flask
- Requests
- JSON (armazenamento de listas e logs)

## Instalação

**Pré-requisitos:** Python 3.10 ou superior.

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/web-proxy.git
cd web-proxy
pip install -r requirements.txt
```

## Configuração das listas

As listas são armazenadas em arquivos JSON na raiz do projeto e podem ser gerenciadas tanto pelo painel web quanto editando os arquivos diretamente.

### Sites bloqueados — `blocked.json`

Cada entrada possui um `id` único (UUID), a `url` do domínio e um `timestamp` de quando foi adicionada:

```json
[
  {
    "id": "2580b413-eee5-4795-98f2-a9e18ff2aaba",
    "url": "www.exemplo.com",
    "timestamp": "2026-05-29 00:50:55"
  }
]
```

> Basta o domínio — o proxy compara automaticamente o domínio da URL requisitada com os da lista.

### Palavras filtradas — `words.json`

Cada entrada possui o termo `original` e sua versão `censored`:

```json
[
  {
    "id": "99a7f9e5-d065-46fd-a0a7-992dd53fd44e",
    "original": "palavra",
    "censored": "substituta",
    "added_at": "2026-05-29 01:12:58"
  }
]
```

## Execução

```bash
python app.py
```

O servidor sobe na porta `5001`. Acesse o painel de administração em:

```
http://localhost:5001
```

Para usar o proxy, faça requisições no formato:

```
http://localhost:5001/https://www.exemplo.com
```

## Estrutura do projeto

```
web-proxy/
├── app.py              # Rotas Flask e lógica principal
├── utils.py            # Funções auxiliares (log, filtro, JSON)
├── blocked.json        # Lista de domínios bloqueados
├── words.json          # Lista de palavras filtradas
├── log.json            # Registro de requisições
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── blocked_sites.html
│   ├── swear_words.html
│   └── forbidden.html
└── static/
    └── js/main.js
```

---

## Uso de IA no desenvolvimento

> *A Inteligência Artificial foi usada para planjamento, correção, sugestão de ideias e design de páginas. Para a estrutura do projeto, correção de código e esclarecimentos de dúvidas sobre as bibliotecas, foi usado o Gemini. O design da páina foi feito usando a IA do Figma, e o resultado original, feito com TypeScript e React, foi traduzido para a sintaxe HTML e Jinja2 usando Claude, junto com a estruturação do README.md.*

## Por que essa tecnologia?

> *Escolhi o Flask e a biblioteca Requests por ter maior familiaridade com Python e o Flask do que o Express de JavaScript (a única outra linguagem que sou familiarizado)*

## Vantagens e dificuldades

> *As maiores vantagens de trabalhar com o Flask sem dúvida é o aproveitamento da sintaxe e outras bibliotecas do Python, como a Requests, urllib.parse, etc, bem como a leveza e facilidade do próprio framework. As maiores dificuldades no trabalho foi a criação de um sistema centralizado CRUD nos arquivos JSONs e a checagem da URL *

---

## Autor

Davi Vitorino