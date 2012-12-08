%define major   1
%define libname %mklibname svg-cairo %{major}
%define devname %mklibname svg-cairo -d

Name:		libsvg-cairo
Summary:	A SVG library based on cairo
Version:	0.1.6
Release:	15
License:	BSD
Group:		System/Libraries
URL:		http://cairographics.org/snapshots/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libsvg)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	jpeg-devel

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
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	%{libname}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < 0.1.6-15

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
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg-cairo.pc

%changelog
* Thu May 03 2012 Götz Waschk <waschk@mandriva.org> 0.1.6-14mdv2012.0
+ Revision: 795317
- remove libtool archive
- yearly rebuild

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-13
+ Revision: 661530
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-12mdv2011.0
+ Revision: 602608
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-11mdv2010.1
+ Revision: 488783
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-10mdv2010.0
+ Revision: 416626
- rebuilt against libjpeg v7

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-9mdv2009.1
+ Revision: 301472
- rebuilt against new libxcb

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-8mdv2009.0
+ Revision: 229807
- fix build (-lm)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.6-6mdv2008.1
+ Revision: 179003
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sun Jun 18 2006 Stefan van der Eijk <stefan@eijk.nu> 0.1.6-4
- rebuild for png
- %%mkrel

* Thu Sep 29 2005 Pascal Terjan <pterjan@mandriva.org> 0.1.6-3mdk
- use the %%release which is defined

* Thu Aug 11 2005 Götz Waschk <waschk@mandriva.org> 0.1.6-2mdk
- rebuild for new cairo

* Fri Jul 08 2005 Tigrux <tigrux@ximian.com> 0.1.6-1mdk
- New release 0.1.6

* Wed Mar 09 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.1.5-1mdk
- spec fixes
- New release 0.1.5

* Fri Jun 04 2004 Marcel Pol <mpol@mandrake.org> 0.1.4-2mdk
- buildrequires (slbd)

* Fri Jun 04 2004 Marcel Pol <mpol@mandrake.org> 0.1.4-1mdk
- initial mandrake package

