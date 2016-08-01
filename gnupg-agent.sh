#!/bin/sh

if [ -r "${HOME}/.gnupg/gpg.conf" ]; then
	CFG="${HOME}/.gnupg/gpg.conf"
else
	CFG="${HOME}/.gnupg/options"
fi

seahorse=no
if [ -r "${HOME}/.gnupg/gpg-agent.conf" ]; then
	grep -qE "^[[:blank:]]*pinentry-program[[:blank:]]*.*seahorse-agent" "${HOME}/.gnupg/gpg-agent.conf" && seahorse=yes
fi

if grep -q "^[[:blank:]]*use-agent" ${CFG} 2>/dev/null; then
	if [ -f "${HOME}/.gnupg/GPG_AGENT_INFO" ] && \
			pid="$(cut -d: -f2 $HOME/.gnupg/GPG_AGENT_INFO)" && \
			[ "$(resolvesymlink "/proc/$pid/exe")" = "/usr/bin/gpg-agent" ]; then
		export GPG_AGENT_INFO="$(cat ${HOME}/.gnupg/GPG_AGENT_INFO)"
	else
		if [ "$seahorse" = "no" ]; then
			eval "$(gpg-agent --daemon)"
		else
			eval "$(seahorse-agent --variables)"
		fi
		echo $GPG_AGENT_INFO > ~/.gnupg/GPG_AGENT_INFO
		export GPG_AGENT_INFO
	fi
fi
unset CFG
unset pid
