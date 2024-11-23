import os
import subprocess

def create_folder() -> str:
    dir_path = os.path.expanduser("~/Desktop/downloaded_audio")

    # check if the path exists
    if os.path.exists(dir_path):
        print("\nOutput Directory / Folder Already Exists!\n")
    # if the directory / folder does not exists
    else:
        print("\nCreating Output Folder\n")
        # create the directory / folder
        os.mkdir(os.path.expanduser("~/Desktop/downloaded_audio"))

    return dir_path

def main():

    user_url = input("\nPlease Enter YouTube URL: ")

    path = create_folder()

    file_name = os.path.join(path + "/%(title)s.%(ext)s")

    yt_audio_cmd = ["yt-dlp", user_url, "--format", "m4a", "-o", file_name]


    yt_audio_cmd_2 = ["yt-dlp", user_url, "--format", "bestaudio", "--extract-audio", "--audio-format", "m4a", "-o", file_name]
    # run the command in shell
    # NOTE: thinking of using this command
    subprocess.run(yt_audio_cmd)
    # NOTE: its good this one, but it needs to delete the .webm file... one more step
    # subprocess.run(yt_audio_cmd_2)

    print("\nConverting to MP3\n")

    os.chdir(os.path.expanduser("~/Desktop/downloaded_audio/"))
    for item in os.listdir():
        input_file = item
        file_name_wo_ext = os.path.splitext(item)[0]
        output_file = os.path.join(file_name_wo_ext + ".mp3")

        # ffmpeg_mp3_cmd = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", "-q:a", "0", "-ar", "44100", "-y", output_file]
        # ffmpeg_mp3_cmd = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", "-ab", "192k", "-ar", "44100", "-y", output_file]

        ffmpeg_mp3_cmd = [
            "ffmpeg", 
            "-i", input_file, 
            "-vn", 
            "-acodec", "libmp3lame", 
            "-ab", "192k", 
            "-ar", "44100", 
            "-f", "mp3",  # Explicitly specify the format
            "-y", 
            output_file
        ]

        subprocess.run(ffmpeg_mp3_cmd)

        # remove m4a file
        # os.remove(input_file)


if __name__ == '__main__':
    main()
