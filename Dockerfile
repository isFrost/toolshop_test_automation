# Get Jenkins image
FROM jenkins/jenkins:lts

# Switch to root user to install necessary components
USER root

# Install python
RUN apt-get update
RUN apt-get install -y python3 python3-venv pip virtualenv

# Install custom plugins
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:2.31.1 build-timeout:1.32 github-branch-source:1789.v5b_0c0cea_18c3

# Install wget
RUN apt-get install -y wget

# Set non-interactive mode for installation
ENV DEBIAN_FRONTEND=noninteractive

# Detect architecture and install appropriate Chrome
RUN ARCH=$(uname -m) && \
    if [ $ARCH = "x86_64" ]; then \
        wget -O /tmp/google-chrome.deb ttps://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb; \
    elif [ $ARCH = "aarch64"] || [ $ARCH = "arm64"]; then \
        wget -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_arm64.deb; \
    else \
        echo "Unsupported architecture: $ARCH" && exit 1; \
    fi && \
    sudo dpkg -i /tmp/google-chrome.deb || sudo apt-get install -f -y

# Detect architecture and install appropriate Firefox
RUN ARCH=$(uname -m) && \
    if [ $ARCH = "x86_64" ]; then \
        wget -O /tmp/firefox.tar.bz2 https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US; \
    elif [ $ARCH = "aarch64" ]; then \
        wget -O /tmp/firefox.tar.bz2 https://download.mozilla.org/?product=firefox-latest&os=linux-aarch64&lang=en-US; \
    else \
        echo "Unsupported architecture: $ARCH" && exit 1; \
    fi && \
    tar -xjf /tmp/firefox.tar.bz2 -C /opt/ && \
    ln -sf /opt/firefox/firefox /usr/bin/firefox

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Switch to Jenkins
USER jenkins