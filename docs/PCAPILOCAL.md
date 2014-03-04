### PCAPI Local Wifi

The following outlines the steps need to run the pcapi-local wifi test.

### Prerequisite Setup

* The testing tool uses the Microsoft Windows [Wireless Hosted Network](http://msdn.microsoft.com/en-us/library/dd815243%28VS.85%29.aspx) feature availble only on Windows 7 and newer.
* A supported [wifi device and driver](https://virtualrouter.codeplex.com/wikipage?title=Supported%20Devices&referringTitle=Documentation).
* Administrator Access.
* [Open port 80](http://windows.microsoft.com/en-us/windows/open-port-windows-firewall#1TC=windows-7) on firewall.
* python version 2.7.x [installed](http://www.python.org/download/releases/2.7.6/) and correctly [configured](http://docs.python.org/2/using/windows.html#configuring-python).
* [easy_install](https://pypi.python.org/pypi/setuptools#windows)

### Set Up

* Install Virtualenv

```
C:\easy_install virtualenv
```

* Download wifi-test [zip file](http://fieldtripgb.edina.ac.uk/pcapilocal/wifi-test.zip) and `Extract All`.
* In windows explorer navigate to the mounted location and double click on `install` batch file.
* Right click on `run` batch file and choose `Run as administrator`.
* Navigate to Control Panel -> Network and Internet -> Network and Connection and ensure there is a Wireless Network Connection with an SSID of `ft-test` and Media State `Enabled`.
*

### Install Client

* Ensure Andoird device allows installs from unauthorised sources.
* Open http://fieldtripgb.edina.ac.uk/releases/bierton/FieldTripGB-debug.apk with the Android browser and install app.
* Switch to ft-test in your wifi settings (password qwertyui)

### Run Test

* Open Fieldtrip GB (Bierton).
* Click on the `Test Virtual Wifi` button on the home page.
* A Success GET and POST will be reported if successful.
* A text file POSTed from the client named post.txt is created in wifi-test/pcapi/

### Clean Up

* Disable Virtual Wifi Adapter created above.
* Disable firewall rule created above.