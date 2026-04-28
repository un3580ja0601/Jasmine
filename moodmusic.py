user_mood = input("What's your mood? (calm, energetic, sad, happy, loving): ")

# This list stores songs and their moods.
# Using a list keeps the program simpler because we can store multiple songs instead of creating separate variables for each song.

songs = [
    ["Moon - Daniel Caesar", "calm"],
    ["Over the Moon - The Marías", "calm"],
    ["Body - Don Toliver", "energetic"],
    ["Ladygirl - Malcolm Todd", "energetic"],
    ["Superficial - Avenoir", "sad"],
    ["Is it a Crime? - Montell Fish", "sad"],
    ["The Spins - Mac Miller", "happy"],
    ["CAN'T STOP THE FEELING! - Justin Timberlake", "happy"],
    ["Risk it All - Bruno Mars", "loving"],
    ["Everybody Here Wants You - Jeff Buckley", "loving"]
]

'''
Student developed function

Takes in a list of songs and a mood.

parameters:
songs - a list of [song name, mood] pairs (strings)
mood - the mood used to filter songs

return type:
list or None - a list of song names that match the mood,
or None if no matches are found
'''
def matchsong(songs, mood):
    matching = None

    #Iteration
    for song in songs:
        # Selection
        if song[1] == mood:
            if matching == None:
                matching = []
            matching.append(song[0])

    return matching


result = matchsong(songs, user_mood)

if result == None:
    print("No songs found for that mood.")
else:
    print("Songs that match your mood:")
    for song in result:
        print("- " + song)
      
