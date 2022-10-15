%define githash bcee4e15d3e4d970d477ca3ad1cc7b1b4c691345

%define shorthash %(c=%{githash}; echo ${c:0:10})

Name:           tofi
Version:        0.6.0
Release:        7.git.%{shorthash}%{?dist}
Summary:        An extremely fast and simple dmenu / rofi replacement for wlroots-based Wayland compositors
License:        MIT
URL:            https://github.com/philj56/tofi
Source0:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz
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
%autosetup -n

%build
meson --prefix /usr -Dbuildtype=release build
ninja -C build

%install
ninja -C build install

%files

%changelog
