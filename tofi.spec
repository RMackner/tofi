%define githash 89c713a9d5a8ee5cdb0fa728a171231391463fdf

%define shorthash %(c=%{githash}; echo ${c:0:10})


Name:           tofi
Version:        7.git.%{shorthash}v0.6.0
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
%{_sysconfdir}/xdg/tofi/config
%{_bindir}/tofi
%{_bindir}/tofi-drun
%{_bindir}/tofi-run
%{_datadir}/bash-completion/completions/tofi
%{_datadir}/bash-completion/completions/tofi-drun
%{_datadir}/bash-completion/completions/tofi-run
%{_datadir}/licenses/tofi/LICENSE
%{_mandir}/man1/tofi*.gz
%{_mandir}/man5/tofi*.gz


%changelog
%autochangelog
