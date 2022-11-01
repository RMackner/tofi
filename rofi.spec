Name:          rofi
Version:       1.7.5
Release:       2
Summary:       A window switcher, run dialog and dmenu replacement - fork with wayland support
License:       MIT
URL:           https://github.com/lbonn/%{name}/archive
Source:        %{name}-%{version}.tar.gz


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
git clone https://github.com/lbonn/rofi.git --recursive
%autosetup -n %{name}

%build
MESON_OPTIONS=(
    -Dcheck=disabled
)
%meson "${MESON_OPTIONS[@]}"
%meson_build

%install
%meson_install

%files
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
