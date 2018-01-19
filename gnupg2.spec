#
# Conditional build:
%bcond_without	tests		# testsuite on build
%bcond_without	dirmngr		# dirmngr packages build
%bcond_with	default_gpg	# install as gpg/gpgv instead of gpg2/gpgv2
%bcond_with	gnutls		# GnuTLS instead of NTBTLS
%bcond_with	selinux		# "SELinux hacks"
#
Summary:	GNU Privacy Guard - tool for secure communication and data storage - enhanced version
Summary(pl.UTF-8):	GnuPG - narzędzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych - wersja rozszerzona
Name:		gnupg2
# 2.1.x is development version unfortunately (see gpg2 --version)
Version:	2.2.4
Release:	0.1
License:	GPL v3+
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2
# Source0-md5:	709e5af5bba84d251c520222e720972f
Source1:	gnupg-agent.sh
Patch0:		%{name}-info.patch
Patch1:		%{name}-pth.patch
Patch2:		%{name}-disable_tests.patch
Patch3:		%{name}-pl.po-update.patch
Patch4:		%{name}-am.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.14
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel >= 7.10
BuildRequires:	gettext-tools >= 0.17
%{?with_gnutls:BuildRequires:	gnutls-devel >= 3.0}
BuildRequires:	libassuan-devel >= 1:2.5.0
BuildRequires:	libgcrypt-devel >= 1.7.0
BuildRequires:	libgpg-error-devel >= 1.24
BuildRequires:	libksba-devel >= 1.3.4
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	npth-devel >= 1.2
%{!?with_gnutls:BuildRequires:	ntbtls-devel >= 0.1.0}
%{?with_dirmngr:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	gnupg2-common = %{version}-%{release}
Requires:	sqlite3 >= 3.7
%{?with_default_gpg:Obsoletes:	gnupg < 2}
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
Requires:	libassuan >= 1:2.0.0
Requires:	libgcrypt >= 1.5.0
Requires:	libgpg-error >= 1.11
Requires:	libksba >= 1.0.7
Conflicts:	gnupg-agent < 1.9.14-2

%description common
Common files used by tools from GnuPG project.

%description common -l pl.UTF-8
Pliki wspólne używane przez różne narzędzia z projektu GnuPG.

%package plugin-keys_curl
Summary:	GnuPG 2 plugin for allow talk to a HTTP/FTP keyserver
Summary(pl.UTF-8):	Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy HTTP/FTP
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}
Requires:	curl-libs >= 7.10

%description plugin-keys_curl
GnuPG 2 plugin for allow talk to a HTTP(S)/FTP(S) keyserver.

%description plugin-keys_curl -l pl.UTF-8
Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy
HTTP(S)/FTP(S).

%package plugin-keys_finger
Summary:	GnuPG 2 plugin for allow talk to a FINGER keyserver
Summary(pl.UTF-8):	Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy FINGER
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}

%description plugin-keys_finger
GnuPG 2 plugin for allow talk to a FINGER keyserver.

%description plugin-keys_finger -l pl.UTF-8
Wtyczka 2 GnuPG pozwalająca komunikować się z serwerem kluczy FINGER.

%package plugin-keys_hkp
Summary:	GnuPG 2 plugin for allow talk to a HKP keyserver
Summary(pl.UTF-8):	Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy HKP
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}

%description plugin-keys_hkp
GnuPG 2 plugin for allow talk to a HKP keyserver.

%description plugin-keys_hkp -l pl.UTF-8
Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy HKP.

%package plugin-keys_kdns
Summary:	GnuPG 2 plugin for allow talk to a KDNS keyserver
Summary(pl.UTF-8):	Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy KDNS
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}

%description plugin-keys_kdns
GnuPG 2 plugin for allow talk to a KDNS keyserver.

%description plugin-keys_kdns -l pl.UTF-8
Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy KDNS.

