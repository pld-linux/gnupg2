#!/bin/sh

if [ -r "${HOME}/.gnupg/gpg.conf" ]; then
    CFG="${HOME}/.gnupg/gpg.conf"
else
    CFG="${HOME}/.gnupg/options"
fi

X11=no
seahorse=no
if [ -r "${HOME}/.gnupg/gpg-agent.conf" ]; then
    grep -qE "^[[:blank:]]*pinentry-program[[:blank:]]*.*pinentry-(qt|qt4|gtk)" "${HOME}/.gnupg/gpg-agent.conf" && X11=yes
    grep -qE "^[[:blank:]]*pinentry-program[[:blank:]]*.*seahorse-agent" "${HOME}/.gnupg/gpg-agent.conf" && X11=yes && seahorse=yes
fi

if grep -q "^[[:blank:]]*use-agent" ${CFG} 2>/dev/null; then
    if [ -f "${HOME}/.gnupg/GPG_AGENT_INFO" ] && pid="$(cut -d: -f2 $HOME/.gnupg/GPG_AGENT_INFO)" && [ -n "$pid" ] && kill -0 "$pid"  2>/dev/null; then
	export GPG_AGENT_INFO="$(cat ${HOME}/.gnupg/GPG_AGENT_INFO)"
    else
	if [ -n "$DISPLAY" -a "$X11" = "yes" ] || [ -z "$DISPLAY" -a "$X11" = "no" ]; then
            if [ "$seahorse" = "no" ]; then
                eval "$(gpg-agent --daemon)"
            else
                eval "$(seahorse-agent --variables)"
            fi
	    echo $GPG_AGENT_INFO > ~/.gnupg/GPG_AGENT_INFO
	    export GPG_AGENT_INFO
	fi
    fi
fi
unset X11
unset CFG
unset pid
