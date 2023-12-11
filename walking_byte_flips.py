import random

def flip_single_byte(input_bytes):
    input_list = bytearray(input_bytes)
    flip_pos = random.randint(0, len(input_list) - 1)
    input_list[flip_pos] = random.randint(0, 255)
    return bytes(input_list)

def flip_two_bytes(input_bytes):
    input_list = bytearray(input_bytes)
    start_pos = random.randint(0, len(input_list) - 2)
    input_list[start_pos] = random.randint(0, 255)
    input_list[start_pos + 1] = random.randint(0, 255)
    return bytes(input_list)

def flip_four_bytes(input_bytes):
    input_list = bytearray(input_bytes)
    start_pos = random.randint(0, len(input_list) - 4)
    for i in range(start_pos, start_pos + 4):
        input_list[i] = random.randint(0, 255)
    return bytes(input_list)

def format_binary_string(binary_str):
    return ' '.join([binary_str[i:i+4] for i in range(0, len(binary_str), 4)])

def bytes_to_binary(input_bytes):
    return ' '.join(format(byte, '08b') for byte in input_bytes)

# Test cases
test_0 = b"\x08\x08\x08\x08\x08\x08\x08\x08"
test_1 = b"\x08\x08\x08\x08\x08\x08\x08\x08"
test_2 = b"\x0F\x0F\x0F\x0F\x0F\x0F\x0F\x0F"

flipped_1 = flip_single_byte(test_0)
flipped_2 = flip_two_bytes(test_1)
flipped_4 = flip_four_bytes(test_2)

print("\nOriginal input (test_0): ")
print("Hexadecimal: ", test_0)
print("Binary: ", bytes_to_binary(test_0))

print("Flipping a single byte: ")
print("Hexadecimal: ", flipped_1)
print("Binary: ", bytes_to_binary(flipped_1))

print("\nOriginal input (test_1): ")
print("Hexadecimal: ", test_1)
print("Binary: ", bytes_to_binary(test_1))

print("Flipping two bytes in a row: ")
print("Hexadecimal: ", flipped_2)
print("Binary: ", bytes_to_binary(flipped_2))

print("\nOriginal input (test_2): ")
print("Hexadecimal: ", test_2)
print("Binary: ", bytes_to_binary(test_2))

print("Flipping four bytes in a row: ")
print("Hexadecimal: ", flipped_4)
print("Binary: ", bytes_to_binary(flipped_4))