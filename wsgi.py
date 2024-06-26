import os
import socket
from api import create_app

if os.getenv("FLASK_DEBUG") == "development":
    app = create_app("config.DevConfig")
else:
    app = create_app("config.ProdConfig")

if __name__ == "__main__":
    ipAddress = socket.gethostbyname(socket.gethostname())
    app.run(host=ipAddress, port=os.getenv("PORT", 5000))
