Since this is Python Application to Add Two Numbers, you will need to download and have Python setup in your local machine.

# Installing Python:

To install Python on your local machine, get a copy of the standard distribution of Python software from **[this link](https://www.python.org/downloads)** based on your operating system, hardware architecture and version of your local machine.

## Windows OS

To install Python on a Windows platform, you need to download the installer. A web-based installer, executable installer and embeddable zip files are available to install Python on Windows. Visit https://www.python.org/downloads/windows and download the installer based on your local machine's hardware architecture.

The web-based installer needs an active internet connection. So, you can also download the standalone executable installer. Visit https://www.python.org/downloads and click on the Download Python 3.10.6 button as shown below. (3.10.6 is the latest version as of this writing.)

This will download python-3.10.x.exe for 32/64 bit. For the 64 bit installer, go to https://www.python.org/downloads/windows and select the appropriate 64 bit installer, as shown below:

![](https://www.tutorialsteacher.com/Content/images/python/download-python-windows64.png)

Now, download the Windows x86-64 executable installer for 64-bit Windows and double click on it to start the python installation wizard as shown below:

![](https://www.tutorialsteacher.com/Content/images/python/install-wizard1.png)

Installation is a simple wizard-based process. As you can see in the above figure, the default installation folder will be C:\ Users\ {UserName}\ AppData\ Local\Programs\ Python\ Python37 for Python 3.7.0 64 bit. Check the Add Python 3.7 to PATH checkbox, so that you can execute python scripts from any path. You may choose the installation folder or feature by clicking on Customize installation. This will go to the next step of optional features, as shown below:

![](https://www.tutorialsteacher.com/Content/images/python/install-wizard2.png)

Click Next to continue.

![](https://www.tutorialsteacher.com/Content/images/python/install-wizard3.png)

After successful installation, you can check the Python installation by opening a command prompt and type:

`python --version` 

Or,

`python -V` and `press Enter` 

If Python installed successfully then it will display the installed version.


## Linux OS
Most of Linux distributions come with Python already installed. However, the Python 2.x version is incorporated in many of them. 

To check if Python 3.x is available, run the following command in the Linux terminal:

`$ which python3
`

If available, it will return the path to the Python3 executable as /usr/local/bin/python3.

To install Python on Ubuntu 18.04, Ubuntu 20.04 and above, execute the following commands:

`$ sudo apt-get update`

`$ sudo apt-get install python3.10 python3-pip`

After the installation, you can run Python 3.10 and pip3 commands.

For other Linux distributions use the corresponding package managers, such as YUM for Red Hat, aptitude for debian, DNF for Fedora, etc.

## Mac OS

You can install Python by downloading official installer from https://www.python.org/downloads/mac-osx page. Download the latest version of Python under the heading Python Releases for Mac OS X. Double click on the installer file to start the installation wizard.

On the installation wizard, click on Continue a few times until you're asked to agree to the software license agreement, click on Agree and finish the installation.