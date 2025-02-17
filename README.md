# PRODIGY_CS_03

# Password Strength Checker

This project provides a Python script to assess the strength of a given password based on various criteria such as length, uppercase and lowercase letters, numbers, and special characters.

## Features
- Evaluates password strength as **Weak, Moderate, or Strong**.
- Provides feedback on how to improve password security.
- Uses regular expressions to check for character patterns.

## Requirements
Ensure you have Python installed to run this script.

## Usage

### Run the script
```sh
python main.py
```

### Example Output
```
Enter your password: P@ssw0rd123
Password Strength: Strong
```
If the password is weak, the script provides suggestions to improve it.

## Project Structure
```
├── main.py         # Password strength checker script
├── README.md       # This file
```

## How It Works
1. The script takes user input for a password.
2. It checks for:
   - Length (at least 8 and 12 characters for higher scores)
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Special characters
3. A strength score is calculated based on these criteria.
4. The password is classified as Weak, Moderate, or Strong.
5. If necessary, feedback is provided to improve the password.

## Author
Disha Sejpal

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

