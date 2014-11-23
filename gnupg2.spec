# TODO: ntbtls instead of gnutls (when released)?
#
# Conditional build:
%bcond_without	tests	# testsuite on build
%bcond_with	selinux	# "SELinux hacks"
#
Summary:	GNU Privacy Guard - tool for secure communication and data storage - enhanced version
Summary(pl.UTF-8):	GnuPG - narzędzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych - wersja rozszerzona
Name:		gnupg2
# 2.1.x is development version unfortunately (see gpg2 --version)
Version:	2.1.0
Release:	1.1
License:	GPL v3+
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2
# Source0-md5:	43a809789a1d897f4386680be0b09d02
Source1:	gnupg-agent.sh
Patch0:		%{name}-info.patch

Patch2:		%{name}-disable_tests.patch
Patch3:		%{name}-pl.po-update.patch
Patch4:		%{name}-am.patch
URL:		http://www.gnupg.org/
BuildRequires:	adns-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel >= 7.10
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gnutls-devel >= 3.0
BuildRequires:	libassuan-devel >= 1:2.0.0
BuildRequires:	libgcrypt-devel >= 1.6.0
BuildRequires:	libgpg-error-devel >= 1.15
BuildRequires:	libksba-devel >= 1.2.0
BuildRequires:	libusb-compat-devel >= 0.1
BuildRequires:	npth-devel >= 1.1
# only for dirmngr, which is not built here
#BuildRequires:	openldap-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	gnupg2-common = %{version}-%{release}
Suggests:	gnupg-agent
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnupg2

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
Requires:	libgcrypt >= 1.6.0
Requires:	libgpg-error >= 1.15
Requires:	libksba >= 1.2.0
Requires:	npth >= 1.1
Obsoletes:	gnupg2-plugin-keys_curl
Obsoletes:	gnupg2-plugin-keys_finger
Obsoletes:	gnupg2-plugin-keys_hkp
Obsoletes:	gnupg2-plugin-keys_kdns
Obsoletes:	gnupg2-plugin-keys_ldap
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

%prep
%setup -q -n gnupg-%{version}
%patch0 -p1

%{!?with_tests:%patch2 -p1}
#%patch3 -p1
%patch4 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-dirmngr \
	--enable-gpg \
	%{?with_selinux:--enable-selinux-support} \
	--enable-symcryptrun \
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

# non-existing program
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/gpg-zip.1
# see dirmngr package
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{man1/dirmngr-client.1,man8/dirmngr.8}

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%find_lang gnupg2

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
%doc g10/options.skel
%attr(755,root,root) %{_bindir}/gpg2
%attr(755,root,root) %{_bindir}/gpgv2
%{_mandir}/man1/gpg2.1*
%{_mandir}/man1/gpgv2.1*

%files common -f gnupg2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog ChangeLog-2011 NEWS README THANKS TODO doc/{DETAILS,FAQ,KEYSERVER,OpenPGP}
%attr(755,root,root) %{_bindir}/g13
%attr(755,root,root) %{_bindir}/gpg-connect-agent
%attr(755,root,root) %{_bindir}/gpgconf
%attr(755,root,root) %{_bindir}/gpgkey2ssh
%attr(755,root,root) %{_bindir}/gpgparsemail
%attr(755,root,root) %{_bindir}/gpgtar
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
%{_mandir}/man7/gnupg.7*
%{_mandir}/man8/addgnupghome.8*
%{_mandir}/man8/applygnupgdefaults.8*
%{_infodir}/gnupg.info*

%files -n gnupg-smime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpgsm
%attr(755,root,root) %{_bindir}/gpgsm-gencert.sh
%{_mandir}/man1/gpgsm.1*
%{_mandir}/man1/gpgsm-gencert.sh.1*

%files -n gnupg-agent
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpg-agent
%attr(755,root,root) %{_bindir}/symcryptrun
%attr(755,root,root) %{_libexecdir}/gpg-check-pattern
%attr(755,root,root) %{_libexecdir}/gpg-protect-tool
%attr(755,root,root) %{_libexecdir}/gpg-preset-passphrase
%attr(755,root,root) %{_libexecdir}/scdaemon
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
