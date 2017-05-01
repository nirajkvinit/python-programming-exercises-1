import string, random

easy = ["12345", "password", "admin", "54321", "horse", "cat", "dog", "lmao"]
medium = string.ascii_letters + string.digits
strong = string.ascii_letters + string.digits + "!#%&.()=?$[]{}"


def generate_password(strength="medium"):

    easy_password = easy[random.randint(0, len(easy) - 1)]
    medium_password = ""
    strong_password = ""

    for i in range(0, 8):
        medium_password += (medium[random.randint(0, len(medium) - 1)])

    for i in range(0, 16):
        strong_password += (strong[random.randint(0, len(strong) - 1)])

    if strength == "easy":
        return easy_password
    elif strength == "medium":
        return medium_password
    else:
        return strong_password
