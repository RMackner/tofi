Name:           rofi
Version:        1.7.5
Release:        1
Summary:        A wayland window switcher, run dialog and dmenu replacement
License:        MIT
Group:          System/GUI/Other
Url:            https://github.com/lbonn/%{name}
Source:         https://github.com/lbonn/%{name}/archive/refs/tags/%{version}+wayland1.tar.gz
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  cppcheck
BuildRequires:  flex
BuildRequires:  librsvg2-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel
BuildRequires:  meson
Requires:       xdg-utils

%description
rofi is a popup window switcher roughly based on "superswitcher",
requiring only xlib and pango. This version started off as a clone of
simpleswitcher, the version from Sean Pringle. Rofi developed extra
features, like a run dialog, SSH launcher and can act as a drop-in
dmenu replacement.

%package devel
Summary:        Development files for rofi
Group:          Development/Libraries/C and C++

%description devel
Development files and headers for rofi

%prep
%setup -q

%build
meson build -Dxcb=disabled
ninja -C build

%install
ninja -C build install

%files
%license COPYING
%doc Changelog README.md
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%dir %{_datadir}/rofi/
%{_datadir}/rofi/themes/
%{_mandir}/man*/*

%files devel
%{_includedir}/rofi/
%{_libdir}/pkgconfig/rofi.pc

%changelog
* Mon Oct 15 2018 Brenton Horne <brentonhorne77@gmail.com> - 1.5.1-2
- Adding gcc as a build dependency, apparently it is not installed for 
  F29/Rawhide as a dependency of other build dependencies.
* Mon Oct 15 2018 Brenton Horne <brentonhorne77@gmail.com> - 1.5.1-1
- Initial commit to git repository, with the spec file taken from revision 3 of
  the OBS repository. This spec file is largely taken from openSUSE's.
