import os
import subprocess
import glob


# function to display dashed lines
def print_dashed_line():
    print()
    print('-'*50)
    print()


# function to create folders at required directory
# depending if downloading audio / video; will create folder with respective name
def create_folder(user_option: str):
    # check for the user's option
    if user_option == "audio":
        # meaning user wants to download audio
        dir_path = os.path.expanduser("~/Desktop/downloaded_audio")

        # check if the path exists
        if os.path.exists(dir_path):
            print("<-- Output Directory / Folder Already Exists! -->")
            print_dashed_line()

        # if the directory / folder does not exists
        else:
            print_dashed_line()
            print("<-- Creating Output Folder -->")
            print_dashed_line()
            # create the directory / folder
            # os.mkdir(os.path.expanduser("~/Desktop/downloaded_audio"))
            os.mkdir(dir_path)

    elif user_option == "video":
        # meaning user wants to download audio
        dir_path = os.path.expanduser("~/Desktop/downloaded_video")

        # check if the path exists
        if os.path.exists(dir_path):
            print("<-- Output Directory / Folder Already Exists! -->")
            print_dashed_line()

        # if the directory / folder does not exists
        else:
            print_dashed_line()
            print("<-- Creating Output Folder -->")
            print_dashed_line()
            # create the directory / folder
            # os.mkdir(os.path.expanduser("~/Desktop/downloaded_video"))
            os.mkdir(dir_path)


# function to check for the file size
def check_file_size(file_path: str):
    # exception handling
    try:
        # get the size of the file in question
        txt_file_size = os.path.getsize(file_path)

        # output appropriate message based on size of text file
        # NOTE: this method `.getsize()` return size in bytes
        if txt_file_size == 0:
            # meaning that we have nothing in the file
            print_dashed_line()
            print("<-- The Text File Does NOT Contains Any URLs... Exiting!!! -->")
            print_dashed_line()

            # exit the program
            exit(0)

    # if file has not been found
    except FileNotFoundError as e:
        # NOTE: extracting the file name in the `except` part
        # so that it does not run if the text file has stuff in it ( innit )

        # split the path of file into a list
        path_split = file_path.split("/")
        # get the last value of the list
        file_name = path_split[len(path_split) - 1]

        # output appropriate message
        print(f"\nError: {e}")
        print(f"File '{file_name}' Has NOT Been Found at Desktop!!!")


# function to convert between audio formats
# NOTE: to be used in conjunction with text file as input ==> searches for songs in directory
def convert_audio_format_txt_file(directory_path: str, file_format: str, bitrate: str):
    # evaluate the file format and codecs
    if file_format == "mp3":
        # use the appropriate codec for mp3
        codec = "libmp3lame"

    elif file_format == "wav":
        # use the appropriate codec for wav
        codec = "pcm_s16le"

    else:
        # if the user enters something else
        print_dashed_line()
        print("<-- Invalid File Format Entered... Defaulting to MP3 and Using Default Bitrate -->")
        file_format = "mp3"
        codec = "libmp3lame"

        print_dashed_line()

    # change from the current working directory to where we downloaded the songs
    os.chdir(directory_path)
    # iterate through the whole directory / folder
    for input_song in glob.glob("*.m4a"):
        # out output "file" for the ffmpeg output flag
        output_song = os.path.splitext(input_song)[0]

        # create the ffmpeg command that will be run from Python
        ffmpeg_cmd = [
            "ffmpeg", 
            "-i", input_song, 
            "-vn", 
            "-acodec", codec, 
            "-ab", bitrate, 
            "-ar", "44100", 
            "-f", file_format,
            "-y",
            output_song
        ]

        # run the command from Python
        subprocess.run(ffmpeg_cmd)
        # clean the non-converted file ==> with `.m4a` extension
        os.remove(input_song)


# function to convert between audio formats
# NOTE: to be used with single URLs conversions
def convert_audio_format_single(directory_path: str, file_format: str, bitrate: str):
    # evaluate the file format and codecs
    if file_format == "mp3":
        # use the appropriate codec for mp3
        codec = "libmp3lame"

    elif file_format == "wav":
        # use the appropriate codec for wav
        codec = "pcm_s16le"

    else:
        # if the user enters something else
        print_dashed_line()
        print("<-- Invalid File Format Entered... Defaulting to MP3 and Using Default Bitrate -->")
        file_format = "mp3"
        codec = "libmp3lame"

        print_dashed_line()

    # change from current working directory to where we downloaded the song
    os.chdir(directory_path)
    # iterate through the whole directory / folder
    for input_song in glob.glob("*.m4a"):
        # out output "file" for the ffmpeg output flag
        output_song = os.path.splitext(input_song)[0]

        # create the ffmpeg command that will be run from Python
        ffmpeg_cmd = [
            "ffmpeg", 
            "-i", input_song, 
            "-vn", 
            "-acodec", codec, 
            "-ab", bitrate, 
            "-ar", "44100", 
            "-f", file_format,
            "-y",
            output_song
        ]

        # run the command from Python
        subprocess.run(ffmpeg_cmd)
        # clean the non-convert file ==> with `.m4a` extension
        os.remove(input_song)


