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

    print("\nCreating Output Folder\n")
    path = create_folder()
    file_name = os.path.join(path + "/%(title)s.%(ext)s")

    yt_audio_cmd = ["yt-dlp", user_url, "--format", "m4a", "-o", file_name]
    # run the command in shell
    subprocess.run(yt_audio_cmd)




if __name__ == '__main__':
    main()