%package plugin-keys_ldap
Summary:	GnuPG 2 plugin for allow talk to a LDAP keyserver
Summary(pl.UTF-8):	Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy LDAP
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}

%description plugin-keys_ldap
GnuPG 2 plugin for allow talk to a LDAP keyserver.

%description plugin-keys_ldap -l pl.UTF-8
Wtyczka GnuPG 2 pozwalająca komunikować się z serwerem kluczy LDAP.

%package -n gnupg-agent
Summary:	GnuPG extension - agent
Summary(pl.UTF-8):	Rozszerzenie GnuPG - agent
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}
Requires:	pinentry >= 0.7.5-2
Obsoletes:	newpg

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
%patch0 -p1
%patch1 -p1
%{!?with_tests:%patch2 -p1}
%patch3 -p1
%patch4 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libexecdir=%{pkglibexecdir} \
	%{!?with_dirmngr:--disable-dirmngr} \
	--enable-g13 \
	%{!?with_default_gpg:--enable-gpg-is-gpg2} \
	%{?with_gnutls:--disable-ntbtls} \
	%{?with_selinux:--enable-selinux-support} \
	--enable-symcryptrun \
	--enable-wks-tools \
	--with-capabilities \
	--with-pinentry-pgm=%{_bindir}/pinentry \
	--with-mailprog=/usr/lib/sendmail

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
%endif

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/info/dir

# files useful for users packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gnupg

%find_lang gnupg2
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
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
%doc AUTHORS ChangeLog ChangeLog-2011 NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gpg-connect-agent
%attr(755,root,root) %{_bindir}/gpgconf
%attr(755,root,root) %{_bindir}/gpgkey2ssh
%attr(755,root,root) %{_bindir}/gpgparsemail
%attr(755,root,root) %{_bindir}/kbxutil
%attr(755,root,root) %{_bindir}/watchgnupg
%attr(755,root,root) %{_sbindir}/addgnupghome
%attr(755,root,root) %{_sbindir}/applygnupgdefaults
%attr(755,root,root) %{_sbindir}/g13-syshelp
%dir %{pkglibexecdir}

%{_datadir}/gnupg
%{_mandir}/man1/gpg-connect-agent.1*
%{_mandir}/man1/gpgconf.1*
%{_mandir}/man1/gpgparsemail.1*
%{_mandir}/man1/gpgtar.1*
%{_mandir}/man1/watchgnupg.1*
%{_mandir}/man8/addgnupghome.8*
%{_mandir}/man8/applygnupgdefaults.8*
%{_infodir}/gnupg.info*

%files plugin-keys_curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_curl

%files plugin-keys_finger
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_finger

%files plugin-keys_hkp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_hkp

%files plugin-keys_kdns
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_kdns

%files plugin-keys_ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_ldap

%files -n gnupg-smime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpgsm
%attr(755,root,root) %{_bindir}/gpgsm-gencert.sh
%{_mandir}/man1/gpgsm.1*
%{_mandir}/man1/gpgsm-gencert.sh.1*

%files -n gnupg-agent
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpg-agent
%attr(755,root,root) %{_bindir}/gpg-wks-server
%attr(755,root,root) %{_bindir}/symcryptrun
%attr(755,root,root) %{pkglibexecdir}/gpg-check-pattern
%attr(755,root,root) %{pkglibexecdir}/gpg-protect-tool
%attr(755,root,root) %{pkglibexecdir}/gpg-preset-passphrase
%attr(755,root,root) %{pkglibexecdir}/gpg-wks-client
%attr(755,root,root) %{pkglibexecdir}/scdaemon
%{_mandir}/man1/gpg-agent.1*
%{_mandir}/man1/gpg-preset-passphrase.1*
%{_mandir}/man1/gpg-wks-client.1*
%{_mandir}/man1/gpg-wks-server.1*
%{_mandir}/man1/scdaemon.1*
%{_mandir}/man1/symcryptrun.1*

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
