Login Information Storage Program
This project is a simple Python program that receives an email and a password from the user, validates the input format, and stores the data inside a database file.

📌 Features
Accepts email and password from the user

Validates the email format using a regular expression

Ensures the password contains only letters and digits

Stores the data inside a file-based database (database.txt)

Repeats input prompts until valid data is provided

📧 Email Format Rules
A valid email must follow this structure:

go
Copy code
expression@string.string


Where:

expression → combination of letters and numbers

string → only letters

Exactly one @ and one . must exist in correct order

🔐 Password Rules
Must contain only letters and digits

No special characters allowed

Example: abc123, Pass2024


📁 Database File
All valid entries are stored inside:

pgsql
Copy code
database.txt
In the format:

pgsql
Copy code
email,password


alex@gmail.com,pass123
test123@company.com,hello99
