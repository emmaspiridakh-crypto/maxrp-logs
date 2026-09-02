EMOJIS = {
    "tickets": {
        "ticket": "<:ticket:1542760164082581574>",
    },
    "moderation": {
        "ban": "<:ban:1542761372163506297>",
        "unban": "<:unban:1542761372163506297>",
        "kick": "<a:kick:1542761467600965653>",
        "timeout": "<:timeout:1542500072405606582>",
        "untimeout": "<:untimeout:1542500072405606582>",
        "clear": "<:clear:1542760611530670111>",
    },
    "staff_activity": {
        "on_duty": "<a:on_duty:1542499780163280938>",
        "off_duty": "<a:off_duty:1542499714786787459>",
        "leaderboard": "<:leaderboard:1542759680009576479>",
    },
    "applications": {
        "apply": "<:apply:1542816408281415761>",
    },
    "notifier": {
        "bell": "<a:notif_bell:1542760099141918820>",
        "clock": "<:notif_clock:1542817309393944576>",
    },
    "panel": {
        "scan": "<:scan:1542817856582979584>",
    },
    "whitelist": {
        "accept": "<:wl_accept:1542500013383618640>",
    },
}


def emoji(category: str, name: str) -> str:
    try:
        return EMOJIS[category][name]
    except KeyError:
        return ""
