# Brute-force column ordering
from itertools import permutations

def decrypt_with_key(ciphertext, key):
    return ciphertext

def looks_like_english(text):
    # Simple heuristic: check for common English words
    common_words = ['the', 'and', 'is', 'in', 'it']
    return any(word in text.lower() for word in common_words)

def brute_force_ct(ciphertext, suspected_keylength):
    for possible_key in permutations(range(suspected_keylength)):
        decrypted = decrypt_with_key(ciphertext, possible_key)
        if looks_like_english(decrypted):
            return decrypted, possible_key
# Time complexity grows factorially with key length