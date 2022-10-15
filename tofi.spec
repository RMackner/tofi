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
BuildRequires:  git
BuildRequires:  scdoc
BuildRequires:  wayland-protocols

%description
%{summary}

%prep
%autosetup -p 1 -c

%build
meson --prefix /usr -Dbuildtype=release build
ninja -C build

%install
ninja -C build install

%files

%changelog
