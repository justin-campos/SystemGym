from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, db, login_required


@app.route('/login', methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Nombre de usuario requerido", 'error')
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password", 'error'):
            flash("Contraseña requerido")
            return render_template("login.html")

        # Query database for username
        rows = db.execute("SELECT * FROM administradores WHERE usuario=:username",
                          username=request.form.get("username"))

        print("------------", rows)
        # Ensure username exists and password is correct
        if rows[0]["contrasena"] != request.form.get("password"):
            flash("Usuario/contraseña invalido", 'error')
            return render_template("login.html")
        print("------------2222")
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("inicio de sesion correctamente", 'exito')
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
