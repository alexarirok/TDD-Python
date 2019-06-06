from hello import Flask, render_templates
app = Flask(__name__)

@app.route("/hello/<user>")
def hello_name(user):
    return render_templates("hello_name", name=user)

if __name__ == "__main__":
    app.run(debug = True)
