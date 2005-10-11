#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Class
Summary:	DBIx::Class - Extensible and flexible object <-> relational mapper
#Summary(pl):	
Name:		perl-DBIx-Class
Version:	0.03001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3d55fec74910e4c7e3ee4913d012b74
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBD-SQLite >= 1.08
BuildRequires:	perl-Data-Page
BuildRequires:	perl-Module-Find
BuildRequires:	perl-SQL-Abstract >= 1.2
BuildRequires:	perl-SQL-Abstract-Limit >= 0.11
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl(UNIVERSAL::require)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Class is a sql to oop mapper, inspired by the Class::DBI framework, 
and meant to support compability with it, while restructuring the 
insides, and making it possible to support some new features like 
self-joins, distinct, group bys and more.

It's currently considered EXPERIMENTAL - bring this near a production
database at your own risk! The API is *not* fixed yet, although most of
the primitives should be good for the future and any API changes will be
posted to the mailing list before they're committed.


# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBIx/*.pm
%{perl_vendorlib}/DBIx/Class
%{_mandir}/man3/*
