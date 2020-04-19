def check_sum(bytestring):
    if type(bytestring) == bytes:
        return sum(bytestring) % 255
    else:
        return sum(bytestring.encode()) % 255


def compare_instances(hash1, hash2):
    return hash1 == hash2
