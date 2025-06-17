# Telegram Wallet Insight Chatbot

This Telegram chatbot provides users with insights into their cryptocurrency wallets, built with **Python** and **Streamlit**.

## Features

* **Wallet Balance Tracking:** Get real-time balances for specified cryptocurrencies.
* **Transaction History (Potential Future Feature):** View a summary of recent transactions.
* **Performance Metrics (Potential Future Feature):** Analyze the performance of assets over time.

---

## Setup Instructions

Follow these steps to get your chatbot up and running.

### Prerequisites

* **Python 3.11:** Ensure you have a compatible Python version installed.
* **Telegram Bot Token:** Create a new bot via BotFather on Telegram and obtain your API token. You can get this by messaging botFather on telegram using this [link](https://t.me/BotFather) and send the command ```/newbot```.
* **Morlais API Key:** You will need an API key from Moralis. You can register get it here This is a [here](https://admin.moralis.com/register).
* **OpenAI API Key:** You will need an API key from OpenAI. You can register get it here This is a [here](https://platform.openai.com/docs/overview).

### 1. Clone the Repository

1. get the code onto your machine:

```markdown
git clone https://github.com/FarajaOmbeni/telegram-bot
```
2. Enter the project folder
```markdown
cd telegram-bot
```
3. Create a python environment
```markdown
python -m venv venv
```
4. Activate the virtual environment. This is a windows command
```markdown
source venv/Scripts/activate
```
- Below is the command for mac or linux
```markdown
source venv/bin/activate
```
5. Install the dependancies
```markdown
pip install -r requirements.txt
```

## 2. Configure Environment Variables
Create a file named .env in the root of your project to store sensitive information. Do not commit this file to version control.
```markdown
OPENAI_API_KEY="your-openai-api-key"
TELEGRAM_BOT_TOKEN="your-telegram-bot-api-key"
MORALIS_API_KEY="your-moralis-api-key"
```
Remember to replace the placeholder values with your actual tokens/keys.

## Running the Application
Running the Telegram Bot
```markdown
python main.py
```

Usage
Once the bot is running, find it on Telegram and use the following commands:

- Start the telegram bot
```markdown
/start
```
- Get the balance of the crypto wallet
```markdown
/balance <wallet-address>
```
- Get the profit and loss summary of the crypto wallet
```markdown
/pnl <wallet-address>
```
- Get the history of the crypto wallet
```markdown
/stats <wallet-address>
```

### Where to get a test wallet address?
You can get wallet addresses on [this](https://etherscan.io/) website.