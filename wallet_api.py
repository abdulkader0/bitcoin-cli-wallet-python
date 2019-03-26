import csv
from Crypto.PublicKey import RSA

def pubkeyContent(inputContent):
    contentWithoutHeader= inputContent[len("-----BEGIN PUBLIC KEY-----") + 1:]
    contentWithoutTail = contentWithoutHeader[:-1 * (len("-----END PUBLIC KEY-----") + 1)]
    contentWithoutReturn = contentWithoutTail[:64] + contentWithoutTail[65:129] + contentWithoutTail[130:194] + contentWithoutTail[195:]
    return contentWithoutReturn


class RSAKey4Mixin():
    def __init__(self):
        key = RSA.generate(1024)
        pubkey = key.publickey()
        private_key = key.exportKey()
        session_key = pubkeyContent(pubkey.exportKey())
        self.session_key = session_key.decode()
        self.private_key = private_key.decode()
 
class userInfo():
    def __init__(self, pin_token = "", session_id = "", user_id = ""):
        self.pin_token = pin_token
        self.session_id = session_id
        self.user_id = user_id
    def fromcreateUserJson(self, userInfojson):
        self.pin_token  = userInfojson.get("data").get("pin_token")
        self.session_id = userInfojson.get("data").get("session_id")
        self.user_id    = userInfojson.get("data").get("user_id")

class asset():
    def __init__(self, jsonInput):
        self.type     = jsonInput.get("type")
        self.name     = jsonInput.get("name")
        self.asset_id = jsonInput.get("asset_id")
        self.chain_id = jsonInput.get("chain_id")
        self.balance  = jsonInput.get("balance")
        self.symbol   = jsonInput.get("symbol")
        self.pubkey   = jsonInput.get("public_key")
        self.account_name = jsonInput.get("account_name")
        self.account_tag  = jsonInput.get("account_tag")

class WalletRecord():
    def __init__(self, pin, userid, session_id, pin_token, private_key):
       self.pin = pin
       self.userid = userid
       self.session_id = session_id
       self.pin_token = pin_token
       self.private_key = private_key

def append_wallet_into_csv_file(this_wallet, file_name):
    with open(file_name, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([this_wallet.private_key,
                            this_wallet.pin_token,
                            this_wallet.session_id,
                            this_wallet.user_id,
                            ""])

def load_wallet_csv_file(file_name):
    with open(file_name, newline='') as csvfile:
        reader  = csv.reader(csvfile)

        wallet_records = []
        for row in reader:

            pin         = row.pop()
            userid      = row.pop()
            session_id  = row.pop()
            pin_token   = row.pop()
            private_key = row.pop()
            wallet_records.append(WalletRecord(pin, userid, session_id, pin_token, private_key))
        return wallet_records
def create_wallet_csv_file(file_name):
    with open(file_name, newline='') as csvfile:
        reader  = csv.reader(csvfile)

        wallet_records = []
        for row in reader:

            pin         = row.pop()
            userid      = row.pop()
            session_id  = row.pop()
            pin_token   = row.pop()
            private_key = row.pop()
            wallet_records.append(WalletRecord(pin, userid, session_id, pin_token, private_key))
        return wallet_records
