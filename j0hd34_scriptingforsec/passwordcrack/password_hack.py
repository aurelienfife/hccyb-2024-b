# Open the credentials CSV
# Go through leaked hashes

# For each of the hashes, compare with hashed password from dictionary

import hashlib

credentials = { }

def load_credentials():
    # First load all the usernames and password in a dict
    f = open("leakedcredentials.csv")

    for line in f:
        # Remove the extra whitespace
        line = line.strip() # Remove the extra newline characters    
        # Split on ,
        split_line = line.split(",")
        # Use element 0 as key and element 1 as value
        credentials[split_line[0]] = split_line[1]

    f.close()

def check_passwords():
    # Get dictionary keys sorted alphabetically in a list
    usernames = sorted(credentials.keys())    # keys in alphabetical order
    print(usernames)

    # Main loop - going through the usernames
    for userid in usernames:
        print("Checking password for", userid)

        print("Checking the 10K most common")
        f = open("10k-most-common.txt")

        for passwd in f:
            passwd = passwd.strip() # Remove new line
            # Match password with hash
            if match_passwd(passwd, credentials[userid]):
                print("Password found: ", passwd)
                break
        # print("Password not found in 10K most common")
        f.close()

def match_passwd(clear_password, known_hash):
    # Encode the clear password to hex
    clear_bytes = clear_password.encode('utf-8')
    # Hash the numerical value
    pass_hash = hashlib.sha256(clear_bytes)
    # Extract the hex value of the hash into a string
    hex_hash = pass_hash.hexdigest()

    # Compare
    if hex_hash == known_hash:
        return True
    else:
        return False

def main():
    load_credentials()
    check_passwords()

if __name__ == "__main__":
    main()
