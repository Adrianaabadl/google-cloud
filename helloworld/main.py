"""
def hello_world(request):
    request_args = request.args ---> aqui le crea para pasar un parametro (ademas que crea una especie de diccionario vacio)
    if request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'world'
    return f'Hello {name}'
"""
"""
def hello_world(name):
    if name:
        return f'Hello strager (☞ﾟヮﾟ)☞'
    else:
        return f'Hello {name}'

def hello_world(peticion):
    request = peticion.argumentos
    if request and 'parametro' in request:
        name = request['parametro'].lower()
    else:
        name = 'world'
    return f'Hello {name}'
"""
## multiple arguments ##
def hello_world(request):
    request_args = request.args
    request_json = request.get_json(silent=True) #If I dont pass any json objet then set this variable equal to None
    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'world'
        lastname = ''
    return f'Hello {name} {lastname}'

#https://us-central1-cloud-functions-eaa55.cloudfunctions.net/hello_world/?name=adriana&lastname=abad