#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Class
Summary:	DBIx::Class - Extensible and flexible object <-> relational mapper
Summary(pl):	DBIx::Class - rozszerzalne i elastyczne wi±zanie obiektów <-> relacji
Name:		perl-DBIx-Class
Version:	0.06003
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83b04b4cfafb9e3ae6c50d8b289ea52e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Carp-Clan
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-Class-C3 >= 0.11
BuildRequires:	perl-Class-Data-Accessor >= 0.01
BuildRequires:	perl-Class-Inspector
BuildRequires:	perl-Data-Page >= 2.00
BuildRequires:	perl-Data-UUID
BuildRequires:	perl-DBD-SQLite >= 1.11
BuildRequires:	perl-DBI >= 1.40
BuildRequires:	perl-Module-Find
BuildRequires:	perl-SQL-Abstract >= 1.2
BuildRequires:	perl-SQL-Abstract-Limit >= 0.11
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Only last of them is available in PLD. And if it was we would still
# need only one of Data::UUID, Data::Uniqid, APR::UUID or UUID at any
# time to get full functionality
%define 	_noautoreq	'perl(Data::Uniqid)' 'perl(UUID)' 'perl(APR::UUID)'

%description
DBIx::Class is a SQL to OOP mapper, inspired by the Class::DBI
framework, and meant to support compability with it, while
restructuring the insides, and making it possible to support some new
features like self-joins, distinct, group bys and more.

It's currently considered EXPERIMENTAL - bring this near a production
database at your own risk! The API is *not* fixed yet, although most
of the primitives should be good for the future and any API changes
will be posted to the mailing list before they're committed.

%description -l pl
DBIx::Class to klasa odwzorowuj±ca SQL na OOP, zainspirowana
szkieletem Class::DBI, maj±ca obs³ugiwaæ kompatibilno¶æ z nim, ale
restrukturyzuj±c wnêtrzno¶ci i umo¿liwiaj±c obs³ugê niektórych nowych
mo¿liwo¶ci, takie jak "self-join", "distinct", "group by" i inne.

Ten modu³ jest aktualnie uwa¿any za EKSPERYMENTALNY - zbli¿aæ go do
baz produkcyjnych mo¿na tylko na w³asne ryzyko! API nie zosta³o
jeszcze ustalone, choæ wiêkszo¶æ prymitywów powinna byæ dobra na
przysz³o¶æ i ka¿da zmiana API jest wysy³ana na listê dyskusyjn± przed
zatwierdzeniem.

%package -n perl-SQL-Translator-DBIx-Class
Summary:	DBIx::Class schema parser and file producer
Summary(pl):	Narzêdzie do analizy schematów i tworzenia plików DBIx::Class
Group:		Development/Languages/Perl

%description -n perl-SQL-Translator-DBIx-Class
This package contains SQL::Translator (sqlfairy) parser for
DBIx::Class::Schema objects and producer for DBIx::Class files.

%description -n perl-SQL-Translator-DBIx-Class -l pl
Ten pakiet zawiera analizator SQL::Translator (sqlfairy) dla obiektów
DBIx::Class::Schema oraz generator plików DBIx::Class.

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
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/DBIx/Class/Schema

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBIx/*.pm
%{perl_vendorlib}/DBIx/Class
%dir %{perl_vendorlib}/DBIx/Class/Schema
%{_mandir}/man3/*

%files -n perl-SQL-Translator-DBIx-Class
%defattr(644,root,root,755)
%{perl_vendorlib}/SQL/Translator/Parser/*
%{perl_vendorlib}/SQL/Translator/Producer/*
