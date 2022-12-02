"""Microservice Development

This is the solution of the challenge:
Create a simple microservice in any programming language of your choice, as follows:
- The application should be a web server that returns a JSON response, when its / URL path is accessed:
{
  "timestamp": "<current date and time>",
  "hostname": "<Name of the host (IP also accepted)>",
  "engine": "<Name and/or version of the engine running>",
  "visitor ip": "<the IP address of the visitor>"
}
"""

from flask import Flask
from flask import jsonify
from flask import request
from datetime import datetime
import socket
import pkg_resources

def create_application() -> Flask:
    app = Flask(__name__)


    @app.route("/", methods=["GET"])
    def getResponse():
        # definition of the method that generate the JSON structure
        return jsonify({
            "timestamp" : datetime.now(),
            "hostname" : socket.gethostname(),
            "engine" : pkg_resources.get_distribution('flask').version,
            "visitor ip" : request.remote_addr
        }
        )
    return app

if __name__=="__main__":
    app = create_application()
    app.run(host="0.0.0.0", port=5000, debug=True)