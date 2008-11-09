
%define major   1
%define lib_name %mklibname svg-cairo %major

Name:             libsvg-cairo
Summary:          A SVG library based on cairo
Version: 0.1.6
Release: %mkrel 9
License:          BSD
Group:            System/Libraries
Source:           %{name}-%{version}.tar.bz2
URL:              http://cairographics.org/snapshots/
BuildRoot:        %{_tmppath}/%{name}-%{version}-root
BuildRequires:    libsvg-devel
BuildRequires:    cairo-devel
BuildRequires:    jpeg-devel

%description
Libsvg-cairo provides the ability to render SVG content from files or
buffers. All rendering is performed using the cairo rendering library.

%package -n %{lib_name}
Summary:          A SVG library based on cairo
Group:            System/Libraries

%description -n %{lib_name}
Libsvg-cairo provides the ability to render SVG content from files or
buffers. All rendering is performed using the cairo rendering library.

%package -n %{lib_name}-devel
Summary:          Libraries and include files for developing with libsvg
Group:            Development/C
Requires:         %{lib_name} = %{version}
Provides:         %{name}-devel = %{version}

%description -n %{lib_name}-devel
This package provides the necessary development libraries and include
files to allow you to develop with libsvg-cairo.


%prep
%setup -q

%build
export LIBS="-lm"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif


%files -n %{lib_name}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg-cairo.pc

