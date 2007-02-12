%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check SpamAssassin spamd
Summary(pl.UTF-8):   Wtyczka Nagiosa do sprawdzania spamd ze SpamAssassina
Name:		nagios-plugin-check_spamd
Version:	1.1
Release:	0.6
License:	GPL
Group:		Networking
Source0:	ftp://jhweiss.de/pub/users/weiss/misc/check_spamd
# Source0-md5:	bee229fc60f7536f854d8f10f7f553f4
Source1:	check_spamd.cfg
Patch0:		check_spamd-utils.patch
URL:		http://www.jhweiss.de/code.html
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%define		_noautoreq 'perl(utils)'

%description
check_spamd is a Nagios plugin for checking SpamAssassin's spamd.

%description -l pl.UTF-8
check_spamd to wtyczka Nagiosa do sprawdzania spamd ze SpamAssassina.

%prep
%setup -q -c -T
install %{SOURCE0} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}

sed -e 's,@plugindir@,%{_plugindir},' check_spamd > $RPM_BUILD_ROOT%{_plugindir}/check_spamd
chmod +x $RPM_BUILD_ROOT%{_plugindir}/check_spamd

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_plugindir}/*
