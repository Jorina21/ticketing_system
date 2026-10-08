#where will validate passowords against the hash and convert the hash in to bytes to save in database 


def create_password_hash(raw_password = password) -> str[hash_pwd]:
    #bcypt returns bytes conver to str
    
    pass

def _convert_bytes_to_string( byte_pwd : bytes) -> str:
    #will call this to conver bycrpt byte out put to string to save in db _hased pwd
    
    pass

def verify_password(*, raw_password = password, _hashed_pass = hashed_pass) -> bool:
    pass

