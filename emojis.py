EMOJIS = {
    "tickets": {
        "ticket": "<:ticket:1547991426497773688>",
    },
    "moderation": {
        "ban": "<:ban:1548269903780511785>",
        "unban": "<:unban:1548269903780511785>",
        "kick": "<a:kick:1548286893920223253>",
        "timeout": "<:timeout:1548269753485762611>",
        "untimeout": "<:untimeout:1548269753485762611>",
        "clear": "<:clear:1548269195844915201>",
    },
    "staff_activity": {
        "on_duty": "<a:on_duty:1548269590197575701>",
        "off_duty": "<a:off_duty:1548269566659002479>",
        "leaderboard": "<:leaderboard:1548270973285957662>",
    },
    "applications": {
        "apply": "<:apply:1548269878438531184>",
    },
    "notifier": {
        "bell": "<a:notif_bell:1548269105642209291>",
        "clock": "<:notif_clock:1548284144025473054>",
    },
    "panel": {
        "scan": "<a:scan:1547992308492935209>",
    },
    "whitelist": {
        "accept": "<:wl_accept:1548269957039525918>",
    },
}


def emoji(category: str, name: str) -> str:
    try:
        return EMOJIS[category][name]
    except KeyError:
        return ""
