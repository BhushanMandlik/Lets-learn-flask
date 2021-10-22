from flask import Flask, Markup, render_template

# Create Flask's app object
app = Flask(__name__, 
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static")

@app.route("/")
def hello():
    # return "Hello World!"
    # return Markup("<h1>Hello, I am Bhushan Mandlik</h1>")
    return render_template("index.html", name="Bhushan")

if __name__ == "__main__":
    app.run(debug=True)