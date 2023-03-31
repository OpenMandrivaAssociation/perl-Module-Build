%define modname Module-Build

Summary:	Build and install Perl modules
Name:		perl-%{modname}
Version:	0.4232
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Module::Build
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(CPAN::Meta) >= 2.110.420
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(ExtUtils::CBuilder) >= 0.270
BuildRequires:	perl(ExtUtils::Install)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(ExtUtils::Mkbootstrap)
BuildRequires:	perl(ExtUtils::ParseXS) >= 2.210
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec) >= 0.820
BuildRequires:	perl(File::Temp) >= 0.150
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Module::Metadata) >= 1.000.002
BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(Perl::OSType) >= 1
BuildRequires:	perl(Test::Harness) >= 3.160
BuildRequires:	perl(Test::More) >= 0.490
BuildRequires:	perl(Text::Abbrev)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl(YAML)
# for %%check
BuildRequires:	perl-devel
Suggests:	perl-ExtUtils-CBuilder

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
%autosetup -p1 -n %{modname}-%{version} 
perl Build.PL installdirs=vendor

%build
./Build

%install
./Build install destdir=%{buildroot}

%check
./Build test

%files 
%doc Changes README
%{_bindir}/config_data
%{perl_vendorlib}/Module
%{_mandir}/*/*
