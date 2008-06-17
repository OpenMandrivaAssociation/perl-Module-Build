%define module  Module-Build
%define name    perl-%{module}
%define modprefix Module
%define version 0.2808.01
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Build and install Perl modules
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
BuildRequires:  perl-devel
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(Text::ParseWords)
Buildrequires:  perl(YAML)
# (tv) this is a soft dep (require instead of use); w/o it some builds failed with
# "Module::Build is not configured with C_support":
Suggests: perl-ExtUtils-CBuilder

Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Module::Build is a system for building, testing, and installing Perl modules.
It is meant to be a replacement for ExtUtils::MakeMaker. Developers may alter
the behavior of the module through subclassing in a much more straightforward
way than with MakeMaker. It also does not require a make on your system - most
of the Module::Build code is pure-perl and written in a very cross-platform
way. In fact, you don't even need a shell, so even platforms like MacOS
(traditional) can use it fairly easily. Its only prerequisites are modules that
are included with perl 5.6.0, and it works fine on perl 5.005 if you can
install a few additional modules.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
perl Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%check
./Build test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes INSTALL README
%{_bindir}/config_data
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*


