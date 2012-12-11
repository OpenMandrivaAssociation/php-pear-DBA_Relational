%define		_class		DBA
%define		_subclass	Relational
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.2.0
Release:	%mkrel 8
Epoch:		1
Summary:	Berkeley-style database abstraction class
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DBA_Relational/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Table management extension for DBA.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.0-8mdv2012.0
+ Revision: 741839
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.0-7
+ Revision: 679281
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.0-6mdv2011.0
+ Revision: 613626
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.2.0-5mdv2010.1
+ Revision: 479287
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1:0.2.0-4mdv2010.0
+ Revision: 440973
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.0-3mdv2009.1
+ Revision: 321949
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.0-2mdv2009.0
+ Revision: 236820
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1:0.2.0-1mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.0-1mdv2008.0
+ Revision: 24079
- use epoch
- 0.2.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.19-7mdv2007.0
+ Revision: 81481
- Import php-pear-DBA_Relational

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.19-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.19-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.19-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.19-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.19-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.19-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.19-1mdk
- initial Mandriva package (PLD import)

