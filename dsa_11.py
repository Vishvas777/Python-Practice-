def reverse_string(s):
    stack = []

    # Push each character onto the stack
    for ch in s:
        stack.append(ch)

    # Pop characters to form the reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str


# Example usage
print(reverse_string("hello"))      # olleh
print(reverse_string("Python"))     # nohtyP
print(reverse_string("Stack"))      # kcatS