FROM jenkins/jenkins:lts

USER root

# Install python
RUN apt-get update
RUN apt-get install -y python3 python3-venv pip virtualenv

# Install custom plugins
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:2.31.1 build-timeout:1.32 github-branch-source:1789.v5b_0c0cea_18c3

# Install wget
RUN apt-get install -y wget

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
RUN chmod -x /usr/bin/google-chrome

# Install Firefox
RUN wget https://raw.githubusercontent.com/mozilla/sumo-kb/main/install-firefox-linux/firefox.desktop -P /usr/local/share/applications

USER jenkins