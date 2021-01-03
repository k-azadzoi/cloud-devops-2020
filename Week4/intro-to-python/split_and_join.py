#   Simple function to split and join a string

def split_and_join(str):
    split_str = str.split(" ")  # string will be split after each space
    joined_str = "-".join(split_str)    # This will join the hyphen to each space in the split_str
    return joined_str

print(split_and_join("The quick and brown fox jumped over the bridge"))

