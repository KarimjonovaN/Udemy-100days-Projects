# with open("/Users/navruza/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

number = 10
binary_data = number.to_bytes(1, byteorder='big')  # Convert to 1 byte

with open('new_file.txt', 'ab') as f:  # 'ab' = append binary
    f.write(binary_data)

with open('new_file.txt', 'rb') as f:
    print(f.read())  # This will include your appended byte