def balanced_hash(key):
    hash_value = 5381
    for char in str(key):
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value % TABLE_SIZE