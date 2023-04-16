from api import BASE_URL
from botty import dp

import handlers
from app import app

handlers.setup()
dp.run_server(BASE_URL, app)
