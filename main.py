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

    # evaluate user's option
    if user_option == "1":
        # user wants to only convert 1 YouTube video
        pass

    elif user_option == "2":
        # user wants to convert a list of URLs with text file
        '''
        WARNING:
            I don't really know how to do this correctly. Hence, here are some conditions:
                1. Text File **need** to have a name of 'yt_urls.txt'
                2. Text File **need** to be located at '~/Desktop'
        '''
        text_file = os.path.expanduser("~/Desktop/yt_urls.txt")

        # before we continue with anything... check if file 'yt_urls.txt' exists
        if os.path.isfile(text_file) and os.path.exists(text_file):
            print("Good")

        else:
            print_dashed_line()
            print("You have no 'yt_urls.txt' File!!!")
            print_dashed_line()





    elif user_option == "3":
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
    # user_option = input("Please Select an Option: ")
    audio_downloader()

    # call the function to evaluate the user's choice
    # evaluate_choice(user_option)



# source the main function
if __name__ == '__main__':
    main()