# function to convert download YouTube videos into audio format
def audio_downloader():
    try:
        # welcome screen for audio convert + display options
        print("==> Audio Converter Selected\n")
        print("Option [1]: Enter Single YouTube Video")
        print("Option [2]: Use List of URLs from a Text File")
        print("Option [3]: Exit")

        # prompt the user select an option
        user_option = input("\n\nPlease Select An Option: ")

        # evaluate the user's option
        if user_option == "1":
            # user wants to only convert 1 YouTube link / video
            print("\n<-- Converting A Single URL -->")
            print_dashed_line()

            # call the function to create the output directory / folder
            create_folder("audio")

            # variable to hold the output directory / path
            output_path = os.path.expanduser("~/Desktop/downloaded_audio/")
            # variable to hold the output "filename" for the downloaded songs
            output_song_name = os.path.join(output_path + "%(title)s.%(ext)s")

            # prompt the user to enter the YouTube URL
            # WARNING: Remember to write function to check if URL is valid
            yt_url = input("Please Enter YouTube URL to Convert: ")

            print_dashed_line()
            print("<-- Starting Downloading Process -->\n\n")

            # command to execute from Python in shell
            yt_dlp_cmd = [
                    "yt-dlp",
                    yt_url,
                    "--format", "m4a",
                    "-o", output_song_name
                ]

            # run the command from Python to the Terminal
            subprocess.run(yt_dlp_cmd)

            print_dashed_line()
            print("<-- Starting Conversion Process -->\n\n")

            # prompt the user to enter file_format and bitrate
            user_format = input("Please Select Between 'mp3' and 'wav': ")
            user_bitrate = int(input("Please Enter Bit Rate ( 100 - 2000 ): "))

            # perform check on bitrate
            if (user_bitrate >= 100 and user_bitrate <= 2000):
                # everything is good... use user's bitrate
                actual_bitrate = str(user_bitrate) + "k"
            
                print_dashed_line()

            else:
                print("Invalid Range For Bitrate... Defaulting to 192k")
                actual_bitrate = "192k"

                print_dashed_line()
            
            print(f"<-- Converting to {user_format} -->\n\n")

            # call the function to convert to required audio format
            # convert_audio_format_single(output_path, user_format, actual_bitrate)
            convert_audio_format_txt_file(output_path, user_format, actual_bitrate)
        
        elif user_option == "2":
            # user wants to convert YouTube links / videos with Text File
            print_dashed_line()
            print("<-- Converting URLs from Text File -->")
            print_dashed_line()

            # call the function to create the output directory
            create_folder("audio")

            # variable to hold the output directory / path
            output_path = os.path.expanduser("~/Desktop/downloaded_audio/")
            # variable to hold the output "filename" for the downloaded songs
            output_song_name = os.path.join(output_path + "%(title)s.%(ext)s")
            # directory / path for our input file
            text_file = os.path.expanduser("~/Desktop/yt_urls.txt")

            # verify if text file `yt_urls.txt` exists
            if os.path.isfile(text_file) and os.path.exists(text_file):
                # check for contents in the text file
                check_file_size(text_file)

                # if everything is correct start the downloading process
                # command to execute from Python in shell
                yt_dlp_cmd = [
                        "yt-dlp",
                        "-a", text_file,
                        "--format",
                        "m4a",
                        "-o",
                        output_song_name
                    ]

                # run the command from Python to the Terminal
                subprocess.run(yt_dlp_cmd)

                print_dashed_line()
                print("<-- Starting Conversion Process -->\n")

                # prompt the user to enter file_format and bitrate
                user_format = input("Please Select Between 'mp3' and 'wav': ")
                user_bitrate = int(input("Please Enter Bit Rate ( 100 - 2000 ): "))

                # perform check on bitrate
                if (user_bitrate >= 100 and user_bitrate <= 2000):
                    # everything is good... use user's bitrate
                    actual_bitrate = str(user_bitrate) + "k"

                    print_dashed_line()
                
                else:
                    print("Invalid Range For Bitrate... Defaulting to 192k")
                    actual_bitrate = "192k"

                    print_dashed_line()

                print(f"<-- Converting to {user_format} -->\n\n")

                # call the function to convert to required audio format
                convert_audio_format_txt_file(output_path, user_format, actual_bitrate)

            else:
                # user does not have 'yt_urls.txt' file present at `~/Desktop`
                print_dashed_line()
                print("<-- You have no 'yt_urls.txt' File at Desktop Directory!!! -->")
                print_dashed_line()

        elif user_option == "3":
            # user wants to exit program
            print_dashed_line()
            print("Good Bye!")
            print_dashed_line()
            # exit without errors
            exit(0)

        # if user does not select the right option
        else:
            print_dashed_line()
            print("<-- Wrong Option -->")
            print_dashed_line()

    # if the user does not enter integer data for bitrate
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please Enter Integer Data for Bitrate\n")



# function to display options to user
def display_options():
    # main welcome "screen" + display options to user
    print("\n<-- YouTube Video Downloader and Converter -->\n")
    print("Option [1]: Download Audio")
    print("Option [2]: Download Video")
    print("Option [x]: Exit")
    print_dashed_line()


audio_downloader()
