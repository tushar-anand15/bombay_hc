# Setting up and creating the virtual environment

- ensure python3, pip and virtualenv are installed
- create a new virtual environment using:

```
virtualenv bhc_scraper
```

- activate the environment

```
source bhc_scraper/bin/activate
```

- install required dependencies

```
pip3 install -r requirements.txt
```

- install chromedriver

```
sudo apt-get install chromium-chromedriver
```

[link](https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/)
