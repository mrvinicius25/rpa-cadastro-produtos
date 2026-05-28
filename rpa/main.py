import pyautogui as pg
import time
#biblioteca = pacote de código
pg.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passso a passo do seu programa 
# Passo 1: entrar no sistema empresa
# abrir navegador
pg.press("win")
pg.write("chrome")
pg.press("enter")
time.sleep(5)
pg.click(x = 1064, y = 478)
# fazer uma pausa maior pro site
time.sleep(3)
# Passo 2: fazer login
# clicar no espaço de login
pg.write(link)
pg.press("enter")
time.sleep(7)
pg.click(x = 674, y = 447)
pg.write("alu")
pg.press("tab")
pg.write("1")
pg.press("tab")
pg.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(4)
# Passo 3: abrir a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)
for linha in tabela.index:
    # Passo 4: cadastrar produtos
    pg.click(x=749, y=330)
    pg.hotkey('ctrl', 'a')
    # código
    codigo = str(tabela.loc[linha,"codigo"])
    pg.write(codigo)
    pg.press("tab")
    # marca
    marca = str(tabela.loc[linha,"marca"])
    pg.write(marca)
    pg.press("tab")
    # tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pg.write(tipo)
    pg.press("tab")
    # categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pg.write(categoria)
    pg.press("tab")
    # preço
    preco = str(tabela.loc[linha,"preco_unitario"])
    pg.write(preco)
    pg.press("tab")
    # custo 
    custo = str(tabela.loc[linha,"custo"])
    pg.write(custo)
    pg.press("tab")
    # observação
    obs = str(tabela.loc[linha,"obs"])
    if(obs!="nan"):
        pg.write(obs)
    pg.press("tab")
    pg.scroll(5000)
    # Passo 5: repetir o passo 4

