def convert_category_to_num(default_category_str):
    if default_category_str != "":
        if default_category_str == "Promotion pitch":
            return 0
        elif default_category_str == "Pickup lines":
            return 1
        elif default_category_str == "Interview pitch":
            return 2
        elif default_category_str == "Product pitch":
            return 3


def convert_num_to_category(default_category_str):
    if default_category_str >= 0:
        if default_category_str == 0:
            return "Promotion pitch"
        elif default_category_str == 1:
            return "Pickup lines"
        elif default_category_str == 2:
            return "Interview pitch"
        elif default_category_str == 3:
            return "Product pitch"
        else:
            return "All"


def convert_ids_string_to_array(ids_str: str):
    if ids_str != "":
        ids_array = []
        split_str = ids_str.split(",")
        for item in split_str:
            if item != "" and item.isnumeric():
                ids_array.append(int(item.strip()))
    else:
        ids_array = []
    return ids_array


def convert_ids_array_to_string(ids_array: list):
    global ids_str
    if ids_array:
        ids_str = ""
        for my_id in ids_array:
            ids_str += f",{my_id}"

    return ids_str


def format_pitches_array(pitches_array):
    if pitches_array:
        from app.models import Pitch
        formatted_pitches_array = []
        for pitch in pitches_array:
            pitch_txt = pitch.pitch_txt
            pitch_category = pitch.pitch_category
            pitch_upvt = len(convert_ids_string_to_array(pitch.upvt))
            pitch_dwnvt = len(convert_ids_string_to_array(pitch.dwnvt))
            pitch_timestamp = pitch.timestamp
            pitch_creator_id = pitch.creator_id
            pitch_comments = len(convert_ids_string_to_array(pitch.comments))

            formatted_pitch = Pitch(id=pitch.id, pitch_txt=pitch_txt, comments=pitch_comments,
                                    timestamp=pitch_timestamp, upvt=pitch_upvt, dwnvt=pitch_dwnvt,
                                    creator_id=pitch_creator_id, pitch_category=pitch_category)
            formatted_pitches_array.append(formatted_pitch)
        return formatted_pitches_array
    else:
        return pitches_array
