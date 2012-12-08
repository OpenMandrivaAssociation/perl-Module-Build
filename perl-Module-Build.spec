%define upstream_name    Module-Build
%define upstream_version 0.3800

Name:       perl-%{upstream_name}
%if %mdkversion > 200900
Version:    %perl_convert_version %{upstream_version}
%else
Version:    %{upstream_version}
%endif
Release:    %mkrel 4
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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.380.0-4mdv2012.0
+ Revision: 765486
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.380.0-3
+ Revision: 763980
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.380.0-2
+ Revision: 763283
- force it
- rebuild

  + Shlomi Fish <shlomif@mandriva.org>
    - New version - 0.3800

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.360.700-2
+ Revision: 667258
- mass rebuild

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.360.700-1mdv2011.0
+ Revision: 532156
- update to 0.3607

* Thu Apr 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.360.500-1mdv2010.1
+ Revision: 530667
- update to 0.3605

* Mon Mar 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.360.300-2mdv2010.1
+ Revision: 515889
- ensure backportability

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.360.300-1mdv2010.1
+ Revision: 493589
- update to 0.3603

* Wed Dec 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.360.100-1mdv2010.1
+ Revision: 481712
- update to 0.3601

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.360.0-1mdv2010.1
+ Revision: 480732
- update to 0.36

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.350.0-1mdv2010.0
+ Revision: 421837
- update to 0.35

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.340.201-1mdv2010.0
+ Revision: 418656
- update to 0.340201

* Fri Jul 31 2009 Anssi Hannula <anssi@mandriva.org> 1:0.340.0-2mdv2010.0
+ Revision: 405175
- buildrequires perl-devel for tests
- bump release for the rebuild, works better that way

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild using %%perl_convert_version

* Wed Jul 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.340.0-1mdv2010.0
+ Revision: 393697
- new version

* Sun May 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.33-1mdv2010.0
+ Revision: 373931
- new version

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.32-1mdv2009.1
+ Revision: 345919
- update to new version 0.32

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.31-1mdv2009.1
+ Revision: 318315
- new version

* Tue Nov 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.30-1mdv2009.1
+ Revision: 302168
- new version

* Wed Sep 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2808-4mdv2009.0
+ Revision: 287784
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.2808-3mdv2008.1
+ Revision: 152489
- rebuild for new perl
- replace a requires by a suggests
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 0.2808-2mdv2008.0
+ Revision: 69023
- fix missing deps (b/c of require instead of use) that make other package builds
  failed due to +# (tv) this is a soft dep; w/o it some builds failed with
  "Module::Build is not configured with C_support"

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2808-1mdv2008.0
+ Revision: 47699
- update to new version 0.2808


* Wed Dec 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.2806-1mdv2007.0
+ Revision: 100405
- new version
- Import perl-Module-Build

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.2805-1mdv2007.0
- New version 0.2805

* Mon Jul 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2801-4mdv2007.0
- fix "Module::Build is not configured with C_support at ..."

* Sun Jun 18 2006 Scott Karns <scottk@mandriva.org> 0.2801-3mdv2007.0
- Rebuild
- Remove mdkversion conditional around BuildRequires perl-devel so
  all tests run successfully

* Mon May 22 2006 Scott Karns <scottk@mandriva.org> 0.2801-2mdk
- Added BuildRequires perl(ExtUtils::CBuilder) >= 0.15

* Mon May 22 2006 Scott Karns <scottk@mandriva.org> 0.2801-1mdk
- New release 0.2801
- Improved source URL
- Updated BuildRequires per META.yml and Mandriva perl packaging policy

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.2612-1mdk
- New release 0.2612
- %%mkrel

* Sun Aug 21 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.2611-2mdk
- perl-devel is still required to run the tests of this package

* Wed Jun 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.2611-1mdk
- 0.2611

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.2610-2mdk 
- rpmbuildupdate aware
- better url
- drop useless empty directories
- fix buildrequires in a backward compatible way
- spec cleanup
- Build test in %%check

* Sat Apr 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.2610-1mdk
- 0.2610

* Wed Feb 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.2608-1mdk
- 0.2608

* Sat Dec 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2607-2mdk
- require perl-devel for building on newer than 10.1 too as it's required for testing

* Thu Dec 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.2607-1mdk
- 0.2607

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.2604-2mdk
- fix buildrequires in a backward compatible way

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.2604-1mdk
- 0.2604
- install the new config_data script

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.25-1mdk
- 0.25

* Thu Apr 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.24-1mdk
- new version
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.21-2mdk
- fixed dir ownership (distlint)

