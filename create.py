#!/usr/bin/env python3
import os
import sys

import gnupg

gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

my_secret_store_dir = os.path.expanduser('~/.totp')

user_wants = str(sys.argv[1])

secret_file = os.path.join(my_secret_store_dir, user_wants + '.gpg')

print(f"Will insert into: {secret_file}")

my_secret = input("Give me the secret (C-c cancels): ")

recipients = ['0xF2846B1A0D32C442']
encrypted_secret = gpg.encrypt(my_secret, recipients)

with open(secret_file, "wb") as f:
    f.write(str(encrypted_secret).encode())

print("Encrypted and saved.")
