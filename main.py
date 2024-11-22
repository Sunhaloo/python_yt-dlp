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
    print("\nOption [1]: Download Audio")
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
            print("\nOutput Directory / Folder Already Exists!\n")
        # if the directory / folder does not exists
        else:
            print("\nCreating Output Folder\n")
            # create the directory / folder
            os.mkdir(os.path.expanduser("~/Desktop/downloaded_audio"))

    elif user_option == "2":
        # meaning user wants to download audio
        dir_path = os.path.expanduser("~/Desktop/downloaded_video")

        # check if the path exists
        if os.path.exists(dir_path):
            print("\nOutput Directory / Folder Already Exists!\n")
        # if the directory / folder does not exists
        else:
            print("\nCreating Output Folder\n")
            # create the directory / folder
            os.mkdir(os.path.expanduser("~/Desktop/downloaded_video"))



# function to download the audio itself
# WARNING: This is a test only
def audio_downloader():
    pass


# function to download the video itself
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
        print("\nGood Bye!\n")
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
