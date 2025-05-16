#
# Conditional build:
%bcond_without	tests		# testsuite on build
%bcond_without	dirmngr		# dirmngr packages build
%bcond_without	default_gpg	# install as gpg/gpgv instead of gpg2/gpgv2
%bcond_with	gnutls		# GnuTLS instead of NTBTLS
%bcond_with	selinux		# "SELinux hacks"
#
Summary:	GNU Privacy Guard - tool for secure communication and data storage - enhanced version
Summary(pl.UTF-8):	GnuPG - narzędzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych - wersja rozszerzona
Name:		gnupg2
# 2.4.x is stable, 2.5.x testing
Version:	2.4.8
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	https://www.gnupg.org/ftp/gcrypt/gnupg/gnupg-%{version}.tar.bz2
# Source0-md5:	a165b60aeaac0bb4d251117a45199c5f
Source1:	gnupg-agent.sh
Patch0:		%{name}-info.patch
Patch1:		%{name}-nogit.patch
Patch2:		%{name}-pl.po-update.patch
URL:		https://www.gnupg.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.16.3
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel >= 7.10
BuildRequires:	gettext-tools >= 0.21
%{?with_gnutls:BuildRequires:	gnutls-devel >= 3.2}
BuildRequires:	libassuan-devel >= 1:2.5.0
BuildRequires:	libgcrypt-devel >= 1.9.1
BuildRequires:	libgpg-error-devel >= 1.46
BuildRequires:	libksba-devel >= 1.6.3
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	npth-devel >= 1.2
%{!?with_gnutls:BuildRequires:	ntbtls-devel >= 0.2.0}
%{?with_dirmngr:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 2.011
BuildRequires:	sqlite3-devel >= 3.27
BuildRequires:	texinfo
BuildRequires:	tpm2-tss-devel
BuildRequires:	zlib-devel
Requires:	gnupg2-common = %{version}-%{release}
Requires:	sqlite3-libs >= 3.27
%if %{with default_gpg}
Obsoletes:	gnupg < 2
Obsoletes:	gnupg-plugin-keys_curl < 2
Obsoletes:	gnupg-plugin-keys_hkp < 2
Provides:	gnupg = %{version}-%{release}
%endif
Suggests:	gnupg-agent
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pkglibexecdir	%{_libexecdir}/gnupg2

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

This is enhanced version.

%description -l pl.UTF-8
GnuPG (GNU Privacy Guard) jest narzędziem do bezpiecznej komunikacji i
bezpiecznego przechowywania danych. Może być używany do szyfrowania
oraz podpisywania danych. Umożliwia zaawansowane zarządzanie kluczami
i spełnia normy zdefiniowane w standardzie OpenPGP, który jest opisany
w RFC2440.

To jest wersja rozszerzona.

%package common
Summary:	GnuPG - common files
Summary(pl.UTF-8):	GnuPG - pliki wspólne
Group:		Applications/File
Requires:	libassuan >= 1:2.5.0
Requires:	libgcrypt >= 1.9.1
Requires:	libgpg-error >= 1.46
Requires:	libksba >= 1.6.3
Requires:	npth >= 1.2
Obsoletes:	gnupg2-plugin-keys_curl < 2.1
Obsoletes:	gnupg2-plugin-keys_finger < 2.1
Obsoletes:	gnupg2-plugin-keys_hkp < 2.1
Obsoletes:	gnupg2-plugin-keys_kdns < 2.1
Obsoletes:	gnupg2-plugin-keys_ldap < 2.1
Conflicts:	gnupg < 1.4.18-2
Conflicts:	gnupg-agent < 1.9.14-2

%description common
Common files used by tools from GnuPG project.

%description common -l pl.UTF-8
Pliki wspólne używane przez różne narzędzia z projektu GnuPG.

%package -n gnupg-agent
Summary:	GnuPG extension - agent
Summary(pl.UTF-8):	Rozszerzenie GnuPG - agent
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}
Requires:	pinentry >= 0.7.5-2
Obsoletes:	newpg < 1

%description -n gnupg-agent
GnuPG extension - agent.

