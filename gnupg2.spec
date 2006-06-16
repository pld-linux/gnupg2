#
# Conditional build:
%bcond_without	pth	# without pth-based based version of gnupg
#
Summary:	GNU Privacy Guard - tool for secure communication and data storage - development version
Summary(pl):	GnuPG - narzêdzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych - wersja rozwojowa
Name:		gnupg2
Version:	1.9.20
Release:	2
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/gnupg/gnupg-%{version}.tar.bz2
# Source0-md5:	93899203fc0530f03e146d49b65c1e28
Source1:	gnupg-agent.sh
Patch0:		%{name}-info.patch
Patch1:		%{name}-pth.patch
URL:		http://www.gnupg.org/
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	libassuan-devel >= 1:0.6.10
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libgpg-error-devel >= 1.0
BuildRequires:	libksba-devel >= 0.9.13
BuildRequires:	libusb-devel
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
GnuPG (GNU Privacy Guard) jest narzêdziem do bezpiecznej komunikacji i
bezpiecznego przechowywania danych. Mo¿e byæ u¿ywany do szyfrowania
oraz podpisywania danych. Umo¿liwia zaawansowane zarz±dzanie kluczami
i spe³nia normy zdefiniowane w standardzie OpenPGP, który jest opisany
w RFC2440.

Wersja rozwojowa. Nie do u¿ytku z kluczami produkcyjnymi.

%package common
Summary:	GnuPG - common files
Summary(pl):	GnuPG - pliki wspólne
Group:		Applications/File
Requires:	libgpg-error >= 1.0
Conflicts:	gnupg-agent < 1.9.14-2

%description common
Common files used by tools from GnuPG project.

%description common -l pl
Pliki wspólne u¿ywane przez ró¿ne narzêdzia z projektu GnuPG.

%package -n gnupg-agent
Summary:	GnuPG extension - agent
Summary(pl):	Rozszerzenie GnuPG - agent
Group:		Applications/File
Requires:	gnupg2-common = %{version}-%{release}
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
Summary(pl):	Rozszerzenie GnuPG - obs³uga S/MIME
Group:		Applications/File
Requires:	gnupg2-common = %{version}-%{release}
Conflicts:	gnupg-agent < 1.9.14-2

%description -n gnupg-smime
GnuPG extension - S/MIME support.

%description -n gnupg-smime -l pl
Rozszerzenie GnuPG - obs³uga S/MIME.

%prep
%setup -q -n gnupg-%{version}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* scripts
%configure \
	--with-capabilities \
	%{!?with_pth:--disable-threads} \
	--enable-gpg \
%ifarch sparc sparc64
	--disable-m-guard \
%else
	--enable-m-guard \
%endif
	--without-included-gettext \
	--disable-m-debug \
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

%files common -f gnupg2.lang
%defattr(644,root,root,755)
%doc AUTHORS main-ChangeLog NEWS README THANKS TODO
%doc intl-ChangeLog jnlib-ChangeLog m4-ChangeLog po-ChangeLog scripts-ChangeLog common-ChangeLog kbx-ChangeLog tools-ChangeLog doc-ChangeLog
%attr(755,root,root) %{_bindir}/gpg-connect-agent
%attr(755,root,root) %{_bindir}/gpgconf
%attr(755,root,root) %{_bindir}/gpgkey2ssh
%attr(755,root,root) %{_bindir}/gpgparsemail
%attr(755,root,root) %{_bindir}/watchgnupg
%attr(755,root,root) %{_sbindir}/addgnupghome
%attr(755,root,root) %{_bindir}/kbxutil
%{_datadir}/gnupg
%{_infodir}/*info*

%files -n gnupg-smime
%defattr(644,root,root,755)
%doc sm-ChangeLog
%attr(755,root,root) %{_bindir}/gpgsm
%attr(755,root,root) %{_bindir}/gpgsm-gencert.sh

%files -n gnupg-agent
%defattr(644,root,root,755)
%doc agent-ChangeLog scd-ChangeLog
%attr(755,root,root) %{_bindir}/gpg-agent
%attr(755,root,root) %{_bindir}/scdaemon
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gpg-protect-tool
%attr(755,root,root) %{_libexecdir}/gpg-preset-passphrase
%attr(755,root,root) %{_libexecdir}/pcsc-wrapper

%files -n gnupg-agent-profile_d
%defattr(644,root,root,755)
%attr(755,root,root) /etc/profile.d/gnupg-agent.sh

%files -n gnupg-agent-xinitrc
%defattr(644,root,root,755)
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/gnupg-agent.sh
