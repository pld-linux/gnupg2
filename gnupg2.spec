#
# Conditional build:
%bcond_without	xinitrc	# don't use xinitrc's directory
%bcond_without	pth	# without pth-based based version of gnupg
#
Summary:	GNU Privacy Guard - tool for secure communication and data storage - development version
Summary(pl):	GnuPG - narzêdzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych - wersja rozwojowa
Name:		gnupg2
Version:	1.9.15
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/gnupg/gnupg-%{version}.tar.gz
# Source0-md5:	c1955d88280ff6e847f82f37b9a9a008
Source1:	gnupg-agent.sh
Patch0:		%{name}-info.patch
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	libassuan-devel >= 1:0.6.9
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libgpg-error-devel >= 0.6
BuildRequires:	libksba-devel >= 0.9.7
BuildRequires:	pcsc-lite-devel
BuildRequires:	opensc-devel >= 0.8.0
%{?with_pth:BuildRequires:	pth-devel >= 2.0.0}
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
%{?with_xinitrc:Requires: xinitrc}
Obsoletes:	newpg

%description -n gnupg-agent
GnuPG extension - agent.

%description -n gnupg-agent -l pl
Rozszerzenie GnuPG - agent.

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

%build
cp -f /usr/share/automake/config.* scripts
%configure \
	--with-capabilities \
	%{!?with_pth:--disable-threads} \
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
install -d $RPM_BUILD_ROOT/etc/profile.d
%{?with_xinitrc:install -d $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkglibdir=%{_libexecdir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/profile.d/gnupg-agent.sh
%{?with_xinitrc:ln -sf /etc/profile.d/gnupg-agent.sh $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/gnupg-agent.sh}

mv ChangeLog main-ChangeLog || :
find . -name ChangeLog |awk '{src=$0; dst=$0;sub("^./","",dst);gsub("/","-",dst); print "cp " src " " dst}'|sh

%find_lang gnupg2

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files 
%defattr(644,root,root,755)
%doc g10-ChangeLog g10/options.skel
%attr(755,root,root) %{_bindir}/gpg2
%attr(755,root,root) %{_bindir}/gpgv2

%files common -f gnupg2.lang
%defattr(644,root,root,755)
%doc AUTHORS main-ChangeLog NEWS README THANKS TODO 
%doc intl-ChangeLog jnlib-ChangeLog m4-ChangeLog po-ChangeLog scripts-ChangeLog common-ChangeLog kbx-ChangeLog tools-ChangeLog doc-ChangeLog
%attr(755,root,root) %{_bindir}/gpgconf
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
%attr(755,root,root) %{_bindir}/sc-copykeys
%attr(755,root,root) %{_bindir}/scdaemon
%attr(755,root,root) %{_libexecdir}/gpg-protect-tool
%attr(755,root,root) %{_libexecdir}/gpg-preset-passphrase
%attr(755,root,root) %{_libexecdir}/pcsc-wrapper
%attr(755,root,root) /etc/profile.d/gnupg-agent.sh
%{?with_xinitrc:%attr(755,root,root) /etc/X11/xinit/xinitrc.d/gnupg-agent.sh}
