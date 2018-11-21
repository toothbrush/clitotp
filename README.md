# clitotp

This is a very hacky script to generate TOTPs on the CLI in a way that
i understand and can manage.  It puts the data where i want it,
encrypted with GnuPG.  This will probably not be suitable for your
needs, but it scratches my itch.  I encourage you to look at one of
the many other superb CLI TOTP utilities out there if this is too
rough and ready for you.

# Instructions for the impatient

You need Python.  You'll want to install the dependencies in the
`requirements.txt` file.  This worked for me:

```ShellSession
$ cd src/clitotp
$ virtualenv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
```

## Using the tool

You'll want to start by inserting a secret into the database.  The
file locations are hard-coded, deal with it.  The only argument these
scripts take (for now) is the name of the TOTP thing.  Probably the
website or app name is a good choice here.

```ShellSession
$ ./create.py github
Will insert into: /Users/yourfineface/.totp/github.gpg
Give me the secret (C-c cancels): aaaa bbbb cccc dddd
Encrypted and saved.
```

When it comes time for a site to nag you about 2FA, you can call up
the relevant thing like so:

```ShellSession
$ ./totp.py github.gpg
Trying to decrypt /Users/yourfineface/.totp/github.gpg... done.
This token: 164160 (copied)
Next token: 440926
```

Note that it'll place the current TOTP on your clipboard, ready for
pasting wherever.  It'll also check whether the token is about to
expire, and if it is, move on to that one instead (each one is valid
for 30s, and every time `epoch time % 30 == 0` they roll over).  It
also helpfully prints the next-up token, in case you're verifying a
new service and it wants two passwords for extra super duper security.

# Appendix: completion

I am a lazy person, so can't be bothered remembering or typing the
names of my TOTP secrets.  This bit of zsh made completions work for
me.  It may help you, too.

```zsh
compdef _totp_files totp.py

function _totp_files () {
    _arguments '1:site name:_totp_sites'
}

function _totp_sites () {
    local store_dir=~/.totp
    _files -W ${store_dir} -g '*.gpg'
}
```

Peace, love, and vegetables, or something like that. 🌽
