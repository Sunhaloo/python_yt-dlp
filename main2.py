import os
import subprocess

# function to display dashed lines
def print_dashed_line():
    print()
    # display the character '-' 50 times
    print('-'*50)
    print()


# function to display options to user
def display_options():
    print("\nYouTube Video Downloader and Converter\n")

    # display available options to user
    print("Option [1]: Download Audio")
    print("Option [2]: Download Video")
    print("Option [x]: Exit")

    print_dashed_line()


'''
We are going to write a function that will create a folder at
~/Desktop/
This folder which will either be called 'downloaded_audio' or 'downloaded_videos'
Well this folder will be the output folder for the '-o' flag
'''
def create_folder(user_option: str):
    # check for the user's option
    if user_option == "1":
        # meaning user wants to download audio
        dir_path = os.path.expanduser("~/Desktop/downloaded_audio")

        # check if the path exists
        if os.path.exists(dir_path):
            print_dashed_line()
            print("Output Directory / Folder Already Exists!")
            print_dashed_line()

        # if the directory / folder does not exists
        else:
            print_dashed_line()
            print("Creating Output Folder")
            print_dashed_line()
            # create the directory / folder
            os.mkdir(os.path.expanduser("~/Desktop/downloaded_audio"))

    elif user_option == "2":
        # meaning user wants to download audio
        dir_path = os.path.expanduser("~/Desktop/downloaded_video")

        # check if the path exists
        if os.path.exists(dir_path):
            print_dashed_line()
            print("Output Directory / Folder Already Exists!")
            print_dashed_line()

        # if the directory / folder does not exists
        else:
            print_dashed_line()
            print("Creating Output Folder")
            print_dashed_line()
            # create the directory / folder
            os.mkdir(os.path.expanduser("~/Desktop/downloaded_video"))


# function to check if text file containing URLs actually contains something
# NOTE: this is how I would do it!
def check_file_size_open_file(file_path: str):
    # exception handling
    try:
        # open the file in read mode
        with open(file_path, 'r') as txt_file:
            # read the first line of the text file
            first_line = txt_file.readlines(1)

            # output appropriate message based on contents of text file
            if not first_line:
                print_dashed_line()
                print("The Text File Does NOT Contain Any URLs... Exiting!!!")
                print_dashed_line()

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


# INFO: This is the better version for checking the file size
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
            print("The Text File Does NOT Contains Any URLs... Exiting!!!")
            print_dashed_line()

            # exit the program
            exit()

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


# function to convert `.m4a` files to `.mp3`
def convert_to_mp3(directory_path: str, bitrate: str):
    # display the formats that we can convert to
    print_dashed_line()
    print("Select the Output Type")
    print_dashed_line()

    print("Option [1]: MP3 Format")
    print("Option [2]: WAV Format")

    # prompt the user to enter output format
    user_format = input("Please Select Output File Format: ")
    print_dashed_line()

    # select the appropriate file format and code for ffmpeg command below
    if user_format == "1":
        # user wants to user to convert to mp3
        file_format = "mp3"
        codec = "libmp3lame"

    elif user_format == "2":
        # user wants to user to convert to wav
        file_format = "wav"
        codec = "pcm_s16le"
    
    # if user does not select something appropriate
    else:
        print_dashed_line()
        print('Wrong Option')
        print_dashed_line()

    # change from current working directory to where we downloaded the songs
    os.chdir(directory_path)
    # iterate through the whole directory / folder
    for song in os.listdir(directory_path):
        # get each song's name
        input_song = song
        # find the name of the song without extension ( ==> NO `.m4a` )
        output_song = os.path.splitext(input_song)[0]

        # arguments to pass through ffmpeg
        ffmpeg_cmd = [
            "ffmpeg", 
            "-i", input_song, 
            "-vn", 
            "-acodec", "libmp3lame", 
            "-ab", bitrate, 
            "-ar", "44100", 
            "-f", "mp3",
            "-y",
            output_song
            ]

        # run command from Python
        subprocess.run(ffmpeg_cmd)
        # clean the `.m4a` file
        os.remove(input_song)



