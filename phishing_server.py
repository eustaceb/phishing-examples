from bottle import route, post, run, template, static_file, request

### Index
@route("/")
def index():
    items = []
    items += [{"url":"/fakebook", "text":"Fakebook: previous tab"}]
    items += [{"url":"/autofill", "text":"Autofill example"}]
    return template('index.html', items=items)

### Static files
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

### Autofill
@route("/autofill")
def autofill():
    return template('autofill.html')

@post("/capturepost")
def capture_post():
    return template('captured.html', req=request)

### Fakebook section
@route("/fakebook")
def fakebook():
    return template('fakebook.html')

@route("/bargain")
def fakebook_404():
    return template('fakebook404.html')

@route("/fakebooklogin")
def fakebook_login():
    return template('fakebooklogin.html')

if __name__ == "__main__":
    run(host='localhost', port=8080)
