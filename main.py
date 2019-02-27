import subprocess
import multiprocessing
import os

input_path = os.listdir()
output_path = os.listdir()


def ffmpeg_720(video_name):
    bash_command = "ffmpeg -i " + input_path + "/" + video_name + \
                   ' -r 30 -b 2M -s hd720 ' + output_path + "/" + video_name[:-4] + "_720.mp4"
    subprocess.call(bash_command)
    print("720-size video conversion finished")


def ffmpeg_480(video_name):
    bash_command = "ffmpeg -i " + input_path + "/" + video_name + \
                   ' -r 30 -b 1M -s hd480 ' + output_path + "/" + video_name[:-4] + "_480.mp4"
    subprocess.call(bash_command)
    print("480-size video conversion finished")


def run():
    p = multiprocessing.Pool(processes=multiprocessing.cpu_count()-2)
    print("The current computer has " + str(multiprocessing.cpu_count()) + " cpu cores.")
    for video in os.listdir(input_path):
        if video.endswith(".mp4"):
            p.apply_async(ffmpeg_720, args=(video,))
            p.apply_async(ffmpeg_480, args=(video,))
    print("All processes start")
    p.close()
    p.join()


def main():
    run()


if __name__ == '__main__':
    main()
