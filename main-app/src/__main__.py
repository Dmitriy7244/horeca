from api import set_webhook

import app
import handlers
from deps import run

app.setup()
set_webhook()
handlers.setup()
run()
