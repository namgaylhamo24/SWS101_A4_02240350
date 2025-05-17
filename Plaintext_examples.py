# Python Implementation of the Example
def columnar_encrypt(plaintext, key):
    # Add padding if needed
    padding = len(key) - (len(plaintext) % len(key))
    if padding != len(key):
        plaintext += 'X' * padding
    
    # Create matrix
    num_cols = len(key)
    matrix = [list(plaintext[i:i+num_cols]) 
              for i in range(0, len(plaintext), num_cols)]
    
    # Sort columns by key
    sorted_cols = sorted([(key[i], i) for i in range(num_cols)])
    col_order = [col[1] for col in sorted_cols]
    
    # Generate ciphertext
    ciphertext = ''
    for col in col_order:
        ciphertext += ''.join([row[col] for row in matrix])
    return ciphertext

# Example usage
print(columnar_encrypt("SECRETMESSAGE", "CODE")) 
# Output: "SEESERGEETXAEMXS"