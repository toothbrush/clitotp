#!/usr/bin/env python
import os
import sys
import time

import gnupg
import onetimepass as otp
import pyperclip

gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

my_secret_store_dir = os.path.expanduser('~/.totp')

user_wants = str(sys.argv[1])

secret_file = os.path.join(my_secret_store_dir, user_wants)

sys.stderr.write("Trying to decrypt {}... ".format(secret_file))

with open(secret_file, "rb") as f:
    my_secret = gpg.decrypt_file(f)
    my_secret = str(my_secret).strip()

sys.stderr.write("done.\n")

clock = time.time()
interval_length = 30
intervals_no = int(clock) // interval_length

seconds_validity_left = interval_length - int(clock) % interval_length

# Almost expired?  Go ahead and grab the next one.
if seconds_validity_left < 5:
    sys.stderr.write("Expires in %ds, skipping.\n" % seconds_validity_left)
    intervals_no += 1

# Pad to 6 digits.
my_token = "%06d" % otp.get_hotp(my_secret,
                                 intervals_no)

print "This token: %s" % my_token,
pyperclip.copy(my_token)
sys.stderr.write("Token copied to clipboard.\n")

next_token = otp.get_hotp(my_secret,
                          intervals_no+1)

sys.stderr.write("Next token: %06d\n" % next_token)
