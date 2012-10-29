Summary:	Simple DirectMedia Layer - ttf handling
Name:		SDL_ttf
Version:	2.0.11
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_ttf/release/%{name}-%{version}.tar.gz
# Source0-md5:	61e29bd9da8d245bc2471d1b2ce591aa
URL:		http://www.libsdl.org/projects/SDL_ttf/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a sample library which allows you to use TrueType fonts in
your SDL applications. It comes with an example program "sdlfont"
which displays an example string for a given TrueType font file.

%package devel
Summary:	Header files and more to develop SDL_ttf applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and more to develop SDL_ttf applications.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure		\
	LIBS="-lm"	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install .libs/showfont $RPM_BUILD_ROOT%{_bindir}/sdlfont

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/sdlfont
%attr(755,root,root) %ghost %{_libdir}/libSDL_ttf-2.0.so.?
%attr(755,root,root) %{_libdir}/libSDL_ttf-2.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_ttf.so
%{_libdir}/libSDL_ttf.la
%{_includedir}/SDL/SDL_ttf.h
%{_pkgconfigdir}/SDL_ttf.pc

