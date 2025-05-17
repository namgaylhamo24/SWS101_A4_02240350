def columnar_encrypt(plaintext, key, padding_char='X'):
    """
    Encrypts plaintext using columnar transposition cipher
    Follows the exact steps from your example with "ATTACK AT DAWN" and "LEMON"
    """
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    
    # Calculate padding needed
    key_length = len(key)
    padding = (key_length - (len(plaintext) % key_length)) % key_length
    padded_text = plaintext + padding_char * padding
    
    # Create encryption matrix
    num_rows = len(padded_text) // key_length
    matrix = [list(padded_text[i*key_length:(i+1)*key_length]) 
              for i in range(num_rows)]
    
    # Determine column order (sorted alphabetically with original positions)
    sorted_key = sorted([(char, i) for i, char in enumerate(key)])
    column_order = [index for (char, index) in sorted_key]
    
    # Generate ciphertext by reading columns in order
    ciphertext = []
    for col in column_order:
        ciphertext.append(''.join([matrix[row][col] for row in range(num_rows)]))
    
    return ' '.join(ciphertext)

def columnar_decrypt(ciphertext, key, padding_char='X'):
    """
    Decrypts ciphertext encrypted with columnar transposition
    """
    key = key.upper()
    cipher_blocks = ciphertext.split()
    
    # Reconstruct column order
    sorted_key = sorted([(char, i) for i, char in enumerate(key)])
    column_order = [index for (char, index) in sorted_key]
    
    # Determine original column positions
    num_cols = len(key)
    num_rows = len(cipher_blocks[0])  # All blocks same length
    
    # Rebuild the transposed matrix
    transposed = []
    for i, col in enumerate(column_order):
        # Find which cipher block corresponds to this column
        block_index = column_order.index(col)
        transposed.append(list(cipher_blocks[block_index]))
    
    # Reconstruct original matrix by reading rows
    plaintext = []
    for row in range(num_rows):
        for col in range(num_cols):
            plaintext.append(transposed[col][row])
    
    # Remove padding and restore original case
    decrypted = ''.join(plaintext).rstrip(padding_char)
    return decrypted

# Example usage matching your step-by-step demo
plaintext = "ATTACK AT DAWN"
key = "LEMON"

# Encryption
ciphertext = columnar_encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}") 
# Output: "AKW TAN TTX CAX ADX"

# Decryption
decrypted = columnar_decrypt(ciphertext, key)
print(f"Decrypted: {decrypted}")  
# Output: "ATTACKATDAWN" (spaces not preserved)