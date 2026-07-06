# netbird — RPM package

An RPM package of [netbird](https://github.com/netbirdio/netbird), derived from the [openSUSE package](https://build.opensuse.org/package/show/openSUSE:Factory/netbird). Builds the client, `combined`, `management`, `signal`, and `relay` server components and shell completions.

## COPR Build Status

- netbird: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird/)
- netbird-server: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-server/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-server/)
- netbird-management: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-management/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-management/)
- netbird-relay: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-relay/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-relay/)
- netbird-signal: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-signal/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-signal/)
- netbird-ui: [![Copr build status](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-ui/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/highpingblorg/netbird/package/netbird-ui/)

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
