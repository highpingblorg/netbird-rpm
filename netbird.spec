#
# spec file for package netbird-management
#
# Derived from the openSUSE netbird package
#
%global debug_package %{nil}

Name:           netbird
Version:        0.74.3
Release:        0%{?dist}
Summary:        Mesh VPN based on WireGuard
License:        AGPL-3.0-only AND BSD-3-Clause
URL:            https://github.com/netbirdio/netbird
Source0:        https://github.com/netbirdio/netbird/archive/refs/tags/v%{version}.tar.gz
Source2:        %{name}.service
BuildRequires:  git-core
BuildRequires:  golang >= 1.25
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libpcap)
%{?systemd_requires}

%description
NetBird combines a configuration-free peer-to-peer private network and a
centralized access control system in a single platform, making it easy to
create secure private networks for your organization or home.

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
%autosetup

%build
# Live module fetch: no vendored deps are bundled. Requires build network access.
export GOFLAGS="-mod=mod"
export GOPROXY="https://proxy.golang.org,direct"
export GOTOOLCHAIN=auto

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

export LDFLAGS="-X github.com/netbirdio/netbird/version.version=v%{version} \
    -X main.date=${BUILD_DATE} -X main.builtBy=copr"

go build -o %{name} -buildmode=pie -ldflags "$LDFLAGS" ./client

%install
install -Dm755 -t %{buildroot}%{_bindir} %{name}

# Generate completions
for sh in bash zsh fish; do
  ./%{name} completion $sh > %{name}.${sh}
done
install -Dm644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 %{name}.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

# Install service file
install -Dm644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

# Prepare config directory which netbird will populate once configured by user
install -d %{buildroot}%{_sysconfdir}/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md SECURITY.md AUTHORS CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTOR_LICENSE_AGREEMENT.md
%dir %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Fri Jul 10 2026 highpingblorg@pm.me - 0.74.3-0
- Bump netbird version to 0.74.3
* Mon Jul 06 2026 highpingblorg@pm.me - 0.74.2-0
- Bump netbird version to 0.74.2
* Wed Jul 01 2026 highpingblorg@pm.me - 0.73.2-0
- Initial EL8/9/10 port of the netbird client, derived from the openSUSE package.
- Fetch source from GitHub by tag; build Go modules live (requires build network
  access); no vendored deps.
- EL %%systemd_* scriptlets; split out from the management/signal/relay/ui specs.
