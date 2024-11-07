import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"""Olá! Bem vindo ao seu Assistente Particular AlertPix!\n
        Você já possui conta AlertPix??""",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    answer = """Commands availale:\n
    type /btc for receive Bitcoin price.
    """
    await update.message.reply_text(answer)


async def yes_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    answer = """Então entre no em nosso grupo especial e começe a apostar!!!\n
    """
    await update.message.reply_text(answer)
    
async def no_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    answer = """Você pode se cadastrar em no site e começar hoje mesmo!\n
    clique no link abaixo:\n(Restam poucas vagas...)\n<link_do_site>
    """
    await update.message.reply_text(answer)
    
async def unknow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    answer = """Não entendi sua resposta...
    """
    await update.message.reply_text(answer)
    
    
async def basic_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle user response based on message text."""
    response = update.message.text.lower()  

    responses = {
        "sim": "Então entre no nosso grupo especial e comece a apostar!!!\n",
        "não": """Você pode se cadastrar no site e começar hoje mesmo!\n
                  clique no link abaixo:\n(Restam poucas vagas...)\n<link_do_site>"""
    }


    answer = responses.get(response, "Não entendi sua resposta...")
    await update.message.reply_text(answer)

def main() -> None:
    """Start the bot."""
    with open("token.txt") as tokenfile:
        token = tokenfile.read()
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, basic_chat))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()