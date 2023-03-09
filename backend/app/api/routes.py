import os
import sys
from dotenv import load_dotenv
load_dotenv()


path = os.environ["FILE_PATH"]
sys.path.append(path)

from api.controller.QRCodeGeneratorController import qrcodeGenroutes

def setup_routes(app):
    app.add_routes(qrcodeGenroutes)


