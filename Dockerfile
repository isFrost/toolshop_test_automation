FROM jenkins/jenkins:lts

USER root

# Install python
RUN apt-get update
RUN apt-get install -y python3 python3-venv pip virtualenv

# Install custom plugins
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:2.31.1 build-timeout:1.32 github-branch-source:1789.v5b_0c0cea_18c3

# Install Chrome
RUN apt-get install -y wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN chmod -x /usr/bin/google-chrome

# Intall Firefox
RUN wget https://raw.githubusercontent.com/mozilla/sumo-kb/main/install-firefox-linux/firefox.desktop -P /usr/local/share/applications

# Install Chrome Driver
RUN wget -q -O chromedriver-linux64.zip https://bit.ly/chromedriver-linux64-121-0-6167-85 && \
    unzip -j chromedriver-linux64.zip chromedriver-linux64/chromedriver && \
    rm chromedriver-linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chown root:root /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver

# Install Gecko Driver for Firefox
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -zxvf geckodriver-v0.30.0-linux64.tar.gz && \
    rm geckodriver-v0.30.0-linux64.tar.gz && \
    mv geckodriver /usr/bin/geckodriver && \
    chown root:root /usr/bin/geckodriver && \
    chmod +x /usr/bin/geckodriver

USER jenkins