#
# spec file for package netbird-management
#
# Derived from the openSUSE netbird package
#

%global debug_package %{nil}

Name:           netbird-ui
Version:        0.73.2
Release:        0%{?dist}
Summary:        UI panel indicator applet for netbird
License:        AGPL-3.0-only AND BSD-3-Clause
URL:            https://github.com/netbirdio/netbird
Source0:        https://github.com/netbirdio/netbird/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  golang >= 1.25
BuildRequires:  hicolor-icon-theme
BuildRequires:  libayatana-appindicator-gtk3-devel
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(xxf86vm)
Requires:       netbird
# Replaces the openSUSE "netbird-applet" subpackage name.
Provides:       netbird-applet = %{version}-%{release}

%description
Optional UI panel indicator applet for netbird.

%prep
%autosetup -n netbird-%{version}

%build
export GOFLAGS="-mod=mod"
export GOPROXY="https://proxy.golang.org,direct"
export GOTOOLCHAIN=auto

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

export LDFLAGS="-X github.com/netbirdio/netbird/version.version=v%{version} \
    -X main.date=${BUILD_DATE} -X main.builtBy=copr"

go build -o netbird-ui -buildmode=pie -ldflags "$LDFLAGS" ./client/ui

%install
install -Dm755 netbird-ui %{buildroot}%{_bindir}/netbird-ui
install -Dm644 client/ui/build/netbird.desktop %{buildroot}%{_datadir}/applications/netbird.desktop
# All icons are 256x256. These seem to get pulled into the applet binary
# regardless, but still worth throwing in separately.
install -dm755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -Dm644 client/ui/assets/netbird*.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
# The system-tray-connected icon is the same as netbird.ico, which won't be
# picked up by xdg with .ico metadata.
install -Dm644 client/ui/assets/netbird-systemtray-connected.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/netbird.png

%fdupes %{buildroot}%{_datadir}/icons/

%files
%license LICENSE
%{_bindir}/netbird-ui
%{_datadir}/applications/netbird.desktop
%{_datadir}/icons/hicolor/256x256/apps/netbird*.png

%changelog
* Wed Jul 01 2026 highpingblorg@pm.me - 0.73.2-0
- Initial EL8/9/10 port of the netbird UI applet, split into its own spec and
  always built (no longer optional).
- Fetch source from GitHub by tag; build Go modules live (requires build network
  access).
