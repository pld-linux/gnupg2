#!/bin/sh

if [ -r "${HOME}/.gnupg/gpg.conf" ]; then
	CFG="${HOME}/.gnupg/gpg.conf"
else
	CFG="${HOME}/.gnupg/options"
fi

if grep -q "^[[:blank:]]*use-agent" ${CFG} 2>/dev/null; then
	/usr/bin/gpgconf --launch gpg-agent
fi

unset CFG
