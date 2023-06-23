from app import app, db, login_required
from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from datetime import datetime

app.config['SECRET_KEY'] = '123'


@app.route('/', methods=["GET", "POST"])
@login_required
def index():

    print

    if request.method == "POST":

        # Obtener la fecha y hora actual
        fecha_y_hora_actual = datetime.now()

        # Formatear la fecha y hora
        fecha_y_hora_formateada = fecha_y_hora_actual.strftime(
            "%Y/%m/%d - %H:%M:%S")

        # Imprimir la fecha y hora formateada
        print("Fecha y hora actual:", fecha_y_hora_formateada)

        # capturamos el nombre del usuario
        nombremiembro = request.form.get('nombremiembro')

        # capturamos el nombre del usuario
        nombredia = request.form.get('nombrecliente')

        print("-hola!-------", nombremiembro)
        print("-hola!-------", nombredia)

        if(nombremiembro == None):
            db.execute("INSERT INTO AsistenciaPorDia (nombre, fechahoraentrada, idadmin) values (:nombredia, :fecha_y_hora_formateada, '1')",
                       nombredia=nombredia, fecha_y_hora_formateada=fecha_y_hora_formateada)
        else:

            idcliente = db.execute(
                "SELECT idcliente FROM clientes WHERE nombre =:nombremiembro", nombremiembro=nombremiembro)

            print(idcliente)

            db.execute("INSERT INTO AsistenciaClientes (idcliente, fechahoraentrada, idadmin) values (:idcliente, :fecha_y_hora_formateada, '1')",
                       idcliente=idcliente, fecha_y_hora_formateada=fecha_y_hora_formateada)

    clientes = db.execute("SELECT * FROM clientes")

    asistencia = db.execute(
        "SELECT * FROM AsistenciaClientes INNER JOIN clientes on AsistenciaClientes.idac = clientes.idcliente")

    return render_template("index.html", clientes=clientes, asistencia=asistencia)
