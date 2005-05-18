%define 	module	TwistedWords

Summary:	Chat and Instant Messaging for Twisted
Summary(pl):	Chat oraz Instant Messaging dla Twisted
Name:		python-%{module}
Version:	0.1.0
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Words/0.1/%{module}-%{version}.tar.bz2
# Source0-md5:	168ca07ab860324054c539bec1b0ef57
URL:		http://twistedmatrix.com/projects/words/
BuildRequires:	ZopeInterface
BuildRequires:	python-devel >= 2.2
Requires:	python-Twisted >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted Words includes:
- Low-level protocol implementations of OSCAR (AIM and ICQ), IRC, MSN,
  TOC (AIM),
- Jabber libraries,
- Prototypes of chat server and client frameworks built on top of the
  protocols.

%description -l pl
Twisted Words zawiera:
- Niskopoziomowe implementacje protoko³ów OSCAR (AIM oraz ICQ), IRC,
  MSN, TOC (AIM),
- Biblioteki Jabberowe,
- Prototypy serwera chatowego

%package doc
Summary:	Documentation for Twisted
Summary(pl):	Dokumentacja do Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for Twisted - event-driven networking framework
written in Python.

%description doc -l pl
Dokumentacja offline do Twisted - narzêdzia do budowania rozproszonych
aplikacji sieciowych pisanych w Pythonie.

%package examples
Summary:	Example programs for Twisted
Summary(pl):	Programy przyk³adowe do Twisted
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Twisted.

%description examples -l pl
Ten pakiet zawiera przyk³adowe programy dla Twisted.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir}/twisted,%{py_sitescriptdir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

ln -sf %{py_sitescriptdir}/twisted/words $RPM_BUILD_ROOT%{py_sitedir}/twisted/words

install doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -ar doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/twisted/words
%{py_sitescriptdir}/twisted
%{_mandir}/man1/*.1*

%files doc
%defattr(644,root,root,755)
%doc doc/howto

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
