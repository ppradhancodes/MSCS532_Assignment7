def improved_hash(key):
    hash_value = 0
    for char in str(key):
        hash_value = (hash_value * 31 + ord(char)) % TABLE_SIZE
    return hash_value