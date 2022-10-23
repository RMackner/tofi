%define githash a6fa0ebe77df9d1750ba3d035f55282dde9dcc87

%define shorthash %(c=%{githash}; echo ${c:0:10})


Name:           tofi
Version:        5.git.%{shorthash}v0.6.0
Release:        %autorelease
Summary:        An extremely fast and simple dmenu / rofi replacement for wlroots-based Wayland compositors
License:        MIT
URL:            https://github.com/philj56/tofi
Source0:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz
Conflicts:      tofi

Requires: harfbuzz
Requires: cairo
Requires: pango
Requires: libxkbcommon

BuildRequires:  meson
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
%autosetup -n %{name}-%{githash}

%build
meson _build
ninja -C _build/

%install
export DESTDIR=%{buildroot}
ninja -C _build/ install

%files
/etc/xdg/tofi/*
/usr/bin/*
/usr/lib/debug/usr/bin/*
/usr/share/bash-completion/completions/*
/usr/share/licenses/*
/usr/share/man/*


%changelog
%autochangelog
