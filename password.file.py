from cryptography.fernet import Fernet

# Function to generate a key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt the password
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Function to decrypt the password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Main program
def main():
    # Generate a key for encryption
    key = generate_key()
    
    print("A new key has been generated.")
    print(f"Keep this key safe; you will need it to decrypt your password:\n{key.decode()}\n")

    # Get user input for the secret password
    secret_password = input("Enter your secret password: ")

    # Encrypt the password
    encrypted_password = encrypt_password(secret_password, key)

    # Write the encrypted password to a file
    with open("encrypted_password.txt", "wb") as file:
        file.write(encrypted_password)

    print("Your password has been encrypted and saved to 'encrypted_password.txt'.")

    # For demonstration, we'll also show how to decrypt the password
    decrypt_choice = input("Do you want to decrypt the password? (yes/no): ").strip().lower()
    if decrypt_choice == 'yes':
        try:
            decrypted_password = decrypt_password(encrypted_password, key)
            print(f"The decrypted password is: {decrypted_password}")
        except Exception as e:
            print("An error occurred during decryption:", e)

if __name__ == "__main__":
    main()
