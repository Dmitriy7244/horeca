from api import APP_URL
from botty import dp

import handlers
from app import app

handlers.setup()
dp.run_server(APP_URL, app)
