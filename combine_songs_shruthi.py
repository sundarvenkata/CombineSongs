from pydub import AudioSegment


def slice_and_combine(files_with_times, output_file):
    segments = []
    for file_with_time in files_with_times:
        song = AudioSegment.from_mp3(file_with_time['file'])
        start_time = file_with_time['start_time'] * 1000  # pydub works in milliseconds
        end_time = file_with_time['end_time'] * 1000
        segment = song[start_time:end_time]
        #segment = segment.fade_in(2000).fade_out(2000)
        # if segments:  # if there are already segments in the list
        #     # Crossfade the last segment with the new one
        #     segments[-1] = segments[-1].append(segment, crossfade=1500)  # 1500 milliseconds crossfade
        # else:
        segments.append(segment)
        #segments.append(segment)

    combined = sum(segments)

    combined.export(output_file, format='mp3')


if __name__ == "__main__":
    files_with_times = [
        {'file': '../songs/Onakka_Munthiri.mp3', 'start_time': 9, 'end_time': 46},
        {'file': '../songs/Jimikki_Kammal.mp3', 'start_time': 23, 'end_time': 69},
        {'file': '../songs/Butta_bomma.mp3', 'start_time': 42.5, 'end_time': 83},
        {'file': '../songs/Halamithi_Habibo.mp3', 'start_time': 0, 'end_time': 40},
        {'file': '../songs/Gaandha_kannazhagi.mp3', 'start_time': 50, 'end_time': 96.5},
        {'file': '../songs/Ranjithame.mp3', 'start_time': 34.5, 'end_time': 68.5},
        {'file': '../songs/Pala_palli.mp3', 'start_time': 32.5, 'end_time': 90}
    ]
    output_file = "../songs/combined_shruthi.mp3"
    slice_and_combine(files_with_times, output_file)
