import operator

CALCULATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def lambda_handler(event, context):
    code = event.get('code', '')
    status_code = 200

    num1, sign, num2 = code.split()
    return_value = CALCULATIONS[sign](int(num1), int(num2))
  
    return {'statusCode': status_code, 'body': return_value}
