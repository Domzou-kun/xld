![multiple_loader Logo](https://github.com/Domzou-kun/xld/blob/main/docs/icon/logo.png?raw=true)

<div align="center">
   
   <a href="">![PyPI](https://img.shields.io/pypi/v/multipleloader)</a>
   <a href="">![PyPI - Python Version](https://img.shields.io/pypi/pyversions/multipleloader)</a>
   <a href="">![PyPI - Format](https://img.shields.io/pypi/format/multipleloader)</a>
   <a href="">![PyPI - License](https://img.shields.io/pypi/l/multipleloader)</a>
   <a href="">[![Downloads](https://static.pepy.tech/personalized-badge/multipleloader?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/multipleloader)</a>
   <a href="">![GitHub issues](https://img.shields.io/github/issues/Domzou-kun/xld)</a>
   <br>
   <a href="">![GitHub followers](https://img.shields.io/github/followers/Domzou-kun?style=social)</a>
   <a href="">[![Twitter](https://badgen.net/badge/icon/tweet?icon=twitter&label)](https://twitter.com/intent/tweet?text="xld"%20is%20a%20recommended%20repository😊👍%0a&url=https://github.com/Domzou-kun/xld&hashtags=Github,Python)
   </a>


</div>

<div align="center">
   <br>
   
   # **the latest version of 1.0.2🎉**
   ## Changes in the new version of **1.0.2**
   **- Release. -**  
   <br>

</div>

---
# Multiple Loader
`multiple loader`(hereinafter referred to as EEV `xld`) is a python library. It is a library that reads the main data file extensions often used by data scientists for data analysis in a **"simpler"** and **"one-line"** format.

---

## Description of xld
`xld` is a python library that automatically loads files in a single line, without the need to specify with statements or modes. Just pass the file path and it will recognize the file extension and load it using the appropriate library.

---

## More about Multiple Loader(xld)
`xld` is a library that automatically recognizes file extensions and loads files.
The extensions supported by the `current version(1.0.1)` are the following extensions:

 - csv / tsv
 - json
 - npy / npz
 - json
 - pickle / pkl

More extensions will be supported in the future.

The supported libraries are as follows:

 - [csv (Standard Library)](https://docs.python.org/3/library/csv.html)
 - [json (Standard Library)](https://docs.python.org/3/library/json.html)
 - [numpy](https://numpy.org/doc/)
 - [pandas](https://pandas.pydata.org/docs/)
 - [pickle (Standard Library)](https://docs.python.org/3/library/pickle.html)
 - [joblib](https://joblib.readthedocs.io/en/stable/)



Standard features include the following,
 - Basic Usage
   ```Python
   import multipleloader as xld
   load_data = xld.load("test_file.csv")
   ```
   Simply import the library and pass the file path you wish to load.
   The actual loading screen will look like this:
   ![xld test gif 1](https://github.com/Domzou-kun/xld/blob/main/docs/gif/xld_test_gif_1.gif?raw=true)


   In addition, the following LIBRARIES are supported for the extensions.
   - csv / tsv
      - csv
      - numpy
      - pandas **(default)**
   - json
      - json **(default)**
      - pandas
   - pickle / pkl
      - pickle **(default)**
      - pandas
      - joblib
   - npy / npz
      - numpy **(default)**

   You can also specify a library if you wish to load data using a library other than the one configured by default.

   ```Python
   import multipleloader as xld
   load_data = xld.load("test_file.csv", lib="numpy") # Default is pandas
   ```
   In the sample code above, numpy is specified for library.
   When specifying library, numpy also supports spelling inconsistencies such as very commonly used abbreviations such as np.

## Optional arguments, etc
The list of arguments, etc. that can be used in `xld` is as follows.
```
import multipleloader as xld

loaded_data = xld(  # The results will always return with a type of List.
   
   filepath,      # Required argument
      ### List to be used in the target function.

   lib,
      ### Argument to set if you want to use the default library.
   
   encoding
      ### To specify the encoding.
)
```

---

## Getting Started
### Installing

### Latest xld via [PyPI](https://pypi.org/project/multipleloader/) (pip install)
![PyPI](https://img.shields.io/pypi/v/multipleloader)
[![Downloads](https://static.pepy.tech/badge/multipleloader/month)](https://pepy.tech/project/multipleloader)
```
pip install multipleloader
```

### Install by pip from github

```
pip install git+https://github.com/Domzou-kun/xld.git
```
or install via SSH
```
pip install git+git://github.com:Domzou-kun/xld.git
```

## Authors

Domzou

## link
 - The link to PyPI is here.  
    - [PyPI project link](https://pypi.org/project/multipleloader/)  

## Version history
If you want to know about past versions, please refer to [version history](https://github.com/Domzou-kun/xld/blob/main/docs/version_history.txt).

## LICENSE
xld has a MIT license, as found in the [LICENSE file](https://github.com/Domzou-kun/xld/blob/main/LICENSE).





