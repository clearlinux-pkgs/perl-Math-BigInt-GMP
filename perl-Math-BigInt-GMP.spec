#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-BigInt-GMP
Version  : 1.6007
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-GMP-1.6007.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigInt-GMP-1.6007.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Math-BigInt-GMP-perl = %{version}-%{release}
Requires: gmp-lib
Requires: gmp-lib-hsw
BuildRequires : buildreq-cpan
BuildRequires : gmp-dev
BuildRequires : gmp-gmpxx
BuildRequires : gmp-lib-hsw
BuildRequires : perl(Math::BigInt)

%description
Math-BigInt-GMP
Math::BigInt::GMP is a replacement library for Math::BigInt::Calc that
reimplements some of the Math::BigInt::Calc functions in XS. It can be used
via:

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
%setup -q -n Math-BigInt-GMP-1.6007
cd %{_builddir}/Math-BigInt-GMP-1.6007

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::BigInt::GMP.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Math/BigInt/GMP.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Math/BigInt/GMP/GMP.so
