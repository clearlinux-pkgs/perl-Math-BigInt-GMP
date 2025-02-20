#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : perl-Math-BigInt-GMP
Version  : 1.7001
Release  : 47
URL      : https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-GMP-1.7001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-GMP-1.7001.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Math-BigInt-GMP-perl = %{version}-%{release}
Requires: gmp-lib
BuildRequires : buildreq-cpan
BuildRequires : gmp-dev
BuildRequires : gmp-gmpxx
BuildRequires : perl(Math::BigInt)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Math::BigInt::GMP - backend library for Math::BigInt etc. based on GMP
SYNOPSIS
# to use it with Math::BigInt
use Math::BigInt lib => 'GMP';

%package dev
Summary: dev components for the perl-Math-BigInt-GMP package.
Group: Development
Provides: perl-Math-BigInt-GMP-devel = %{version}-%{release}
Requires: perl-Math-BigInt-GMP = %{version}-%{release}

%description dev
dev components for the perl-Math-BigInt-GMP package.


%package perl
Summary: perl components for the perl-Math-BigInt-GMP package.
Group: Default
Requires: perl-Math-BigInt-GMP = %{version}-%{release}

%description perl
perl components for the perl-Math-BigInt-GMP package.


%prep
%setup -q -n Math-BigInt-GMP-1.7001
cd %{_builddir}/Math-BigInt-GMP-1.7001
pushd ..
cp -a Math-BigInt-GMP-1.7001 buildavx2
popd
pushd ..
cp -a Math-BigInt-GMP-1.7001 buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::BigInt::GMP.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
