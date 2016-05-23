Summary: Libav video encoding and decoding library
Name: libav
Version: 9.18
Release: 1
License: LGPL 2.1
Group: Multimedia
Source: https://libav.org/releases/libav-9.18.tar.gz
URL: https://libav.org
Distribution: N/A
Vendor: N/A
Packager: N/A

%description
Libav provides cross-platform tools and libraries to convert, manipulate and stream a wide range of multimedia formats and protocols.

%package devel
Summary: Libav devel package
Requires: %{name} = %{version}

%description devel
Libav provides cross-platform tools and libraries to convert, manipulate and stream a wide range of multimedia formats and protocols.

%package tools
Summary: Libav tools package
Requires: %{name} = %{version}

%description tools
Libav provides cross-platform tools and libraries to convert, manipulate and stream a wide range of multimedia formats and protocols.

%prep
%setup
rm -rf $RPM_BUILD_ROOT
./configure --prefix=/usr --disable-debug --enable-shared --disable-static

%build
make

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_datadir}/avconv/*.avpreset

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libavcodec/*.h
%{_includedir}/libavdevice/*.h
%{_includedir}/libavfilter/*.h
%{_includedir}/libavformat/*.h
%{_includedir}/libavresample/*.h
%{_includedir}/libavutil/*.h
%{_includedir}/libswscale/*.h

%files tools
%defattr(-,root,root)
%{_bindir}/avprobe
%{_bindir}/avconv
