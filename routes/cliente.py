from app import app, db, login_required
from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from datetime import datetime

app.config['SECRET_KEY'] = '123'


@app.route('/clientes', methods=["GET", "POST"])
@login_required
def cliente():

    if request.method == "POST":

        # capturamos el nombre del usuario
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        celular = request.form.get('celular')
        correo = request.form.get('correo')

        print(nombre, apellido, celular, correo)

        db.execute("INSERT INTO clientes (nombre, apellido, fechaderegistro, fechadevencimiento, estadomembresia, ultimavisita, celular, correo, idadmin) VALUES (:nombre, :apellido, 2023, 2024, 1, 2, :celular, :correo, 1)",
                   nombre=nombre, apellido=apellido, celular=celular, correo=correo)

        return redirect("/clientes")

    clientes = db.execute("SELECT * from clientes")

    return render_template("cliente.html", clientes=clientes)
