#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# Author : Thomas Schmeiduch @schtho

from cmk.utils.site import omd_site

register_notification_parameters("urlcall", Dictionary(
    elements = [
        ("request_url",
            ListOfStrings(
                title=_("Request URL"),
                orientation="vertical",
                 help=_("Your URL to request, for example: https://myservice.com/test "
                        "Also supports variables such as $HOSTNAME$ "),
                allow_empty=False,
                size="max",
                default_value="",
            ),
        ),
        ("request_body",
            TextAreaUnicode(
                title=_("URL Body"),
                help = _("Add Body to Request"),
                default_value="",
                cols=40,
                rows="auto",
            ),
        ),
        ("request_method", DropdownChoice(
            title=_("Request Method"),
            help = _("Select the Method of Request"),
            choices=[
                ("GET", _("GET")),
                ("POST", _("POST")),
                ("PUT", _("PUT")),
                ("DELETE", _("DELETE")),
            ],
            default_value="GET",
        )),
    ]
))