import emoji

print("This is a test :thumbs_up:")
print(emoji.emojize("This is a test :thumbs_up:"))
print(emoji.emojize("That was really funny! :grinning_face_with_big_eyes:"))

for k, v in emoji.UNICODE_EMOJI.items():
    print(emoji.emojize(v))