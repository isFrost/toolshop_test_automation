# get basic os image
FROM ubuntu:22.04

# Switch to root user to install necessary components
USER root

# Install python, wget, gpg, git
RUN apt update
RUN apt-get install -y python3 python3-venv pip virtualenv
RUN apt install -y wget
RUN apt install -y gnupg2
RUN apt install -y git

# Install Java (required for jenkins)
RUN apt update && apt install -y openjdk-11-jdk

# Install Jenkins
RUN wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
RUN echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
    https://pkg.jenkins.io/debian-stable binary/ | tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null
RUN apt update
RUN apt install -y jenkins

# Detect architecture and install appropriate Chrome
RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        wget -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb; \
    elif [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then \
        wget -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_arm64.deb; \
    else \
        echo "Unsupported architecture: $ARCH" && exit 1; \
    fi && \
    dpkg -i /tmp/google-chrome.deb || apt install -f -y

# Install Firefox
RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "arm64" ]; then \
        apt install -y firefox:arm64; \
    else \
        apt install -y firefox; \
    fi

# Expose Jenkins port
EXPOSE 8080

# Start Jenkins service
CMD ["jenkins"]