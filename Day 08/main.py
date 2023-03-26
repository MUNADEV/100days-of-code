from art import logo

def get_user_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid input. Please enter 'encode' or 'decode': ")
        return get_user_input()
    
    message = input("Enter your message: ")
    if not message.isalpha():
        print("Invalid input. Message must only contain letters.")
        return get_user_input()
    
    shift = input("Enter the shift number: ")
    if not shift.isdigit():
        print("Invalid input. Shift must be a positive integer.")
        return get_user_input()
    
    return direction, message, int(shift)

def caesar(message, shift, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #26
    if direction == 'decode':
        shift = -shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translated_message = ''.join([shifted_alphabet[alphabet.index(letter)] if letter in alphabet else letter for letter in message])
    return translated_message

print(logo)
should_end = False
while not should_end:
    direction, message, shift = get_user_input()
    shift = shift % 26
    translated_message = caesar(message, shift, direction)
    print(f"Here's the {direction}d message: {translated_message}")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    should_end = (restart == 'no') #conditional
print("Goodbye!")
