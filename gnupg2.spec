#
# Conditional build:
%bcond_without	pth	# without pth-based based version of gnupg
%bcond_without	tests	# testsuite on build
#
Summary:	GNU Privacy Guard - tool for secure communication and data storage - development version
Summary(pl):	GnuPG - narz�dzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych - wersja rozwojowa
Name:		gnupg2
Version:	2.0.3
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2
# Source0-md5:	4e33a5d35583da439f1bd26aa7e7042a
Source1:	gnupg-agent.sh
Patch0:		%{name}-info.patch
Patch1:		%{name}-pth.patch
Patch2:		%{name}-pl.po-update.patch
Patch3:		%{name}-disable_tests.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.3
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel >= 0.15
BuildRequires:	libassuan-devel >= 1:0.9.3
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libgpg-error-devel >= 1.4
BuildRequires:	libksba-devel >= 1.0.0
BuildRequires:	libusb-devel
BuildRequires:	openldap-devel
BuildRequires:	pcsc-lite-devel
%{?with_pth:BuildRequires:	pth-devel >= 2.0.0}
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	gnupg2-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnupg2

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

This is development version. Don't use it with production keys.

%description -l pl
GnuPG (GNU Privacy Guard) jest narz�dziem do bezpiecznej komunikacji i
bezpiecznego przechowywania danych. Mo�e by� u�ywany do szyfrowania
oraz podpisywania danych. Umo�liwia zaawansowane zarz�dzanie kluczami
i spe�nia normy zdefiniowane w standardzie OpenPGP, kt�ry jest opisany
w RFC2440.

Wersja rozwojowa. Nie do u�ytku z kluczami produkcyjnymi.

%package common
Summary:	GnuPG - common files
Summary(pl):	GnuPG - pliki wsp�lne
Group:		Applications/File
Requires:	libassuan >= 1:0.9.3
Requires:	libgpg-error >= 1.4
Conflicts:	gnupg-agent < 1.9.14-2

%description common
Common files used by tools from GnuPG project.

%description common -l pl
Pliki wsp�lne u�ywane przez r�ne narz�dzia z projektu GnuPG.

%package plugin-keys_curl
Summary:	GnuPG 2 plugin for allow talk to a HTTP/FTP keyserver
Summary(pl):	Wtyczka GnuPG 2 pozwalaj�ca komunikowa� si� z serwerem kluczy HTTP/FTP
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}

%description plugin-keys_curl
GnuPG 2 plugin for allow talk to a HTTP(S)/FTP(S) keyserver.

%description plugin-keys_curl -l pl
Wtyczka GnuPG 2 pozwalaj�ca komunikowa� si� z serwerem kluczy
HTTP(S)/FTP(S).

%package plugin-keys_finger
Summary:	GnuPG 2 plugin for allow talk to a FINGER keyserver
Summary(pl):	Wtyczka GnuPG 2 pozwalaj�ca komunikowa� si� z serwerem kluczy FINGER
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}

%description plugin-keys_finger
GnuPG 2 plugin for allow talk to a FINGER keyserver.

%description plugin-keys_finger -l pl
Wtyczka 2 GnuPG pozwalaj�ca komunikowa� si� z serwerem kluczy FINGER.

%package plugin-keys_hkp
Summary:	GnuPG 2 plugin for allow talk to a HKP keyserver
Summary(pl):	Wtyczka GnuPG 2 pozwalaj�ca komunikowa� si� z serwerem kluczy HKP
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}

%description plugin-keys_hkp
GnuPG 2 plugin for allow talk to a HKP keyserver.

%description plugin-keys_hkp -l pl
Wtyczka GnuPG 2 pozwalaj�ca komunikowa� si� z serwerem kluczy HKP.

%package plugin-keys_ldap
Summary:	GnuPG 2 plugin for allow talk to a LDAP keyserver
Summary(pl):	Wtyczka GnuPG 2 pozwalaj�ca komunikowa� si� z serwerem kluczy LDAP
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}

%description plugin-keys_ldap
GnuPG 2 plugin for allow talk to a LDAP keyserver.

%description plugin-keys_ldap -l pl
Wtyczka GnuPG 2 pozwalaj�ca komunikowa� si� z serwerem kluczy LDAP.

%package -n gnupg-agent
Summary:	GnuPG extension - agent
Summary(pl):	Rozszerzenie GnuPG - agent
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}
Requires:	pinentry
Obsoletes:	newpg

%description -n gnupg-agent
GnuPG extension - agent.

%description -n gnupg-agent -l pl
Rozszerzenie GnuPG - agent.

%package -n gnupg-agent-profile_d
Summary:	gnupg-agent start script for text mode
Summary(pl):	Skrypt startowy gnupg-agenta dla trybu tekstowego
Group:		Applications/File
Requires:	gnupg-agent = %{version}-%{release}

%description -n gnupg-agent-profile_d
gnupg-agent start script for text mode.

%description -n gnupg-agent-profile_d -l pl
Skrypt startowy gnupg-agenta dla trybu tekstowego.

