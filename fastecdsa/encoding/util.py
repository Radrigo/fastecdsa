from struct import pack


def int_bytelen(x):
    length = 0

    while x:
        length += 1
        x >>= 8

    return length


def int_to_bytes(x):
    bs = b''

    while x:
        bs = pack('=B', (0xff & x)) + bs
        x >>= 8

    return bs


def bytes_to_int(bytestr):
    """Make an integer from a big endian bytestring."""
    value = 0
    for byte_intval in bytestr:
        value = value * 256 + byte_intval
    return value
