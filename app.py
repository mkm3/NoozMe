# from flask import Flask, render_template, redirect, url_for, request


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     """Route for handling the login page logic."""
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)
