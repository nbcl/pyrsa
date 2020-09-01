from keygen import keyGen

class rsa1028():
    """Main RSA class
    Generates public, private keys
    and can encrypt and decrypt messages
    """
    def __init__(self):
        rsa1028 = keyGen()
        self.n = rsa1028.public[0]
        self.e = rsa1028.public[1]
        self.d = rsa1028.private

    def encrypt(self, message: str) -> int:
        """Encrypts non-padded message"""
        encoded = pow(message, self.e, self.n)
        return encoded

    def decrypt(self, encoded: str) -> int:
        """Decrypts non-padded message"""
        message = pow(encoded, self.d, self.n)
        return message

rsa = rsa1028()
rsa.decrypt(rsa.encrypt(1))