%description -n gnupg-agent -l pl.UTF-8
Rozszerzenie GnuPG - agent.

%package -n gnupg-agent-profile_d
Summary:	gnupg-agent start script for text mode
Summary(pl.UTF-8):	Skrypt startowy gnupg-agenta dla trybu tekstowego
Group:		Applications/File
Requires:	gnupg-agent = %{version}-%{release}

%description -n gnupg-agent-profile_d
gnupg-agent start script for text mode.

%description -n gnupg-agent-profile_d -l pl.UTF-8
Skrypt startowy gnupg-agenta dla trybu tekstowego.

%package -n gnupg-agent-xinitrc
Summary:	gnupg-agent start script for X-Window mode
Summary(pl.UTF-8):	Skrypt startowy gnupg-agenta dla trybu X-Window
Group:		Applications/File
Requires:	gnupg-agent = %{version}-%{release}
Requires:	xinitrc

%description -n gnupg-agent-xinitrc
gnupg-agent start script for X-Window mode.

%description -n gnupg-agent-xinitrc -l pl.UTF-8
Skrypt startowy gnupg-agenta dla trybu X-Window.

%package -n gnupg-smime
Summary:	GnuPG extension - S/MIME support
Summary(pl.UTF-8):	Rozszerzenie GnuPG - obsługa S/MIME
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}
Conflicts:	gnupg-agent < 1.9.14-2

%description -n gnupg-smime
GnuPG extension - S/MIME support.

%description -n gnupg-smime -l pl.UTF-8
Rozszerzenie GnuPG - obsługa S/MIME.

%package -n dirmngr
Summary:	X509/LDAP certificate and revocation list client
Summary(pl.UTF-8):	Klient certyfikatów i list anulujących X509/LDAP
Group:		Applications
Requires:	%{name}-common = %{version}-%{release}

%description -n dirmngr
DirMngr is a client for managing and downloading certificate
revocation lists (CRLs) for X509 certificates and for downloading the
certificates themselves. DirMngr is usually invoked by gpgsm and in
general not used directly.

%description -n dirmngr -l pl.UTF-8
DirMngr to klient do zarządzania i pobierania list anulujących
certyfikaty (CRLs - certificate revocation lists) dla certyfikatów
X509 oraz do pobierania samych certyfikatów. DirMngr jest zwykle
wywoływany przez gpgsm i nie używany bezpośrednio.

%prep
%setup -q -n gnupg-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
if (grep -q ^development_version=yes configure); then
	echo "configure incorrectly rebuild with messed up development status and likely version and revision." >&2
	echo "Consider fixing nogit.patch" >&2
	exit 1
fi

%configure \
	--libexecdir=%{pkglibexecdir} \
	%{!?with_dirmngr:--disable-dirmngr} \
	--enable-g13 \
	%{!?with_default_gpg:--enable-gpg-is-gpg2} \
	%{?with_gnutls:--disable-ntbtls} \
	%{?with_selinux:--enable-selinux-support} \
	%{!?with_tests:--disable-tests} \
	--enable-wks-tools \
	--with-capabilities \
	--with-pinentry-pgm=%{_bindir}/pinentry \
	--with-mailprog=/usr/lib/sendmail

# required for info rebuild
%{__make} -C doc defs.inc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkglibdir=%{_libexecdir}

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/profile.d/gnupg-agent.sh
install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/gnupg-agent.sh

%if %{without dirmngr}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{man1/dirmngr-client.1,man8/dirmngr.8}
%else
%endif

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/info/dir

# files useful for users packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gnupg

%find_lang gnupg2

%clean
rm -rf $RPM_BUILD_ROOT

%post	common -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	common -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%triggerpostun -n gnupg-agent -- gnupg-agent < 1.9.16-2
%banner gnupg-agent-1.9.16-2 << EOF
Scripts for starting gnupg-agent have been moved to separate
subpackages: gnupg-agent-profile_d and gnupg-agent-xinitrc.
EOF

