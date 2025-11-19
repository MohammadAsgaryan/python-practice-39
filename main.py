import re

# Regex pattern for valid email
EMAIL_PATTERN = r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$"

def get_valid_email():
    while True:
        email = input("Enter your email: ").strip()
        if re.match(EMAIL_PATTERN, email):
            return email
        else:
            print("Invalid email format!")
            print("Correct format example: example123@gmail.com")
            print("Please try again...\n")   


def get_valid_password():
    while True:
        password = input("Enter your password (letters and digits only): ").strip()
        if password.isalnum():
            return password
        else:
            print("Password must contain only letters and numbers.")
            print("Please try again...\n")

            
def save_to_database(email, password, filename= "database.txt"):
    with open(filename, "a", encoding="utf-8") as db:
        db.write(f"{email},{password}\n")

   
def main():
    print("=== Login Information Storage Program ===\n")
       
       
    email = get_valid_email()
    password = get_valid_password()
    
    save_to_database(email, password) 
    
    print("\nYour data has been saved successfully!")
    
if __name__ == "__main__":
    main()