import random

def flip_single_bit(input_str):
    input_list = list(input_str)
    flip_pos = random.randint(0, len(input_list) - 1)
    input_list[flip_pos] = '0' if input_list[flip_pos] == '1' else '1'
    return ''.join(input_list)

def flip_two_bits(input_str):
    input_list = list(input_str)
    start_pos = random.randint(0, len(input_list) - 2)
    input_list[start_pos] = '0' if input_list[start_pos] == '1' else '1'
    input_list[start_pos + 1] = '0' if input_list[start_pos + 1] == '1' else '1'
    return ''.join(input_list)

def flip_four_bits(input_str):
    input_list = list(input_str)
    start_pos = random.randint(0, len(input_list) - 4)
    for i in range(start_pos, start_pos + 4):
        input_list[i] = '0' if input_list[i] == '1' else '1'
    return ''.join(input_list)


test_0 = "00000001"
test_1 = "11000000"
test_2 = "00001111"
test_3 = "10101010"

flipped_1 = flip_single_bit(test_0)
flipped_2 = flip_two_bits(test_1)
flipped_4 = flip_four_bits(test_2)

test_3_flipped_1 = flip_single_bit(test_3)
test_3_flipped_2 = flip_two_bits(test_3)
test_3_flipped_4 = flip_four_bits(test_3)

print("\nOriginal input (test_0): ")
print(test_0)
print("Flipping a single bit: ")
print(flipped_1)
print("\nOriginal input (test_1): ")
print(test_1)
print("Flipping two bits in a row: ")
print(flipped_2)
print("\nOriginal input (test_2): ")
print(test_2)
print("Flipping four bits in a row: ")
print(flipped_4)

print("\n\n Original input (test_3): ")
print(test_3)
print("Flipping a single bit: ")
print(test_3_flipped_1)
print("Flipping two bits in a row: ")
print(test_3_flipped_2)
print("Flipping four bits in a row: ")
print(test_3_flipped_4)