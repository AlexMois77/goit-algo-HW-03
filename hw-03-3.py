import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\N",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    phone_number = str(phone_number)
    pattern = r"[;[\]\'\\\-:!\.\)\(\s]"
    replacement = ""
    clear_nambers = re.sub(pattern, replacement, phone_number)
    clear_nambers = re.sub("[a-z]|[A-Z]", replacement, clear_nambers)
    clear_nambers2 = clear_nambers.split(",")

    replacement2 = "+380"
    pattern2 = r"^380|^38|^0"

    sanitized_numbers = []

    for num in clear_nambers2:        
        sanitized_numbers.append(re.sub(pattern2, replacement2, num))
    return sanitized_numbers
print("Нормалізовані номери телефонів для SMS-розсилки:", (normalize_phone(raw_numbers)))
# print (sanitized_numbers)

