# Installation
It is assumed that you have already installed Python 3.6.

## Windows

There are two ways to install the project for Windows. The easy way is to use the `install.ps1` script, which handles all the program requirements. If you don't want to use this script, an alternative method is described in the [Without Script](#without-script) section.

### With Script

* Run the `install.ps1` script in a PowerShell terminal running as Administrator
* Run `pip install .`
* To check if everything installed correctly, check the [Testing](#testing) section.

### Without Script
NOTICE: If possible use precompiled packages (wheels) provided in the `windows_dependencies` directory to install project's dependencies. However the provided wheels are only suitable for Windows (64-bit architecture) with Python 3.6 (64-bit). 

* Download and install `GTK3+`. 
* Download and install `Bloomberg C++ SDK`:
    * extract the files from the installation archive (zip) from the `windows_dependencies` directory
    * create a new environment variable called `BLPAPI_ROOT` and set it to the path of the `/bin` directory inside the Bloomberg's directory (extracted from the `zip` achive)
    * add `/bin` directory to the `PATH` environment variable
* Install `blpapi` by running `pip install blpapi-3.9.1-cp36-cp36m-win_amd64.whl` in the `windows_dependencies` directory.
* Install `numpy` by running `pip install numpy-1.15.4+mkl-cp36-cp36m-win_amd64.whl` in the `windows_dependencies` directory.
* Install `scipy` by running `pip install scipy-1.1.0-cp36-cp36m-win_amd64.whl` in the `windows_dependencies` directory.
* Install `cvxopt` by running `pip install cvxopt-1.2.2-cp36-cp36m-win_amd64.whl` in the `windows_dependencies` directory.
* Install `statsmodels` by running `pip install statsmodels-0.9.0-cp36-cp36m-win_amd64.whl` in the `windows_dependencies` directory.
* Install `TA Lib` (optional):
    * extract TA Lib SDK archive (zip) to `C:\ta-lib` (unfortunately this is the fixed path)
    * run `pip install TA_Lib-0.4.17-cp36-cp36m-win_amd64.whl` in the `windows_dependencies` directory.
* Install `Haver` (optional) by running `Haver-1.1.0-cp36-cp36m-win_amd64.whl` in the `windows_dependencies` directory.
* Install other requirements using `pip`. Run `pip install -r requirements.txt` in the main directory of the `QuantFin Lib`.
* Install Interactive Brokers platform (optional):
    * install `TWS` by running `TWS API Install 973.06.msi` in the `windows_dependencies`
    * got to `C:\TWS_API\source\pythonclient` and run `python setup.py install`

# Configuration
## Starting directory
Starting directory is used to turn relative paths into absolute paths. In many places you'll be required to specify
a path which should be relative to the starting directory. To set up starting directory one needs to either:
- call `set_starting_dir_abs_path(abs_path_to_starting_directory)`
- or set `QF_STARTING_DIRECTORY` environment variable.

## Settings files
Many components from `qf-lib` require the `Settings` object as a dependency. To create it one needs to put in their Python code:
```python
from qf_lib.settings import Settings


settings_path = ...
secret_settings_path = ...
settings = Settings(settings_path, secret_settings_path)
```  
where `settings_path` is an absolute path of your file containing settings (JSON, described later) used
by the application and the `secret_settings_path` which is complementary to the settings file but contains secret data
(e.g. passwords) and thus mustn't be added to the CVS. When `Settings` object is created, it:
- loads settings defined in the `settings.json` file
- loads settings defined in the `secret_settings.json` file (if the file exists)
- loads settings defined in the `QUANTFIN_SECRET` environment variable (if the `secret_settings.json` file doesn't exist)
- merges both loaded sets of settings together.

Sample content of the `settings.json`:
```json
{
  "some_setting": "value of that setting",
  "another_setting": "value of another setting",
  "some_connection_settings": {
    "username": "jan.kowalski"
  }
}
```

Sample content of the `secret_settings.json`:
```json
{
  "some_connection_settings": {
    "password": "i like donuts"
  }
}
```

## QF-Lib used settings
You may define your own settings and later on have them loaded into `Settings` object. However there are some, which are
required for some QF-Lib components to work correctly.

NOTICE: all paths used in the settings should be relative to the starting directory. (which can be set either by using `set_starting_dir_abs_path(path)` function or by setting
`QF_STARTING_DIRECTORY` environment variable)

Below you'll find a list of those.

#### company_name and logo_path
`settings.json`:
```json
    "company_name": "Jacek Witkowski PDK",
    "logo_path": "path/to/logo.jpg"
```
Used by components producing tearsheets (in a form of PDFs). The company name and a logo is put in the header of those
tearsheets.

#### document_css_directory (optional)
`settings.json`:
```json
    "document_css_directory": "input/elements_css"
```
Setting used by the `PDFExporter` component to style the elements put in PDFs (e.g. tables, paragraphs, etc.).
If `document_css_directory` is not specified then the default style will be applied.

#### bloomberg
`settings.json`:
```json
  "bloomberg": {
    "host": "localhost",
    "port": 8194
  }
```

Used by the `BloombergDataProvider`. To have this component running, first you need to have a Bloomberg subscription.
Then you need to have the BLPAPI running somewhere. Then you need to specify where the API is running by specifying its
host and port.
 
#### email_templates_directory
`settings.json`:
```json
  "email_templates_directory": "input/email_templates"
```

Setting used by the `EmailPublisher`. Email templates are HTML templates with placeholders (e.g. {{user.name}}).

#### output_directory
`settings.json`:
```json
  "output_directory": "output"
```
A relative path to the directory into which different components will put their output (e.g. generated tearsheets).

#### smtp
`settings.json`:
```json
  "smtp": {
    "host": "smtp.server.pl",
    "port": 587,
    "domain": "SOME_DOMAIN",
    "tls": true,
    "sender": "sample_user@some.domain.pl"
  }
```

`secret_settings.json`:
```json
  "smtp": {
    "username": "sample_user",
    "password": "VeryStrong P4ssw0rd with s0me Polish special characters (to confuse the hacker)"
  }
```
SMTP settings used by the `EmailPublisher`.

#### haver_path
`settings.json`:
```json
  "haver_path": "C:/absolute/path-to-haver-data"
```
Absolute path to the Haver data (see: http://www.haver.com/).


#### Links
* `windows_dependencies` directory
* [GTK3+](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2017-11-15/gtk3-runtime-3.22.26-2017-11-15-ts-win64.exe)
* [Bloomberg C++ SDK](https://software.tech.bloomberg/BLPAPI-Stable-Generic/blpapi_cpp_3.8.18.1-windows.zip)
* [Bloomberg Python](https://bintray.com/bloomberg/BLPAPI-Experimental-pip/blpapi_python/3.9.1#files/simple/blpapi)
* [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
* [Haver](http://www.haver.com/python/haver/)
* [cvxopt](http://cvxopt.org/install/index.html#windows)
* [TA Lib](http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-msvc.zip)

# Testing
After the installation process you may test if everything was setup fine. In order to do so you need to download
the `QuantFin Lib` from git and then:
1. Add path of `QuantFin Lib` to the `PYTHONPATH` environment variable (create it if it doesn't exist).
2. Go to the `qf_lib_tests` directory.
3. Run `python run_unit_tests.py` script. There should be no skipped tests and no errors if all the requirements were installed
correctly.
4. Run `python run_integration_tests.py` script. It's better if you have established Bloomberg, Haver and Quandl connections.
Otherwise some tests might be skipped. However there should be no errors.
