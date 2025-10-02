import hashlib

def crack_sha1_hash(hash, use_salts=False):
    """
    Cracks a SHA-1 hash by comparing it against common passwords.
    
    Args:
        hash: The SHA-1 hash string to crack
        use_salts: If True, tries prepending and appending salts to passwords
    
    Returns:
        The cracked password string, or "PASSWORD NOT IN DATABASE" if not found
    """
    
    # Leer las contraseñas más comunes
    try:
        with open('top-10000-passwords.txt', 'r') as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        return "PASSWORD NOT IN DATABASE"
    
    # Si no usamos salts, solo probamos las contraseñas directamente
    if not use_salts:
        for password in passwords:
            # Hashear la contraseña y comparar
            hashed = hashlib.sha1(password.encode()).hexdigest()
            if hashed == hash:
                return password
    else:
        # Leer los salts conocidos
        try:
            with open('known-salts.txt', 'r') as f:
                salts = f.read().splitlines()
        except FileNotFoundError:
            return "PASSWORD NOT IN DATABASE"
        
        # Probar cada combinación de salt + password
        for password in passwords:
            for salt in salts:
                # Probar salt prepended (salt + password)
                salted_password = salt + password
                hashed = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed == hash:
                    return password
                
                # Probar salt appended (password + salt)
                salted_password = password + salt
                hashed = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed == hash:
                    return password
    
    return "PASSWORD NOT IN DATABASE"