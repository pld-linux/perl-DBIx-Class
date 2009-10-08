#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Class
Summary:	DBIx::Class - Extensible and flexible object <-> relational mapper
Summary(pl.UTF-8):	DBIx::Class - rozszerzalne i elastyczne wiązanie obiektów <-> relacji
Name:		perl-DBIx-Class
Version:	0.08112
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bf4f4dd040c5f994606c33ee5fcdc9f6
URL:		http://search.cpan.org/dist/DBIx-Class/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Carp-Clan >= 6.0
BuildRequires:	perl-Class-Accessor-Grouped >= 0.09000
BuildRequires:	perl-Class-C3-Componentised >= 1.0005
BuildRequires:	perl-Class-Inspector >= 1.24
BuildRequires:	perl-DBD-SQLite >= 1.25
BuildRequires:	perl-DBI >= 1.605
BuildRequires:	perl-Devel-Cycle >= 1.10
BuildRequires:	perl-Test-Memory-Cycle
BuildRequires:	perl-SQL-Translator >= 0.11002
BuildRequires:	perl-Text-CSV
BuildRequires:	perl-Data-Page >= 2.00
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-File-Temp >= 0.22
BuildRequires:	perl-JSON-Any >= 1.18
BuildRequires:	perl-MRO-Compat >= 0.09
BuildRequires:	perl-Module-Find >= 0.06
BuildRequires:	perl-Path-Class >= 0.16
BuildRequires:	perl-SQL-Abstract >= 1.58
BuildRequires:	perl-SQL-Abstract-Limit >= 0.13
BuildRequires:	perl-Scope-Guard >= 0.03
BuildRequires:	perl-Sub-Name >= 0.04
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple >= 0.92
BuildRequires:	perl-Test-Warn >= 0.21
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Only APR::UUID is available in PLD. And if it was we would still
# need only one of Data::UUID, Data::Uniqid, APR::UUID or UUID at any
# time to get full functionality
%define 	_noautoreq	'perl(Data::Uniqid)' 'perl(UUID)' 'perl(APR::UUID)' 'perl(JSON)' 'perl(DBD::Multi)' 'perl(DBIC::SQL::Abstract)'

%description
DBIx::Class is a SQL to OOP mapper, inspired by the Class::DBI
framework, and meant to support compability with it, while
restructuring the insides, and making it possible to support some new
features like self-joins, distinct, group bys and more.

It's currently considered EXPERIMENTAL - bring this near a production
database at your own risk! The API is *not* fixed yet, although most
of the primitives should be good for the future and any API changes
will be posted to the mailing list before they're committed.

%description -l pl.UTF-8
DBIx::Class to klasa odwzorowująca SQL na OOP, zainspirowana
szkieletem Class::DBI, mająca obsługiwać kompatibilność z nim, ale
restrukturyzując wnętrzności i umożliwiając obsługę niektórych nowych
możliwości, takie jak "self-join", "distinct", "group by" i inne.

Ten moduł jest aktualnie uważany za EKSPERYMENTALNY - zbliżać go do
baz produkcyjnych można tylko na własne ryzyko! API nie zostało
jeszcze ustalone, choć większość prymitywów powinna być dobra na
przyszłość i każda zmiana API jest wysyłana na listę dyskusyjną przed
zatwierdzeniem.

%package -n perl-SQL-Translator-DBIx-Class
Summary:	DBIx::Class schema parser and file producer
Summary(pl.UTF-8):	Narzędzie do analizy schematów i tworzenia plików DBIx::Class
Group:		Development/Languages/Perl

%description -n perl-SQL-Translator-DBIx-Class
This package contains SQL::Translator (sqlfairy) parser for
DBIx::Class::Schema objects and producer for DBIx::Class files.

%description -n perl-SQL-Translator-DBIx-Class -l pl.UTF-8
Ten pakiet zawiera analizator SQL::Translator (sqlfairy) dla obiektów
DBIx::Class::Schema oraz generator plików DBIx::Class.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# SQL::Translator is FUBAR
mv t/94versioning.t{,.fubar}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"DBIx::Class", EXE_FILES=>[<script/*>])' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/DBIx/Class/{Schema,ResultSet}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/DBIx/*.pm
%{perl_vendorlib}/DBIx/Class
%{_mandir}/man3/DBIx*
%{_mandir}/man1/

%files -n perl-SQL-Translator-DBIx-Class
%defattr(644,root,root,755)
%{perl_vendorlib}/SQL/Translator/Parser/*
%{perl_vendorlib}/SQL/Translator/Producer/*
%{_mandir}/man3/SQL*
