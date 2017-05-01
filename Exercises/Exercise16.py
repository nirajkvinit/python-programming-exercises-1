# Simplified version for 16 char passwords w/ numbers and letters

# Unnecessary complicated version w/ some options is in folder password-generator

import string, random

allowed_characters = string.ascii_letters + string.digits

password = ""

for i in range(16):
    password += allowed_characters[random.randint(0, len(allowed_characters) - 1)]

print("\nYour new password is : %s" % password)