%define srcver  %(echo %{version} | sed -e 's/\\.\\([0-9]\\)$/.0\\1/' -e 's/\\.//g')
Name:		praat
Summary:	Praat: doing phonetics, speech analysis and synthesis by computer
Version:	5.1.15
Release:	%mkrel 1
License: 	GPLv2
Group:		Sciences/Other
Url:		http://www.fon.hum.uva.nl/praat/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{revision}-buildroot
BuildRequires:	libxp-devel
BuildRequires:	libxt-devel
BuildRequires:	libsm-devel
BuildRequires:	libice-devel
BuildRequires:	libxext-devel
BuildRequires:	libalsa-devel
BuildRequires:	libxmu-devel
BuildRequires:	lesstif-devel
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
ln -fs makefiles/makefile.defs.linux.dynamic makefile.defs
%make

%clean
rm -rf %{buildroot}

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

