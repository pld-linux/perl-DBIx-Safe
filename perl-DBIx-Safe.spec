#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	DBIx
%define	pnam	Safe
Summary:	DBIx::Safe - Safer access to your database through a DBI database handle
#Summary(pl.UTF-8):	
Name:		perl-DBIx-Safe
Version:	1.2.5
Release:	1
License:	bsd
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TU/TURNSTEP/DBIx-Safe-1.2.5.tar.gz
# Source0-md5:	ca5abd5fec19da9d51e6312f6707c534
URL:		http://search.cpan.org/dist/DBIx-Safe/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBD-Pg >= 1.49
BuildRequires:	perl-DBI >= 1.49
BuildRequires:	perl-Module-Signature >= 0.50
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this module is to give controlled, limited access to
an application, rather than simply passing it a raw database handle
through DBI. DBIx::Safe acts as a wrapper to the database, by only
allowing through the commands you tell it to. It filters all things
related to the database handle - methods and attributes.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/DBIx/*.pm
%{_mandir}/man3/*
