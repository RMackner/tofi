%define githash 0d779ef6359ff8a66b7c22ca7dee6b6097faa903

%define shorthash %(c=%{githash}; echo ${c:0:10})


Name:           tofi
Version:        6.git.%{shorthash}v0.6.0
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



%changelog
%autochangelog
