import shortuuid


def get_meeting_response(user_mentions: list, room_name: str) -> str:
    return f"""
---
#### Meeting
Entrem aí {", ".join(user_mentions)}

{room_name}
---
"""


def get_meeting_name(name: [str, None]) -> str:
    if not name or name[0] == "%":
        return shortuuid.uuid()
    return name.split("+%40")[0]


def mattermost_command_to_json(text: str) -> dict:
    splitted_text = text.split("&")
    fields = {
        "user_mentions": [],
        "user_mentions_ids": [],
        "channel_mentions": [],
        "channel_mentions_ids": [],
    }
    for field_name_and_field_value in splitted_text:
        field, value = field_name_and_field_value.split("=")
        if field in fields.keys():
            fields[field].append(value)
        else:
            fields[field] = value
    return fields
