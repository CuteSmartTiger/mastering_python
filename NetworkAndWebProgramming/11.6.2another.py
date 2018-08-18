from xmlrpc.server import SimpleXMLRPCServer

def add(x,y):
    return x+y

serv = SimpleXMLRPCServer(('', 15000))
serv.register_function(add)
serv.serve_forever()