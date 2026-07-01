# netbird — Enterprise Linux (EL8/9/10) RPM

An EL8/9/10 RPM packaging of [netbird](https://github.com/netbirdio/netbird), derived from the [openSUSE package](https://build.opensuse.org/package/show/openSUSE:Factory/netbird). Builds the client plus optional `management`, `signal`, and `relay` server components and shell completions.

## Files

```
netbird.spec                  client: netbird + bash/fish/zsh-completion + service
netbird-management.spec       management server + completions + service
netbird-signal.spec           signal server + completions + service
netbird-relay.spec            relay server (no unit yet)
netbird-ui.spec               GUI tray applet (needs EPEL GUI libs)
netbird.service               client systemd unit    (Source2 of netbird.spec)
netbird-management.service    management server unit  (Source3 of netbird-management.spec)
netbird-signal.service        signal server unit      (Source4 of netbird-signal.spec)
