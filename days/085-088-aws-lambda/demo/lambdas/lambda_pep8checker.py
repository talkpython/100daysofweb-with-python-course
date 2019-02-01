from contextlib import redirect_stdout
from io import StringIO
import tempfile

import pycodestyle

TMP = '/tmp'
TEMPFILE = tempfile.NamedTemporaryFile(dir=TMP)


def lambda_handler(event, context):
    code = event.get('code', '')

    with open(TEMPFILE.name, 'w') as f:
        f.write(f'{code}\n')  # need to add final newline
        f.seek(0)  # rewind file

        out = StringIO()
        with redirect_stdout(out):
            pep = pycodestyle.Checker(f.name, show_source=True)
            pep.check_all()

        return {'statusCode': 200,  # = ok, lambda raises exceptions early
                'body': out.getvalue()}


if __name__ == '__main__':
    print('ok')
    event = dict(code='print("hello world")')
    ret = lambda_handler(event, {})
    print(ret)

    print()
    print('not ok')
    event = dict(code='   print("hello world")')
    ret = lambda_handler(event, {})
    print(ret)
