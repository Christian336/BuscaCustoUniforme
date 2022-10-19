from app import app
from flask import render_template, request, redirect, flash

from app import map
from app import functions


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():

    partida = request.form.get('partida')
    destino= request.form.get('destino')

    if partida in map.cidades and destino in map.cidades:
        # Rodando o Programa

        caminho = functions.bcu(map.mapa, partida, destino)

        return '''
        <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>homepage</title>
        <style>
            body{
                font-family: Arial, Helvetica, sans-serif;
                background-color: black;
                color: white;
            }
            h1{
                font-size: 80px;
                text-align: center;
            }
            form{
                text-align: center;
            }

            p{
                text-align: center;
            }
            
        </style>
    </head>
    <body>
        <header><h1>Resultado da Busca</h1></header><hr><br><br><b>
        <p>O caminho mais curto é: '''+functions.formatar(caminho)+'''</p>
        <p>A distância desse caminho é: '''+str(functions.rota_distancia(caminho))+''' km.</p>
        </b>
        <form action="/index">
            <input type="submit" value="Voltar Para Página Inicial">
        </form>

        
    </body>
    </html>
        '''
    else:
        flash(' ')
        return redirect('/index')