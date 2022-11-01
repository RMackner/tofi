#rofi
%define githash fd0ef6bc1514a83dd18d74436cfe103444df1b6d

#libgwater
%define githash2 42a145150cff135be377754486c504836ddea836

#libnkutils
%define githash3 b39df45e80fa6bcb40b1be8266d9d9b06854e19b

%define shorthash %(c=%{githash}; echo ${c:0:10})




Name:          rofi
Version:       1.7.5
Release:       5.git.%{shorthash}%{?dist}
Summary:       A window switcher, run dialog and dmenu replacement - fork with wayland support
License:       MIT
URL:           https://github.com/lbonn/%{name}/archive
Source0:       https://github.com/lbonn/rofi/archive/%{githash}.tar.gz
Source2:       https://github.com/sardemff7/libgwater/archive/%{githash2}.tar.gz
Source3:       https://github.com/sardemff7/libnkutils/archive/%{githash3}.tar.gz


BuildArch: x86_64
Requires: xcb-util-cursor
BuildRequires: gcc-c++, meson, check, make, autoconf, bison, glibc
BuildRequires: automake >= 1.11.3
BuildRequires: flex >= 2.5.39
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-xcb)
BuildRequires: pkgconfig(check) >= 0.11.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: git

%description
%{summary}

%prep
%autosetup -n %{name}-%{githash}
cd /builddir/build/BUILD
/usr/bin/tar xvf /builddir/build/SOURCES/%{githash2}.tar.gz
/usr/bin/tar xvf /builddir/build/SOURCES/%{githash3}.tar.gz
cd libgwater-%{githash2}
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
cd /builddir/build/BUILD
cd libnkutils-%{githash3}
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
cd /builddir/build/BUILD
cp -r ./libgwater-%{githash2}/* ./%{name}-%{githash}/subprojects/libgwater/
cp -r ./libnkutils-%{githash3}/* ./%{name}-%{githash}/subprojects/libnkutils/

%build
MESON_OPTIONS=(
    -Dcheck=disabled
)
%meson "${MESON_OPTIONS[@]}"
%meson_build

%install
%meson_install

%find_lang rofi
	
%files -f rofi.lang
%{_datadir}/%{name}/themes/*
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_mandir}/man5/%{name}*
%{_mandir}/man1/%{name}*
%{_includedir}/%{name}/*
%{_datadir}/applications/rofi-theme-selector.desktop
%{_datadir}/applications/rofi.desktop
%{_datadir}/icons/hicolor/scalable/apps/rofi.svg
%{_libdir}/pkgconfig/rofi.pc
