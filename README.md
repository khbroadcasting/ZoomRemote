ZoomRemote
==========

Python HTTP Server to Remote Control Zoom Videoconferencing
-----------------------------------------------------------

**Unofficial and unaffiliated with Zoom**

Instructions
------------

### Windows

#### Installation

Download the portable, standalone executable [here.](https://github.com/khbroadcasting/ZoomRemote/raw/master/dist/ZoomRemote.exe)

#### Usage

Double-click on the file and follow the on-screen instructions!

On first time use, you may receive a warning from Windows Defender that looks like this:

![Windows Defender Warning Unsigned Executable](https://user-images.githubusercontent.com/4184939/30770764-d4c15b80-a045-11e7-9c17-d97176193b66.png)

Don't be alarmed, this just means I haven't signed the exe - it costs hundreds of dollars a year and is not worth it for me.  Just click "more info" and then "Run anyway".  If you don't have the option to run, [see here.](https://github.com/zumoshi/BrowserSelect/issues/25)

You will also likely receive a pop-up from Windows Firewall asking if you want to allow network access, please click "Allow Access" - you will need administrator rights.

These two warnings only appear on the first run - after that it's plain sailing.

### Linux

#### Dependencies

1. Python 3
2. pyautogui - get it with `pip install pyautogui`
3. pyautogui depends on `python3-tk` and `python3-dev` - install with apt oryum.

#### Installation

Download `webserver.py` or `webserver-cli.py` from the source above.

#### Usage

`python3 webserver.py`

If you are serving on port 80 - the default - you will need to elevate your privileges with sudo.  If you are running in a venv you might need to specify the python binary directly when using sudo:

`sudo bin/python webserver-cli.py`

If you can't elevate your privs, run on a port higher than 1024 by changing the PORT constant at the top of the source file. (This could be improved see contributing.)

### Mac

**NOT TESTED - FEEDBACK WELCOME**

Advanced
--------

This is a small python program that interacts with the Zoom client by sending it hotkeys.  At the moment, the Zoom client must be the active window, otherwise the hotkeys will not reach it.  This could be overcome by using an alternative library to `pyautogui` but has not been implemented yet (see contributing).

It has been designed to be very extensible and in fact is not limited to controlling just Zoom at all - any application with behaviour that can be controlled by hotkeys is a viable candidate!

The program comes pre-packaged with the necessary resources for controlling Zoom embedded in the main webserver.py file for convenience of distribution among non-technical users.  However these embedded files can be overridden by placing files in the same directory as the program.

For example by placing an alternate `index.html` in the same directory as the program, you can override the entire user-interface:

* Hotkeys can be defined by modifying or adding HTML form elements copying the style of res/index.html:
    * Each form has a submit button with `class="button"` (for style)
    * A form with `action="index.html"`
    * And a series of `type="hidden"` inputs with `value="<KEY>"` that when pressed together make up the hotkey.
* All the forms are wrapped in a `<div>` with `class="container"` for a very basic responsive layout (please improve! See contributing)

The server extends `SimpleHTTPRequestHandler` so can happily serve files and directories below and above it - I set it up this way for myself so that I could not only remote control Zoom while presenting but also access my notes at the same time on a seperate device.  For this reason and also because Python's `http.server` library also says so:

### THIS IS NOT INTENDED TO BE USED OVER THE PUBLIC INTERNET

The Tkinter GUI is only there to explain to non-technical users how to navigate to an IP address - if you know how to do that please use `webserver-cli.py` instead.  It's much less bloated.

Contributing
------------

Contributions are most welcome!  In particular, pull requests:
* Improving HTML/CSS Layout for a more intuitive responsive grid would be appreciated.  I would like to be able to have multiple buttons side-by-side on a row on mobile devices, to then add navigation functionality.
* Refactoring as a module to remove the embedded images and html from the main `webserver.py` to an imported library.
* Improving the hotkey system to allow multiple hotkeys to be specified to be fired _in sucession_ - for example `<alt>+q` _then_ `ENTER`.
* That allow the PORT to be specified as a command-line argument.
* That provide a better command-line interface and module interface.
* Anything else you can think of.