# function to convert `.m4a` files to `.mp3`
def convert_to_mp32(directory_path: str):
    # display the formats that we can convert to
    print_dashed_line()
    print("Select the Output Type")
    print_dashed_line()

    print("Option [1]: MP3 Format")
    print("Option [2]: WAV Format")

    # prompt the user to enter output format
    user_format = input("Please Select Output File Format: ")
    # prompt the user to enter the bitrate
    user_bitrate = input("Please Enter Bitrate: ")
    bitrate = user_bitrate + "k"
    print_dashed_line()

    # select the appropriate file format and code for ffmpeg command below
    if user_format == "1":
        # user wants to user to convert to mp3
        file_format = "mp3"
        codec = "libmp3lame"

    elif user_format == "2":
        # user wants to user to convert to wav
        file_format = "wav"
        codec = "pcm_s16le"
    
    # if user does not select something appropriate
    else:
        print_dashed_line()
        print('Wrong Option')
        print_dashed_line()

    # change from current working directory to where we downloaded the songs
    os.chdir(directory_path)
    # iterate through the whole directory / folder
    for song in os.listdir(directory_path):
        # get each song's name
        input_song = song
        # find the name of the song without extension ( ==> NO `.m4a` )
        output_song = os.path.splitext(input_song)[0]

        # arguments to pass through ffmpeg
        ffmpeg_cmd = [
            "ffmpeg", 
            "-i", input_song, 
            "-vn", 
            "-acodec", "libmp3lame", 
            "-ab", bitrate, 
            "-ar", "44100", 
            "-f", "mp3",
            "-y",
            output_song
            ]

        # run command from Python
        subprocess.run(ffmpeg_cmd)
        # clean the `.m4a` file
        os.remove(input_song)


# function to allow the user to convert YouTube videos to audio
# NOTE: for now the downloader will be very simple
def audio_downloader():
    print("==> Audio Converter Selected\n")

    # display options to the user
    print("Option [1]: Enter Single YouTube Video")
    print("Option [2]: Use List of URLs from a Text File")
    print("Option [3]: Exit")
    print_dashed_line()

    # ask the user to enter an option
    user_option = input("Please Select an Option: ")

    print_dashed_line()

    # evaluate user's option
    if user_option == "1":
        # user wants to only convert 1 YouTube video
        pass

    elif user_option == "2":

        print("Converting URLs from Text File\n")
        # user wants to convert a list of URLs with text file
        '''
        WARNING:
            I don't really know how to do this correctly. Hence, here are some conditions:
                1. Text File **need** to have a name of 'yt_urls.txt'
                2. Text File **need** to be located at '~/Desktop'
        '''
        # directory and output format for downloaded songs
        output_path = os.path.expanduser("~/Desktop/downloaded_audio")
        output_file_name = os.path.join(os.path.expanduser("~/Desktop/downloaded_audio") + "/%(title)s.%(ext)s")
        # input file for the YouTube URLs
        text_file = os.path.expanduser("~/Desktop/yt_urls.txt")

        # before we continue with anything... check if file 'yt_urls.txt' exists
        if os.path.isfile(text_file) and os.path.exists(text_file):
            # check for contents of file
            check_file_size(text_file)

            # everything is good ==> file present and size of file is greater than 0
            # ==> start the downloading process --> with subprocess module
            # arguments to pass through yt-dlp
            yt_dlp_cmd = [
                    "yt-dlp",
                    "-a",
                    text_file,
                    "--format",
                    "m4a",
                    "-o",
                    output_file_name
                ]

            # run the command from Python
            subprocess.run(yt_dlp_cmd)

        else:
            # user does not have 'yt_urls.txt' file present at `~/Desktop`
            print_dashed_line()
            print("You have no 'yt_urls.txt' File!!!")
            print_dashed_line()

        # start the convertion process

        print_dashed_line()
        print("Starting Conversion Process\n")
        user_bitrate = input("\nPlease Enter Birate: ")
        actual_birate = user_bitrate + "k"

        print_dashed_line()

        # call the function to convert from m4a to mp3
        # NOTE: I plan to add other conversion formats like `.wav`
        # cannot do that right now because I don't understand ffmpeg
        convert_to_mp3(output_path, actual_birate)

    elif user_option == "3":
        # user wants to exit
        print_dashed_line()
        print("Good Bye!")
        print_dashed_line()
        exit(0)

    # if user does not select something appropriate
    else:
        print_dashed_line()
        print('Wrong Option')
        print_dashed_line()


# function to download the YouTube video itself
# NOTE: for now the downloader will be very simple
def video_downloader():
    pass


# function to evaluate the user's choice
def evaluate_choice(user_choice: str):
    # conditions to evaluate based on user's choice
    if user_choice == "1":
        # create the output folder for audio
        create_folder(user_choice)
        # user wants to download in audio format
        audio_downloader()

    elif user_choice == "2":
        # create the output folder for video
        create_folder(user_choice)
        # user wants to download in video format
        video_downloader()

    elif user_choice == "x":
        # user is closing the program
        print_dashed_line()
        print("Good Bye!")
        print_dashed_line()
        exit(0)

    # if user does not select something appropriate
    else:
        print_dashed_line()
        print('Wrong Option')
        print_dashed_line()
        

# our main function
def main():
    # call function to display options to user
    display_options()

    # ask the user to enter his choice
    user_option = input("Please Select an Option: ")

    # call the function to evaluate the user's choice
    evaluate_choice(user_option)


# source the main function
if __name__ == '__main__':
    main()