%package -n gnupg-agent-xinitrc
Summary:	gnupg-agent start script for X-Window mode
Summary(pl):	Skrypt startowy gnupg-agenta dla trybu X-Window
Group:		Applications/File
Requires:	gnupg-agent = %{version}-%{release}
Requires:	xinitrc

%description -n gnupg-agent-xinitrc
gnupg-agent start script for X-Window mode.

%description -n gnupg-agent-xinitrc -l pl
Skrypt startowy gnupg-agenta dla trybu X-Window.

%package -n gnupg-smime
Summary:	GnuPG extension - S/MIME support
Summary(pl):	Rozszerzenie GnuPG - obs�uga S/MIME
Group:		Applications/File
Requires:	%{name}-common = %{version}-%{release}
Conflicts:	gnupg-agent < 1.9.14-2

%description -n gnupg-smime
GnuPG extension - S/MIME support.

%description -n gnupg-smime -l pl
Rozszerzenie GnuPG - obs�uga S/MIME.

%prep
%setup -q -n gnupg-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{!?with_tests:%patch3 -p1}

rm -f po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_pth:--disable-threads} \
	--enable-gpg \
	--enable-symcryptrun \
	--with-capabilities \
	--with-mailprog=/usr/lib/sendmail

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkglibdir=%{_libexecdir}

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/profile.d/gnupg-agent.sh
install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/gnupg-agent.sh

mv ChangeLog main-ChangeLog || :
find . -name ChangeLog |awk '{src=$0; dst=$0;sub("^./","",dst);gsub("/","-",dst); print "cp " src " " dst}'|sh

%find_lang gnupg2
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%triggerpostun -n gnupg-agent -- gnupg-agent < 1.9.16-2
%banner gnupg-agent-1.9.16-2 << EOF
Scripts for starting gnupg-agent have been moved to separate
subpackages: gnupg-agent-profile_d and gnupg-agent-xinitrc.
EOF

%files
%defattr(644,root,root,755)
%doc g10-ChangeLog g10/options.skel
%attr(755,root,root) %{_bindir}/gpg2
%attr(755,root,root) %{_bindir}/gpgv2
%{_mandir}/man1/gpg2.1*
%{_mandir}/man1/gpgv2.1*

%files common -f gnupg2.lang
%defattr(644,root,root,755)
%doc AUTHORS main-ChangeLog NEWS README THANKS TODO
%doc intl-ChangeLog jnlib-ChangeLog m4-ChangeLog po-ChangeLog scripts-ChangeLog common-ChangeLog kbx-ChangeLog tools-ChangeLog doc-ChangeLog
%attr(755,root,root) %{_bindir}/gpg-connect-agent
%attr(755,root,root) %{_bindir}/gpgconf
%attr(755,root,root) %{_bindir}/gpgkey2ssh
%attr(755,root,root) %{_bindir}/gpgparsemail
%attr(755,root,root) %{_bindir}/kbxutil
%attr(755,root,root) %{_bindir}/watchgnupg
%attr(755,root,root) %{_sbindir}/addgnupghome
%attr(755,root,root) %{_sbindir}/applygnupgdefaults
%dir %{_libexecdir}
%{_datadir}/gnupg
%{_mandir}/man1/gpg-connect-agent.1*
%{_mandir}/man1/gpgconf.1*
%{_mandir}/man1/gpgparsemail.1*
%{_mandir}/man1/watchgnupg.1*
%{_mandir}/man8/addgnupghome.8*
%{_mandir}/man8/applygnupgdefaults.8*
%{_infodir}/*.info*

%files plugin-keys_curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_curl

%files plugin-keys_finger
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_finger

%files plugin-keys_hkp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_hkp

%files plugin-keys_ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gpg2keys_ldap

%files -n gnupg-smime
%defattr(644,root,root,755)
%doc sm-ChangeLog
%attr(755,root,root) %{_bindir}/gpgsm
%attr(755,root,root) %{_bindir}/gpgsm-gencert.sh
%{_mandir}/man1/gpgsm.1*
%{_mandir}/man1/gpgsm-gencert.sh.1*

%files -n gnupg-agent
%defattr(644,root,root,755)
%doc agent-ChangeLog scd-ChangeLog
%attr(755,root,root) %{_bindir}/gpg-agent
%attr(755,root,root) %{_bindir}/scdaemon
%attr(755,root,root) %{_bindir}/symcryptrun
%attr(755,root,root) %{_libexecdir}/gnupg-pcsc-wrapper
%attr(755,root,root) %{_libexecdir}/gpg-protect-tool
%attr(755,root,root) %{_libexecdir}/gpg-preset-passphrase
%{_mandir}/man1/gpg-agent.1*
%{_mandir}/man1/gpg-preset-passphrase.1*
%{_mandir}/man1/scdaemon.1*
%{_mandir}/man1/symcryptrun.1*

%files -n gnupg-agent-profile_d
%defattr(644,root,root,755)
%attr(755,root,root) /etc/profile.d/gnupg-agent.sh

%files -n gnupg-agent-xinitrc
%defattr(644,root,root,755)
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/gnupg-agent.sh
