from cryptography.fernet import Fernet

# Generar una nueva clave Fernet válida
SECRET_KEY = Fernet.generate_key()
print("Nueva clave Fernet generada:", SECRET_KEY)
