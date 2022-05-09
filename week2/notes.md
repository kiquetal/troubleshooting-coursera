#### Notes
#### Slowness

    Use cache
    Check about memory leaks

#### Monitoring tools

  ab -n 500 site.example.com
  nice 
  renice for apps running
  pidof <app>
  ps ax   
  for pid in $(pidof ffmpeg); do renice 19 $pid; done
   locate static/001.webm
   killall -STOP ffmpeg

