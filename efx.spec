%define name    efx
%define version 1.11.99
%define release 1
%define gitdate    20140509
%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary:	Graphics Library
Name:		%{name}
Version: 	%{version}
Release:	%{release}
License:	LGPLv2+
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source0:        https://download.enlightenment.org/pre-releases/%{name}-%{version}.tar.bz2
Source100:	efx.rpmlintrc
BuildRequires:	pkgconfig
BuildRequires:	doxygen
BuildRequires:	pkgconfig(efl)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(emile)
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(eo)


%description
%name is a graphics effects library.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries.

%prep
%setup -qn %name-%version

%build
LC_ALL=C NOCONFIGURE=1 ./autogen.sh
%configure2_5x --disable-static
%make

%install
%makeinstall_std

find %buildroot -name *.la | xargs rm

%files
%doc AUTHORS
%{_bindir}/test_*

%files -n %libname
%{_libdir}/*.so.%{major}*
%{_datadir}/%name

%files -n %libnamedev
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/*

