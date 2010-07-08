%define 	module	TwistedWords
%define		major	8.1
%define		minor	0

Summary:	Chat and Instant Messaging for Twisted
Summary(pl.UTF-8):	Chat oraz Instant Messaging dla Twisted
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Words/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	40cecdc6d58efefdb02b50961bb9a381
URL:		http://twistedmatrix.com/trac/wiki/TwistedWords
BuildRequires:	ZopeInterface
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	python-TwistedCore >= 2.4.0
Obsoletes:	python-Twisted-words
Obsoletes:	python-TwistedXish
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted Words includes:
- Low-level protocol implementations of OSCAR (AIM and ICQ), IRC, MSN,
  TOC (AIM),
- Jabber libraries,
- Prototypes of chat server and client frameworks built on top of the
  protocols.

%description -l pl.UTF-8
Twisted Words zawiera:
- Niskopoziomowe implementacje protokołów OSCAR (AIM oraz ICQ), IRC,
  MSN, TOC (AIM),
- Biblioteki Jabberowe,
- Prototypy serwera chatowego

%package doc
Summary:	Documentation for Twisted
Summary(pl.UTF-8):	Dokumentacja do Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for Twisted - event-driven networking framework
written in Python.

%description doc -l pl.UTF-8
Dokumentacja offline do Twisted - narzędzia do budowania rozproszonych
aplikacji sieciowych pisanych w Pythonie.

%package examples
Summary:	Example programs for Twisted
Summary(pl.UTF-8):	Programy przykładowe do Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Twisted.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla Twisted.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
%{__python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir}/twisted,%{py_sitescriptdir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

%{__python} setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

install doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.egg-info
%{py_sitedir}/twisted/words
%{py_sitedir}/twisted/plugins/*
%{_mandir}/man1/*.1*

%files doc
%defattr(644,root,root,755)
%doc doc/howto

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
