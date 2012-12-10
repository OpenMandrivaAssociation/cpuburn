%define debug_package	%nil
%define	name	cpuburn
%define version	1.4a
%define	release	%mkrel 1

Name:		%{name}
Summary:	CPU testing utilities
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
Group:		Monitoring
URL:		http://pages.sbcglobal.net/redelm/
License:	GPLv2
#ExclusiveArch:	%ix86

%description
CPU testing utilities in optimized assembler for maximum loading P6 (Intel 
Pentium Pro, Pentium II, Celeron and Pentium III TM), AMD K6, and P5 
Pentium chips.

%prep
%setup -q

%build
gcc -s -nostdlib -o burnP6 burnP6.S
gcc -s -nostdlib -o burnBX burnBX.S
gcc -s -nostdlib -o burnK6 burnK6.S
gcc -s -nostdlib -o burnK7 burnK7.S
gcc -s -nostdlib -o burnMMX burnMMX.S
gcc -s -nostdlib -o burnP5 burnP5.S

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 {burnP6,burnBX,burnK6,burnK7,burnMMX,burnP5} \
	%{buildroot}%{_bindir}

%files 
%doc Design README
%{_bindir}/*
