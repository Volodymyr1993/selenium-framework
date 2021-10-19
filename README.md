#Project 'social-supermarket-tests'

---------------

## Requirements:

Python 3.7+

---------------

Step-by-step installation on localhost:
```
cd ~
mkdir social-supermarket-tests
mkdir social-supermarket-tests/git
mkdir social-supermarket-tests/bin
cd social-supermarket-tests
```
Create virnual venv
- ```python3.7 -m venv venv```
- ```source venv/bin/activate```

Clone Git
- ```git clone https://github.com/Social-Supermarket/social-supermarket-tests.git```

Install packages
- ```pip install selenium```
- ```pip install pytest```

Setup chromedriver version for linux.
Chromedriver version should be the same as you local Google Chrome

```
wget https://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip && unzip chromedriver_linux64.zi
mv chromedriver_linux64.zip /usr/local/bin
```

Setup Firefox driver version for linux.
visit https://github.com/mozilla/geckodriver/releases

```
1) download the latest version of "geckodriver-vX.XX.X-linux64.tar.gz"
2) unarchive the tarball (tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz)
3) give executable permissions to geckodriver (chmod +x geckodriver)
4) mv geckodriver /usr/local/bin
```

###Running tests:

-----
Use pytest framework to run tests.

To run all tests:

- Switch to project root directory

- Run $ pytest
Run certain test suites: $ pytest <path_to_test_module>

Run certain cases: $ pytest <path_to_test_module>::<test_case_name>

To get extra test summary info, use: $ pytest -rA