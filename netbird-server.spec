#
# spec file for package netbird-server
#
# Derived from the openSUSE netbird package
#
%global debug_package %{nil}

Name:           netbird-server
Version:        0.73.2
Release:        0%{?dist}
Summary:        Backend combined server (Management + Signal + Relay + STUN)
License:        AGPL-3.0-only AND BSD-3-Clause
URL:            https://github.com/netbirdio/netbird
Source0:        https://github.com/netbirdio/netbird/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  git-core
BuildRequires:  golang >= 1.25
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libpcap)
%{?systemd_requires}

%description
Combined netbird backend server. This comrpises the full server.
It includes the Management, Signal, Relay and STUN services.


%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

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

go build -o netbird-server -buildmode=pie -ldflags "$LDFLAGS" ./combined

%install
install -Dm755 -t %{buildroot}%{_bindir} netbird-server

# Generate completions
for sh in bash zsh fish; do
  ./netbird-server completion $sh --config=/dev/null > netbird-server.${sh}
done
install -Dm644 netbird-server.bash %{buildroot}%{_datadir}/bash-completion/completions/netbird-server
install -Dm644 netbird-server.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_netbird-server
install -Dm644 netbird-server.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/netbird-server.fish


# Own the persistent netbird directories (co-owned with the other components).
# Directory=, but owning them here guarantees they exist on install.
install -d %{buildroot}%{_sysconfdir}/netbird
install -d %{buildroot}/var/log/netbird
install -d %{buildroot}/var/lib/netbird


%files
%license LICENSE
%{_bindir}/netbird-server
%dir %{_sysconfdir}/netbird
%dir /var/log/netbird
%dir /var/lib/netbird

%files bash-completion
%{_datadir}/bash-completion/completions/netbird-server

%files fish-completion
%{_datadir}/fish/vendor_completions.d/netbird-server.fish

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_netbird-server

%changelog
* Wed Jul 01 2026 highpingblorg@pm.me - 0.73.2-0
- Initial EL8/9/10 port of the netbird combined server, split into its own spec.
- Fetch source from GitHub by tag; build Go modules live (requires build network
  access); EL %%systemd_* scriptlets.
