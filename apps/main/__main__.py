import handlers

from api import set_webhook
from deps import run

set_webhook()
handlers.setup()
run()
