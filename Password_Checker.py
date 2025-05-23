import re

def check_password(password):
   
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password))
    is_long = len(password) >= 8

    failed = []
    if not is_long:
        failed.append("Password must be at least 8 characters long.")
    if not has_upper:
        failed.append("Password should include at least one uppercase letter.")
    if not has_lower:
        failed.append("Password should include at least one lowercase letter.")
    if not has_digit:
        failed.append("Password should include at least one digit.")
    if not has_special:
        failed.append("Password should include at least one special character.")

   
    if len(failed) == 0:
        strength = "Strong"
    elif len(failed) <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, failed


def main():
    print("🔑 Password Strength Checker 🔑")
    user_password = input("Enter your password: ")
    result, issues = check_password(user_password)

    print(f"\nPassword Level : {result}")
    if issues:
        print("Please fix the following:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print("Your password looks good!")


if __name__ == "__main__":
    main()
