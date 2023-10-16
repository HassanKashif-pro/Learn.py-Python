from replit import audio

def play():
    source = audio.play_file('audio_wav')
    while True:
        print("MyPOD Music Player")
        options = input("Press 1 to Play, "
                        "Press 2 to Exit, "
                        "Anything else will start it again: ")
        if options == '1':
            audio.play_file('audio_wav')
        elif options == '2':
            break

play()
