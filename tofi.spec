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
meson _build
ninja -C _build/

%install
export DESTDIR=%{buildroot}
ninja -C _build/ install

%files
/etc/xdg/tofi/config
/usr/bin/tofi
/usr/bin/tofi-drun
/usr/bin/tofi-run
/usr/lib/debug/usr/bin/tofi-0.6.0-1.fc37.x86_64.debug
/usr/share/bash-completion/completions/tofi
/usr/share/bash-completion/completions/tofi-drun
/usr/share/bash-completion/completions/tofi-run
/usr/share/licenses/tofi/LICENSE
/usr/share/man/man1/tofi-drun.1.gz
/usr/share/man/man1/tofi-run.1.gz
/usr/share/man/man1/tofi.1.gz
/usr/share/man/man5/tofi.5.gz

%changelog
