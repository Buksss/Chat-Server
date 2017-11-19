import socketserver
'''
class requestHandler(socketserver.BaseRequestHandler):
    ''\'
    This is the main class for the Server object
    The server will take text and send it back to the client
    Its handle() method is for handling requests and will be called in a thread
    This is because socketserver is a synchronous library and otherwise would not be able to handle multiple requests at
    once
    ''\'
    def handle(self):
        data = self.request.recv(2048).strip()
        print(data)
        self.request.sendall("Yo we got {} from you. Your IP is".format(data, self.client_address[0]))'''

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())