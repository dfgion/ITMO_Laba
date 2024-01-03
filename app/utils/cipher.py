from cryptography.fernet import Fernet
 
cipher_key = Fernet.generate_key()

cipher = Fernet(cipher_key)