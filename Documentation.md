# Variable Boot Drive Docs

## Turning off the Web Interfaces

Since daemons like running, turning these on and off might get tricky.
It's going to be easier to just give the user a 404 error when they try to access
the web interface when it's supposed to be "offline"

settings.yaml -> web_if -> client -> active: True/False

gets checked with every request, takes milliseconds to check and should have
no noticeable impact on performance. 
