from os import environ
from dotenv import load_dotenv

class Config:
    def __init__(self):
        self.dotenv_file = "/home/serviceharmony/git/hmy-wallet-tools/.env"
        load_dotenv(self.dotenv_file)
        self.hmy_app = environ.get("HMY_APP")
        self.passphrase_file = environ.get("PASSPHRASE_FILE")
        self.rewards_wallet = environ.get("REWARDS_WALLET")
        self.harmony_validator_api = environ.get("HARMONY_VALIDATOR_API")
        self.harmony_rpc = environ.get("HARMONY_RPC")
        self.reserve_amount = environ.get("RESERVE_AMOUNT")
        self.gas_price = environ.get("GAS_PRICE")
        self.ntfy_url = environ.get("NTFY_URL")
        
    def validate(self):
        """Validate the configuration"""
        essential_vars = [
            "hmy_app",
            "passphrase_file",
            "rewards_wallet",
            "harmony_validator_api",
            "harmony_rpc",
            "reserve_amount",
            "gas_price",
            "ntfy_url"
        ]
        for var in essential_vars:
            if not getattr(self, var):
                raise ValueError(f"Config variable {var} is not set!")
            
config = Config()
config.validate()