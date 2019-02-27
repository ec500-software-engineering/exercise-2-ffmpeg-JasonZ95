from pytest import approx
import main
import json
import subprocess
import ffprobe


def ffprobe(file_name) -> dict:
    """ get media metadata """

    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    file_name])
    return json.loads(meta)


def test():
    fnin = 'test.mp4'
    fnout_720 = 'test_720.mp4'
    fnout_480 = 'test_480.mp4'
    orig_meta = ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    main.main()

    meta_720 = ffprobe(fnout_720)
    duration_720 = float(meta_720['streams'][0]['duration'])

    meta_480 = ffprobe(fnout_480)
    duration_480 = float(meta_480['streams'][0]['duration'])

    try:
        assert orig_duration == approx(duration_720)
        assert orig_duration == approx(duration_480)
    except:
        print("test not passed")

    print("test passed")


if __name__ == "__main__":
    test()