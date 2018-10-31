%define major   1
%define libname %mklibname svg-cairo %{major}
%define devname %mklibname svg-cairo -d

%define _disable_lto 1

Name:		libsvg-cairo
Summary:	A SVG library based on cairo
Version:	0.1.6
Release:	26
License:	BSD
Group:		System/Libraries
Url:		http://cairographics.org/snapshots/
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.bz2
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libsvg)

%description
Libsvg-cairo provides the ability to render SVG content from files or
buffers. All rendering is performed using the cairo rendering library.

%package -n %{libname}
Summary:	A SVG library based on cairo
Group:		System/Libraries

%description -n %{libname}
Libsvg-cairo provides the ability to render SVG content from files or
buffers. All rendering is performed using the cairo rendering library.

%package -n %{devname}
Summary:	Libraries and include files for developing with libsvg
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the necessary development libraries and include
files to allow you to develop with libsvg-cairo.

%prep
%setup -q

%build
export LIBS="-lm"
%configure2_5x --disable-static
%make

%install
%makeinstall

%files -n %{libname}
%{_libdir}/libsvg-cairo.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg-cairo.pc

