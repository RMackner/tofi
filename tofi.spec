Name:           tofi
Version:        0.6.0
Release:        %autorelease
Summary:        An extremely fast and simple dmenu / rofi replacement for wlroots-based Wayland compositors
License:        MIT
URL:            https://github.com/philj56/tofi
Source0:        https://github.com/RMackner/tofi/blob/main/0.6.0.tar.gz
Conflicts:      tofi

Requires: freetype2
Requires: harfbuzz
Requires: cairo
Requires: pango
Requires: wayland
Requires: libxkbcommon

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  scdoc
BuildRequires:  wayland-protocols-devel
BuildRequires:  wayland-devel
BuildRequires:  cairo-devel
BuildRequires:  glibc-devel
BuildRequires:  pango-devel
BuildRequires:  libxkbcommon-devel

%description
%{summary}

%prep
%setup

%build
%meson_build

%install
%meson_install

%files

%changelog
