#
# spec file for package netbird-management
#
# Derived from the openSUSE netbird package
#

%global debug_package %{nil}

Name:           netbird-relay
Version:        0.73.2
Release:        0%{?dist}
Summary:        Backend relay server component for netbird
License:        AGPL-3.0-only AND BSD-3-Clause
URL:            https://github.com/netbirdio/netbird
Source0:        https://github.com/netbirdio/netbird/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  git-core
BuildRequires:  golang >= 1.25
BuildRequires:  pkgconfig(libpcap)

%description
Optional relay server component for netbird. Please note that this does not
comprise a full netbird backend server, and is merely built for convenience.
Management/signal/relay are not required for the netbird client application.

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

go build -o %{name} -buildmode=pie -ldflags "$LDFLAGS" ./relay

%install
install -Dm755 -t %{buildroot}%{_bindir} %{name}

# Own the persistent netbird directories (co-owned with the other components).
install -d %{buildroot}%{_sysconfdir}/netbird
install -d %{buildroot}/var/log/netbird
install -d %{buildroot}/var/lib/netbird

%files
%license LICENSE
%{_bindir}/%{name}
%dir %{_sysconfdir}/netbird
%dir /var/log/netbird
%dir /var/lib/netbird

%changelog
* Wed Jul 01 2026 highpingblorg@pm.me - 0.73.2-0
- Initial EL8/9/10 port of the netbird relay server, split into its own spec.
- Fetch source from GitHub by tag; build Go modules live (requires build network
  access).
