import requests
import os
from dotenv import load_dotenv
from model import generate_response

load_dotenv()

class PortFolio:
    def __init__(self):
        self.api_key = os.getenv('MORALIS_API_KEY')
        self.base_url= "https://deep-index.moralis.io/api/v2.2"
        self.headers = {'X-API-Key': self.api_key}
        self.params = {'chain': 'eth'}
    
    def get_balance(self, wallet_address):
        url = f"{self.base_url}/{wallet_address}/balance"

        try:
            response = requests.get(url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                data = response.json()
                eth_balace = float(data['balance']) / 10**18
                return {
                    'success': True,
                    'balance': eth_balace
                }
            else:
                return  {
                    'success': False,
                    'error': "Failed to check balance"
                }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_profitability_summary(self, wallet_address):
        url = f"{self.base_url}/wallets/{wallet_address}/profitability/summary"

        try:
            response = requests.get(url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                data = response.json()
                print(f"PnL: {data}")
                prompt = str(data)
                print(f"prompt: {prompt}")
                suggestion = generate_response(prompt)
                print(f"suggestion: {suggestion}")
                return {
                    'success': True,
                    'value': suggestion
                }
            else:
                return {
                    'success': False,
                    'error': 'Failed to get analysis'
                }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
        
    def get_wallet_stats(self, wallet_address):
        url = f"{self.base_url}/wallets/{wallet_address}/stats"

        try:
            response = requests.get(url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                data = response.json()
                prompt = str(data)
                suggestion = generate_response(prompt)
                return {
                    'success': True,
                    'value': suggestion
                }
            else:
                return {
                    'success': False,
                    'error': 'Failed to get analysis'
                }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

            
