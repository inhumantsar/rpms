# $Id$

Summary: libnet module for perl
Name: perl-libnet
Version: 1.17
Epoch: 2
Release: 1
License: distributable
Group: Applications/CPAN
Source0: libnet-%{version}.tar.gz
Source10: filter-depends.sh
URL: http://www.cpan.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
libnet module for perl

# Provide perl-specific find-{provides,requires}.
%define __find_provides /usr/lib/rpm/find-provides.perl
%define __find_requires %{SOURCE10}

%prep
%setup -q -n libnet-%{version} 

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL < /dev/null
make

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make PREFIX=$RPM_BUILD_ROOT/usr INSTALLDIRS=vendor install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | 
	sed "s@^$RPM_BUILD_ROOT@@g" | 
	grep -v perllocal.pod | 
	grep -v "\.packlist" > libnet-1.0901-filelist
if [ "$(cat libnet-1.0901-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi

%files -f libnet-1.0901-filelist
%defattr(-,root,root)

%changelog
* Wed Dec 19 2001 root <root@redhat.com>
- Spec file was autogenerated. 
