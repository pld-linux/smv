Summary:	SMV - symbolic model verifier
Summary(pl):	SMV - narzêdzie do weryfikacji modeli symbolicznych
Name:		smv
Version:	2.5.4.3
Release:	0.1
License:	No fscking idea :o
Group:		Development/Tools
Source0:	http://www-2.cs.cmu.edu/~modelcheck/smv/%{name}.r%{version}.tar.gz
# Source0-md5:	dd1a7ebcbac935845fc73eb8957386cb
URL:		http://www-2.cs.cmu.edu/~modelcheck/smv.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMV - symbolic model verifier.

%description -l pl
SMV - narzêdzie do weryfikacji modeli symbolicznych.

%prep
%setup -q -n %{name}

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

install smv $RPM_BUILD_ROOT%{_bindir}
install smv.1 $RPM_BUILD_ROOT%{_mandir}/man1
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEW README doc/*
%attr(755,root,root) %{_bindir}/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
%{_mandir}/man1/*
