#
# Conditional build:
%bcond_with	max_cache_ttl # add max-cache-ttl option (for tests) 
%bcond_without	xinitrc	# don't use xinitrc's directory
#
Summary:	GnuPG extension - agent
Summary(pl):	Rozszerzenie GnuPG - agent
Name:		gnupg-agent
Version:	1.9.10
Release:	3
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/gnupg/gnupg-%{version}.tar.gz
# Source0-md5:	d923cfe0921898fbeb66374a0e32ddc6
Source1:	gnupg-agent.sh
# Patch0 based on http://marc.theaimsgroup.com/?l=gnupg-devel&m=109300087831144&w=2
# taken from gnupg cvs.
Patch0:		%{name}-max_cache_ttl.patch	
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	libassuan-devel >= 1:0.6.6
BuildRequires:	libgcrypt-devel >= 1.1.93
BuildRequires:	libgpg-error-devel >= 0.6
BuildRequires:	libksba-devel >= 0.9.7
BuildRequires:	pcsc-lite-devel
BuildRequires:	opensc-devel >= 0.8.0
BuildRequires:	pth-devel >= 2.0.0
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	gnupg
Requires:	pinentry
%{?with_xinitrc:Requires: xinitrc}
Obsoletes:	newpg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnupg

%description
GnuPG extension - agent.

%description -l pl
Rozszerzenie GnuPG - agent.

%prep
%setup -q -n gnupg-%{version}
%{?with_max_cache_ttl:%patch0 -p1}

%build
cp -f /usr/share/automake/config.* scripts
%configure \
	--disable-gpg \
	--with-capabilities \
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
	DESTDIR=$RPM_BUILD_ROOT

ln -sf gpg2 $RPM_BUILD_ROOT%{_bindir}/gpg
install %{SOURCE1} $RPM_BUILD_ROOT/etc/profile.d/%{name}.sh
%{?with_xinitrc:ln -sf /etc/profile.d/%{name}.sh $RPM_BUILD_ROOT/etc/X11/xinit/xinitrc.d/%{name}.sh}

%find_lang gnupg2

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f gnupg2.lang
%defattr(644,root,root,755)
%doc agent/ChangeLog
%attr(755,root,root) %{_bindir}/gpg-agent
%attr(755,root,root) %{_bindir}/gpgsm
%attr(755,root,root) %{_bindir}/kbxutil
%attr(755,root,root) %{_bindir}/sc-copykeys
%attr(755,root,root) %{_bindir}/sc-investigate
%attr(755,root,root) %{_bindir}/scdaemon
%attr(755,root,root) %{_libdir}/gnupg/gpg-protect-tool
%attr(755,root,root) %{_libdir}/gnupg/pcsc-wrapper
%attr(755,root,root) /etc/profile.d/%{name}.sh
%{?with_xinitrc:%attr(755,root,root) /etc/X11/xinit/xinitrc.d/%{name}.sh}
