from flask import Flask, render_template_string, render_template, redirect, request, url_for
import MVP1map

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

@app.route("/MVP1map.html", methods=['POST', 'GET'])
def map_view():
    if request.method == 'POST':
        # Get coordinates from the form
        user_lat = request.form.get('latitude')
        user_lon = request.form.get('longitude')

        try:
            #convert string to float, pass to MVP1map.py
            User_lat, user_lon = float(user_lat), float(user_lon)
            MVP1map.generate_map(user_lat, user_lon)
        except ValueError:
            return "Invalid input, please enter numeric coordinates."


    return app.send_static_file('MVP1map.html')

# execute command with debug function
if __name__ == '__main__':
    app.run(debug=True)

