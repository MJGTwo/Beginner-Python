# Setting up Python

Before we continue, we need Python on your computer. If you are really against this or you are having difficultly, I would recommend visiting the website [c9.io](c9.io), which is a website that allowed you to have a virtual work station on in your browser. Another for just Python is [here](https://repl.it/languages/python).

## Python for Mac

**If you have the latest OSX, you don't need to do this. OSX comes with Python in El Capitan.** However, it is useful to have Homebrew installed, so you might want to do that while you are here.

In order to get Python site up the correct way, you are going to need to add some tools to terminal. You can press ` cmd - space `  to use Spotlight and type in *terminal* and press `enter`.

Once you are in the terminal you will type `$ xcode-select --install` and press `enter`. This will install gcc. GCC states for *gnu c compiler*. We need this because Python is interpreted into into c++ and the c++ computer is included in gcc.

After this is done, we need to install *Homebrew*. *Homebrew* styles itself as the package manager that OSX is missing from not being Linux. To install Homebrew, type (or copy and paste) the following line into the terminal:

` $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" `

This will install Homebrew, but we have to edit the PATH variable. The path variable is a shortcut that the computer stores *paths* to programs that you call by name. The terminal doesn't know what `brew` is but when you add the path to PATH, it will.

To do this, type in  `cd` to get to your home directory, then type in `sudo nano ~/.profile` to access the file and then at the bottom of the file type in (or copy and paste) `export PATH=/usr/local/bin:/usr/local/sbin:$PATH`. To save your change press `Ctrl-X` followed by pressing `y` and `enter`.

Now the moment we have been waiting for: type `brew install python` into the terminal and press `enter`. This will install Python2.7. Give it a couple minutes.

You can now access the Python shell by typing `python` into terminal. You can exit by typing `quit()` at any point. In most actions in the terminal `Ctrl-C` usually works to exit as well, but Python maps that to exit functions that the Python shell is running. 



## Python for Windows

To install Python go to the website python.org and to their download page. Please selected the latest version of Python2.7, **not** Python3. The download page is linked [here](https://www.python.org/downloads/).

When the installer is done, it will have installed Python2.7 at `C:\Python27\`, which is where we want it, because we don't want it to conflict with other installs of Python in the future.

After Python is installed, we have to edit the PATH variable to be able to access Python easily in Command Prompt or Powershell. [Here is a link](http://www.computerhope.com/issues/ch000549.htm) to a resource on how to edit the PATH variable. Once you get to actually editing the PATH variable, add to the end of it `C:\Python27\;C:\Python27\Scripts\;`. Make sure to have semicolons between the previous item and this item that you have added. You can access the Python shell by opening Powershell or Command Prompt and typing `python`. You can exit by typing `quit()` at any point or `Ctrl-C`

## Moving forward

Congratulations, you have python now. If you ever need to install a Python module/library you can type into the terminal `pip install ~package name~` and it will install that for you. Pip is the *Package Installer for Python*. Let's move to the [IDE section](/ide.md).
