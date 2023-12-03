from pydub import AudioSegment


def slice_and_combine(files_with_times, output_file):
    segments = []
    for file_with_time in files_with_times:
        song = AudioSegment.from_mp3(file_with_time['file'])
        start_time = file_with_time['start_time'] * 1000  # pydub works in milliseconds
        end_time = file_with_time['end_time'] * 1000
        segment = song[start_time:end_time]
        #segment = segment.fade_in(2000).fade_out(2000)
        if segments:  # if there are already segments in the list
            # Crossfade the last segment with the new one
            segments[-1] = segments[-1].append(segment, crossfade=1500)  # 1500 milliseconds crossfade
        else:
            segments.append(segment)
        #segments.append(segment)

    combined = sum(segments)

    combined.export(output_file, format='mp3')



files_with_times = [
    {'file': '../songs/Onakka_Munthiri.mp3', 'start_time': 9, 'end_time': 46},
    {'file': '../songs/Jimikki_Kammal.mp3', 'start_time': 23, 'end_time': 71},
    {'file': '../songs/Butta_bomma.mp3', 'start_time': 9.5, 'end_time': 42.5},
    {'file': '../songs/Halamithi_Habibo.mp3', 'start_time': 0, 'end_time': 40},
    {'file': '../songs/Gaandha_kannazhagi.mp3', 'start_time': 50, 'end_time': 86},
    {'file': '../songs/Pala_palli.mp3', 'start_time': 20, 'end_time': 94},
    {'file': '../songs/Ranjithame.mp3', 'start_time': 34.5, 'end_time': 69.5},
    {'file': '../songs/Ranjithame.mp3', 'start_time': 201, 'end_time': 302},
]
output_file = "../songs/combined.mp3"
slice_and_combine(files_with_times, output_file)
