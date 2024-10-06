def simple_hash(key):
    return sum(ord(char) for char in str(key)) % TABLE_SIZE