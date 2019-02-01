import os

from bottle import abort, request, route, run, view
import requests

API_URL = os.environ['AWS_ENDPOINT']
TITLE = "PyBites PEP8 Checker"
ERROR_CODE = 400


@route('/', method=['GET', 'POST'])
@view('index')
def index():
    code = request.forms.get('code') or ''
    pep_errors = ''

    if code:
        payload = {"code": code}
        resp = requests.post(API_URL, json=payload).json()

        error = resp.get("errorMessage")
        exception = resp.get("errorType")
        if error and exception:
            msg = f"Lambda function raised a {exception} exception"
            abort(ERROR_CODE, msg)

        pep_errors = resp["body"]

    return {'title': TITLE,
            'code': code,
            'pep_errors': pep_errors}


run(host='localhost', port=8080, debug=True, reloader=True)
