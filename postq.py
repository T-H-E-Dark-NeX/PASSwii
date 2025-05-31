import secrets
from quantcrypt.kdf import KKDF
from typing import Optional

class PasswordGenerator:
    
    def __init__(self, master_key: Optional[bytes] = None) -> None:
        self.master_key = master_key or secrets.token_bytes(64)
        self.charset = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789!@#$%^&*"
    
    def generate_password(self, length: int) -> str:
        
        length = max(1, length)
        
        
        derive_len = max(32, length)
        
        password_bytes = KKDF(
            master=self.master_key,
            key_len=derive_len,
            num_keys=1
        )[0]  # 1st ele
        
        
        password_bytes = password_bytes[:length]
        
        password = ''.join(
            self.charset[byte % len(self.charset)] 
            for byte in password_bytes
        )
        
        return password



def main():
    generator = PasswordGenerator()
    
    for length in [16, 24, 32]:
        password = generator.generate_password(length)
        print(f"Length {length}: {password}")
     


def call(l):
    generator = PasswordGenerator()
    
    for length in [ l ,16, 24, 32]:
        password = generator.generate_password(length)
        print(f"Length {length}: {password}")
      


if __name__ == "__main__":
    main()

