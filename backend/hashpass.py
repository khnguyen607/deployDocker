import bcrypt

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(password, hashed_password):
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Example usage:
if __name__ == "__main__":
    # Simulate storing a hashed password into a file
    user_password = "admin"
    hashed_password = hash_password(user_password).decode('utf-8')

    # Save the hashed password to a file (or database)
    with open("hashed_password.txt", "w") as file:
        file.write(hashed_password)

    # Simulate checking a password during login
    input_password = "admin"
    with open("hashed_password.txt", "r") as file:
        stored_hashed_password = file.read()

    if check_password(input_password, stored_hashed_password.encode('utf-8')):
        print("Password is correct.")
    else:
        print("Incorrect password.")
