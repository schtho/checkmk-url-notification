# checkmk-url-notification
This Checkmk Notification Plugin provides support for calling URLs.

## Example URL
This plugin supports variables:
```
http://192.168.1.10:8080/set/myagent?value=$HOSTNAME$
```

## References
For more Documentation or Debugging:
- OMD Shell: `nano ~/lib/check_mk/gui/plugins/wato/notifications.py`
- https://docs.checkmk.com/latest/de/notifications.html#scripts
- `tail -f ~/var/log/notify.log`
- `tail -f ~/var/log/web.log`
