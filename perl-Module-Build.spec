%define upstream_name    Module-Build
%define upstream_version 0.3800

Name:       perl-%{upstream_name}
%if %mdkversion > 200900
Version:    %perl_convert_version %{upstream_version}
%else
Version:    %{upstream_version}
%endif
Release:    %mkrel 3
Epoch:      1

Summary:    Build and install Perl modules
License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Curses interface for Config::Model
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(CPAN::Meta) >= 2.110.420
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.270
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.210
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.820
BuildRequires:  perl(File::Temp) >= 0.150
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Metadata) >= 1.000.002
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Perl::OSType) >= 1
BuildRequires:  perl(Test::Harness) >= 3.160
BuildRequires:  perl(Test::More) >= 0.490
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(Text::ParseWords)
Buildrequires:  perl(YAML)
# for %%check
BuildRequires:  perl-devel

# (tv) this is a soft dep (require instead of use); w/o it some builds failed with
# "Module::Build is not configured with C_support":
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Suggests: perl-ExtUtils-CBuilder

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
%setup -q -n %{upstream_name}-%{upstream_version} 

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
%{perl_vendorlib}/inc
%{perl_vendorlib}/Module
%{_mandir}/*/*
