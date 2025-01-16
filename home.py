from flask import Flask, render_template_string, render_template, redirect

app = Flask(__name__)

# Redirect the root URL to /home
@app.route("/")
def root():
    return redirect("/home", code=302)

#home function at index.html
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/index.html")
def redirect_to_home():
    return redirect("/home")

@app.route("/MVP1map.html")
def row():
    return app.send_static_file('MVP1map.html')

# condition to check valid lat/long: https://www.geeksforgeeks.org/flask-message-flashing/
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == "POST":
#         if request.form['pass'] != "GFG":
#             error = "Invalid Password"
#         else:
#             flash("You are successfully login into the Flask Application")
#             return redirect(url_for('row'))

#     return render_template("login.html", error=error)


# execute command with debug function
if __name__ == '__main__':
    app.run(debug=True)

