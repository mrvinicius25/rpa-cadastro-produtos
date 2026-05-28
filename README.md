# RPA para cadastro de produtos com Python

Este projeto é uma automação (RPA) desenvolvida em Python que realiza o cadastro automático de produtos em um sistema web.

A automação utiliza PyAutoGUI para simular ações do usuário (cliques e digitação) e Pandas para leitura de uma base de dados em CSV.

---

## Funcionalidades

- Abertura automática do navegador
- Acesso ao sistema web
- Login automatizado
- Leitura de base de dados (CSV)
- Cadastro automático de produtos no sistema
- Preenchimento de múltiplos campos de forma sequencial

---

## Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas

---

## Estrutura do projeto
```
rpa-cadastro-produtos/
└── rpa/
    ├── main.py
    ├── auxiliar.py
    └── produtos.csv
```

---

## Como executar

1. Instale as dependências:

```
pip install pyautogui pandas
```
2. Execute o script
```
python main.py
```
## Importante

- Ajuste as coordenadas (`x` e `y`) de acordo com a resolução da sua tela
- Não utilize o computador durante a execução da automação

## Observações

- O arquivo `auxiliar.py` pode ser usado para identificar posições do mouse na tela
- A automação depende do layout da página, podendo quebrar caso o sistema mude

## Possíveis melhorias

- Uso de Selenium вместо PyAutoGUI
- Tratamento de erros
- Interface gráfica
- Logs de execução

---

# Dica importante

Se você quiser deixar seu projeto mais valorizado troque:

> PyAutoGUI → Selenium

Porque:
- PyAutoGUI simula o uso humano (mouse e teclado) para controlar qualquer aplicativo na área de trabalho
- Selenium é padrão de mercado pra automação web e atua diretamente no código-fonte da página web. Ele é ideal para interagir com elementos visíveis ou ocultos

---
