from telegram import Update
from telegram.ext import ContextTypes
from portfolio import PortFolio

service = PortFolio()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
    Welcome! I am your portfolio analyzer bot.
    Commands:
    /balance <wallet> - Check ETH balance
    /pnl <wallet> - Get profit and loss summary
    /stats <wallet> - Get wallet stats
    """
    await update.message.reply_text(message)

async def check_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Send wallet address: /balance 0x...")
        return
    
    wallet = context.args[0]
    await update.message.reply_text("Checking balance...")

    result = service.get_balance(wallet)

    if result['success']:
        balance = result['balance']
        await update.message.reply_text(f"ETH Balance: {balance} ETH")
    else:
        await update.message.reply_text(f"Error: {result['error']}")

async def pnl_analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Send wallet address: /pnl 0x...")
    
    wallet = context.args[0]
    await update.message.reply_text("Checking profit and loss...")

    result = service.get_profitability_summary(wallet)

    if result['success']:
        await update.message.reply_text(result['value'])
    else:
        await update.message.reply_text(f"Error: {result['error']}")
        
async def wallet_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Send wallet address: /pnl 0x...")
    
    wallet = context.args[0]
    await update.message.reply_text("Checking wallet stats...")

    result = service.get_wallet_stats(wallet)

    if result['success']:
        await update.message.reply_text(result['value'])
    else:
        await update.message.reply_text(f"Error: {result['error']}")
        
