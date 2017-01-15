from flask import Flask, request, render_template, url_for

app = Flask(__name__)

### Index
@app.route("/")
def index():
    items = []
    items += [{"url":"/fakebook", "text":"Fakebook: previous tab"}]
    items += [{"url":"/autofill", "text":"Autofill example"}]
    return render_template('index.html', items=items)


### Autofill
@app.route("/autofill")
def autofill():
    return render_template('autofill.html')

@app.route("/capturepost", methods=["POST"])
def capture_post():
    return render_template('captured.html', req=request)

### Fakebook section
@app.route("/fakebook")
def fakebook():
    return render_template('fakebook.html', fb_background=url_for('static', filename='fb.png'))

@app.route("/bargain")
def fakebook_404():
    return render_template('fakebook404.html')

@app.route("/fakebooklogin")
def fakebook_login():
    return render_template('fakebooklogin.html', fb_login = url_for('static', filename='fakebook_login.png'))

if __name__ == "__main__":
    app.run()