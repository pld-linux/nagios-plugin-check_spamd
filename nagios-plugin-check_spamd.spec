Summary:	Nagios pluging to check SpamAssassin spamd
Name:		nagios-plugin-check_spamd
Version:	1.1
Release:	0.1
License:	GPL
Group:		Networking
Source0:	ftp://jhweiss.de/pub/users/weiss/misc/check_spamd
# Source0-md5:	bee229fc60f7536f854d8f10f7f553f4
Patch0:		check_spamd-utils.patch
URL:		http://www.jhweiss.de/code.html
Requires:	nagios-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins

%description
check_spamd is a Nagios plugin for checking SpamAssassins spamd.

%prep
%setup -q -c -T
install %{SOURCE0} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

sed -e 's,@plugindir@,%{_plugindir},' check_spamd > $RPM_BUILD_ROOT%{_plugindir}/check_spamd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*
