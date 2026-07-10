# netbird — RPM package

An RPM package of [netbird](https://github.com/netbirdio/netbird), derived from the [openSUSE package](https://build.opensuse.org/package/show/openSUSE:Factory/netbird). Builds the client, `combined`, `management`, `signal`, and `relay` server components and shell completions.

## Overview

### netbird

Status: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird/)

Supported >= EL8

### netbird-server

Status: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-server/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-server/)

Supported >= EL8

### netbird-management
Status: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-management/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-management/)

Supported >= EL8

### netbird-relay

Status: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-relay/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-relay/)

Supported >= EL8

### netbird-signal

Status: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-signal/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-signal/)

Supported >= EL8

### netbird-ui

Status: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-ui/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-ui/)

Supported >= EL9

## Releasing

Bump `Version:` in the spec files, commit, then push a `v<version>` tag. The [COPR build workflow](.github/workflows/copr-build.yml) submits a build of the tagged commit for every package in the [highpingblorg/netbird](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/) COPR project and reports the results.

## Files

```
netbird.spec                  client: netbird + bash/fish/zsh-completion + service
netbird-management.spec       management server + completions + service
netbird-signal.spec           signal server + completions + service
netbird-server.spec           combined server (management + Signal + Relay) + completions + service
netbird-relay.spec            relay server (no unit yet)
netbird-ui.spec               GUI tray applet (needs EPEL GUI libs)
netbird.service               client systemd unit    (Source2 of netbird.spec)
netbird-management.service    management server unit  (Source3 of netbird-management.spec)
netbird-signal.service        signal server unit      (Source4 of netbird-signal.spec)
netbird-server.service        combined server unit      (Source5 of netbird-signal.spec)
