def validate_email(email):
    # Check if the first character is a letter
    if not email[0].isalpha():
        return False
      
    # Check if email length is between 5 and 30 characters
    if len(email) < 5 or len(email) > 30:
        return False
    
    # Check if email includes '@'
    at_index = email.find('@')
    if at_index == -1:
        return False
    
    # Check if there is at least one '.' after '@'
    dot_index = email.find('.', at_index)
    if dot_index == -1:
        return False
    
    return True

# variables
email = input('Enter your email: ')
result = validate_email(email)

print(result)

validate_email(email)