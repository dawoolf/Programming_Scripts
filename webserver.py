#!/usr/bin/python

"""
	Creating a Simple HTTP Server

"""

import SocketServer
import SimpleHTTPServer

class HttpRequestHandler (SimpleHTTPServer.SimpleHTTPRequestHandler) :

	def do_GET(self) :

		if self.path == '/admin' :
			self.wfile.write('This page is only for Admins!')
			self.wfile.write(self.headers)

		else :
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)



httpServer = SocketServer.TCPServer(("",10000), HttpRequestHandler)

httpServer.serve_forever()
