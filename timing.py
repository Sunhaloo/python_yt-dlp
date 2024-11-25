import time
import os

# get size function
def get_size(file_path: str):
    file_size = os.path.getsize(file_path)
    print(file_size)


# os.stat().st_size
def os_stat(file_path: str):
    file_size = os.stat(file_path).st_size
    print(file_size)


def main():
    start_time = 0
    end_time = 0
    path = "/home/azman/GitHub/python_yt-dlp/test.py"

    for i in range(10):
        start_time = time.perf_counter()
        # get_size(path)
        os_stat(path)
        end_time = time.perf_counter()

    time_taken = end_time = start_time
    # output the result
    print(f"Time Taken: {time_taken / 5}")


if __name__ == '__main__':
    main()

