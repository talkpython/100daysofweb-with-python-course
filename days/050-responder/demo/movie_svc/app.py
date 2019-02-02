import responder

app = responder.API()


@app.route('/')
def index(req, resp):
    resp.content = "Hello world"


app.run()
