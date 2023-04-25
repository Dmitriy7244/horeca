from deps import dp, Message, FSMContext, run
from lib import ask_duplicate_option


@dp.text().state()
def _(msg: Message, state: FSMContext):
    return ask_duplicate_option(msg, state)


run()
