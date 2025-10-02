# SHA-1 Password Cracker

freeCodeCamp Information Security Project

## Description
A password cracker that uses SHA-1 hashing to crack passwords from a list of the top 10,000 most common passwords.

## Files
- `password_cracker.py` - Main function
- `main.py` - Test file
- `test_module.py` - Unit tests
- `top-10000-passwords.txt` - Password list
- `known-salts.txt` - Known salts

## Usage
```python
import password_cracker

# Without salts
result = password_cracker.crack_sha1_hash("hash_here")

# With salts
result = password_cracker.crack_sha1_hash("hash_here", use_salts=True)