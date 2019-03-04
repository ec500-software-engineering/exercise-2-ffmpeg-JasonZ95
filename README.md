# python-ci-template
## Prerequisites
To run the project, you need to install the FFMPEG package first. Here is the [tutorial](https://www.wikihow.com/Install-FFmpeg-on-Windows) for the installation.


By running the main.py promgram, it will convert the videos in current repository into two required qualities: 480p with 1Mbps and 720p with 3Mbps. 


The converstion will be done in seperate process, and the amount of cores that current computer has depends on how many process will work at the same time.
## Method applied for multiprocess
### subprocess:
Used to excecute bash command in python.
### multiprocessing:
Open processes for video conversion.
```python
p = multiprocessing.Pool(processes=multiprocessing.cpu_count()-2) //python
```
I intend to limit the number of process, but since the virtual machine has only two cores, I just set the number as default, which is the num of cpu cores.
## Result  