%files
%defattr(644,root,root,755)
%if %{with default_gpg}
%attr(755,root,root) %{_bindir}/gpg
%attr(755,root,root) %{_bindir}/gpgv
%{_mandir}/man1/gpg.1*
%{_mandir}/man1/gpgv.1*
%else
%attr(755,root,root) %{_bindir}/gpg2
%attr(755,root,root) %{_bindir}/gpgv2
%{_mandir}/man1/gpg2.1*
%{_mandir}/man1/gpgv2.1*
%endif

%files common -f gnupg2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog ChangeLog-2011 NEWS README THANKS TODO doc/{DETAILS,FAQ,KEYSERVER,OpenPGP} doc/examples
%attr(755,root,root) %{_bindir}/g13
%attr(755,root,root) %{_bindir}/gpg-card
%attr(755,root,root) %{_bindir}/gpg-connect-agent
%attr(755,root,root) %{_bindir}/gpg-mail-tube
%attr(755,root,root) %{_bindir}/gpg-wks-client
%attr(755,root,root) %{_bindir}/gpgconf
%attr(755,root,root) %{_bindir}/gpgparsemail
%{?with_tests:%attr(755,root,root) %{_bindir}/gpgscm}
%attr(755,root,root) %{_bindir}/gpgsplit
%attr(755,root,root) %{_bindir}/gpgtar
%attr(755,root,root) %{_bindir}/kbxutil
%attr(755,root,root) %{_bindir}/watchgnupg
%attr(755,root,root) %{_sbindir}/addgnupghome
%attr(755,root,root) %{_sbindir}/applygnupgdefaults
%attr(755,root,root) %{_sbindir}/g13-syshelp
%dir %{pkglibexecdir}
%attr(755,root,root) %{pkglibexecdir}/gpg-auth
%attr(755,root,root) %{pkglibexecdir}/gpg-pair-tool
%attr(755,root,root) %{pkglibexecdir}/gpg-wks-client
%attr(755,root,root) %{pkglibexecdir}/keyboxd

%{_datadir}/gnupg
%{_mandir}/man1/gpg-card.1*
%{_mandir}/man1/gpg-connect-agent.1*
%{_mandir}/man1/gpg-mail-tube.1*
%{_mandir}/man1/gpg-wks-client.1*
%{_mandir}/man1/gpgconf.1*
%{_mandir}/man1/gpgparsemail.1*
%{_mandir}/man1/gpgtar.1*
%{_mandir}/man1/watchgnupg.1*
%{_mandir}/man7/gnupg.7*
%{_mandir}/man8/addgnupghome.8*
%{_mandir}/man8/applygnupgdefaults.8*
%{_infodir}/gnupg.info*

%files -n gnupg-smime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpgsm
%{_mandir}/man1/gpgsm.1*

%files -n gnupg-agent
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpg-agent
%attr(755,root,root) %{_bindir}/gpg-wks-server
%attr(755,root,root) %{pkglibexecdir}/gpg-check-pattern
%attr(755,root,root) %{pkglibexecdir}/gpg-protect-tool
%attr(755,root,root) %{pkglibexecdir}/gpg-preset-passphrase
%attr(755,root,root) %{pkglibexecdir}/scdaemon
%attr(755,root,root) %{pkglibexecdir}/tpm2daemon
%{_mandir}/man1/gpg-agent.1*
%{_mandir}/man1/gpg-check-pattern.1*
%{_mandir}/man1/gpg-preset-passphrase.1*
%{_mandir}/man1/gpg-wks-server.1*
%{_mandir}/man1/scdaemon.1*

%files -n gnupg-agent-profile_d
%defattr(644,root,root,755)
%attr(755,root,root) /etc/profile.d/gnupg-agent.sh

%files -n gnupg-agent-xinitrc
%defattr(644,root,root,755)
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/gnupg-agent.sh

%if %{with dirmngr}
%files -n dirmngr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dirmngr
%attr(755,root,root) %{_bindir}/dirmngr-client
%attr(755,root,root) %{pkglibexecdir}/dirmngr_ldap
%{_mandir}/man1/dirmngr-client.1*
%{_mandir}/man8/dirmngr.8*
%endif
