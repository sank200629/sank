import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = [
    "Cool", "Happy", "Fierce", "Brave", "Witty", "Charming", "Bright", "Loyal", "Silent", "Swift"
]
nouns = [
    "Tiger", "Dragon", "Phoenix", "Lion", "Wolf", "Hawk", "Panda", "Falcon", "Bear", "Eagle"
]

# Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True, username_length=None):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)

    # Combine adjective and noun
    base_name = adj + noun

    # Add numbers and/or special characters
    if include_numbers:
        base_name += str(random.randint(10, 99))  # Add random 2-digit number

    if include_special_chars:
        base_name += random.choice("!@#$%^&*")

    # Adjust username length if specified
    if username_length and username_length > len(base_name):
        extra_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=(username_length - len(base_name))))
        base_name += extra_chars

    return base_name

# Function to save usernames to a file
def save_usernames_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "w") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"Usernames successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

# Main program logic
def main():
    print("Welcome to the Random Username Generator!")
    
    try:
        num_usernames = int(input("How many usernames would you like to generate? "))
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
        username_length = input("Specify username length (leave blank for default): ").strip()
        username_length = int(username_length) if username_length.isdigit() else None

        usernames = []
        for _ in range(num_usernames):
            usernames.append(generate_username(include_numbers, include_special_chars, username_length))

        print("\nGenerated Usernames:")
        for username in usernames:
            print(username)

        # Save to file
        save_option = input("\nWould you like to save the usernames to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            save_usernames_to_file(usernames)

    except ValueError:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
