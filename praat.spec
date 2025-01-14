%define srcver  %(echo %{version} | sed -e 's/\\.\\([0-9]\\)$/.0\\1/' -e 's/\\.//g')
Name:		praat
Summary:	Doing phonetics, speech analysis and synthesis by computer
Version:	5.2.17
Release:	3
License: 	GPLv2
Group:		Sciences/Other
Url:		https://www.fon.hum.uva.nl/praat/
BuildRequires:	libxp-devel
BuildRequires:	libxt-devel
BuildRequires:	libsm-devel
BuildRequires:	libice-devel
BuildRequires:	libxext-devel
BuildRequires:	libalsa-devel
BuildRequires:	libxmu-devel
BuildRequires:	lesstif-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	cairo-devel
Source0:	http://www.fon.hum.uva.nl/praat/praat%{srcver}_sources.tar.gz
Source1:	praat.png
Source2:	praat_mini.png
Source3:	praat_large.png
Source4:	mandriva-praat.desktop

%description
According to its authors, praat is "doing phonetics by computer". There are
several speech analysis functionalities available: spectrograms, cochleograms,
and pitch and formant extraction. Articulatory synthesis, as well as synthesis
from pitch, formant, and intensity are also available. Other features are
segmentation, labelling using the phonetic alphabet, and computation of
statistics.

%prep
%setup -q -n sources_%{srcver}

%build
ln -fs makefiles/makefile.defs.linux.gtk makefile.defs
%make

%clean

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/{applications,icons}
mkdir -p %{buildroot}/%{_datadir}/icons/{mini,large}

# the application itself
cp -vf ./praat %{buildroot}/usr/bin/

# icons provided by antonino mingoia from www.ozzpot.com
cp -vf %{SOURCE1} %{buildroot}/%{_datadir}/icons/praat.png
cp -vf %{SOURCE2} %{buildroot}/%{_datadir}/icons/mini/praat.png
cp -vf %{SOURCE3} %{buildroot}/%{_datadir}/icons/large/praat.png

# our own desktop entry
cp -vf %{SOURCE4} %{buildroot}/%{_datadir}/applications/

%files
%defattr (-,root,root)
%{_bindir}/praat
%{_datadir}/icons/*
%{_datadir}/applications/*.desktop



%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 5.2.17-1mdv2011.0
+ Revision: 645380
- update to new version 5.2.17

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 5.1.29-2mdv2011.0
+ Revision: 614609
- the mass rebuild of 2010.1 packages

* Thu Mar 11 2010 Caio Begotti <caio1982@mandriva.org> 5.1.29-1mdv2010.1
+ Revision: 518189
- new upstream version (changes from the standard lesstif/motif toolkit to gtk and cairo)

* Thu Jan 21 2010 Frederik Himpe <fhimpe@mandriva.org> 5.1.25-1mdv2010.1
+ Revision: 494656
- update to new version 5.1.25

* Mon Dec 21 2009 Caio Begotti <caio1982@mandriva.org> 5.1.22-1mdv2010.1
+ Revision: 480905
- new upstream version

* Wed Sep 16 2009 Caio Begotti <caio1982@mandriva.org> 5.1.15-1mdv2010.0
+ Revision: 443548
- new upstream version, fixes the hanging issue
- fix the categories used for praat
- fix the summary, it was not making much sense

* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 5.1.7-1mdv2010.0
+ Revision: 378427
- update to new version 5.1.7

* Sun May 10 2009 Frederik Himpe <fhimpe@mandriva.org> 5.1.5-2mdv2010.0
+ Revision: 374049
- Really update to 5.1.5
- Add sed hack to convert version string in source version string with
  leading zero: should make mdvsys update work as expected
- Improve summary

* Sun May 10 2009 Frederik Himpe <fhimpe@mandriva.org> 5.1.5-1mdv2010.0
+ Revision: 374037
- update to new version 5.1.5

* Wed Apr 01 2009 Caio Begotti <caio1982@mandriva.org> 5.1.3-1mdv2009.1
+ Revision: 363330
- wrong package name dependency
- fix the menu entry, it's more a scientific app rather an education utility
- import praat


* Wed Apr 01 2009 Caio Begotti <caio@mandriva.com> 5.1.3-1mdv2009.1
- First version, initial import
