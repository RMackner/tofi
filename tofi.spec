%define githash 89c713a9d5a8ee5cdb0fa728a171231391463fdf

%define shorthash %(c=%{githash}; echo ${c:0:10})


Name:           tofi
Version:        8.git.%{shorthash}v0.6.0
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
BuildRequires:  clang-devel
BuildRequires:  llvm-devel

%description
%{summary}

%prep
%autosetup -n %{name}-%{githash}

%build
CC=clang CXX=clang++ meson build-clang

%install
export DESTDIR=%{buildroot}
ninja -C build-clang install

%files
%{_sysconfdir}/xdg/%{name}/config
%{_bindir}/%{name}
%{_bindir}/%{name}-drun
%{_bindir}/%{name}-run
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/bash-completion/completions/%{name}-drun
%{_datadir}/bash-completion/completions/%{name}-run
%{_datadir}/licenses/%{name}/LICENSE
%{_mandir}/man*/%{name}*.gz


%changelog
%autochangelog
