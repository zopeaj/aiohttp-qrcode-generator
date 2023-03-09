import os
import sys
from dotenv import load_dotenv
load_dotenv()


path = os.environ["FILE_PATH"]
sys.path.append(path)

from aiohttp import web
from app.api.routes import setup_routes

app = web.Application()

setup_routes(app)
web.run_app(app, host="127.0.0.1", port=8082)
