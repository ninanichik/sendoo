import random
import string


class EmailsGeneration:
    def creating_full_email(self):
        first_part_of_email = str("".join(random.choice(string.ascii_letters) for _ in range(7)))
        return "".join(list(first_part_of_email + "@mailinator.com"))

    def creating_random_password(self):
        letters = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        digits = ''.join(random.choice(string.digits) for _ in range(2))
        all_password = letters + digits
        return str(''.join(all_password))