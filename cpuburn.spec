%define name cpuburn
%define version 1.4
%define release %mkrel 7 

Name: %{name}
Summary: CPU testing utilities
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Group: Monitoring
URL: http://pages.sbcglobal.net/redelm/
License: GPL
ExclusiveArch:	%ix86

%description
CPU testing utilities in optimized assembler for maximum loading P6 (Intel 
Pentium Pro, Pentium II, Celeron and Pentium III TM), AMD K6, and P5 
Pentium chips.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
gcc -s -nostdlib -o burnP6 burnP6.S
gcc -s -nostdlib -o burnBX burnBX.S
gcc -s -nostdlib -o burnK6 burnK6.S
gcc -s -nostdlib -o burnK7 burnK7.S
gcc -s -nostdlib -o burnMMX burnMMX.S
gcc -s -nostdlib -o burnP5 burnP5.S

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 {burnP6,burnBX,burnK6,burnK7,burnMMX,burnP5} \
	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc Design README
%{_bindir}/*

