from flask import Flask, render_template
def index():
    return render_template('main.html')
app = Flask(__name__)
app.add_url_rule('/', 'index', index)
if __name__ == "__main__":
    app.run()