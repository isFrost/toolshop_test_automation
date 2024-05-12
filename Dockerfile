FROM jenkins/jenkins:lts

USER root

# Install python
RUN apt-get update
RUN apt-get install -y python3 python3-venv pip virtualenv
# Install custom plugins
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:2.31.1 build-timeout:1.32 github-branch-source:1789.v5b_0c0cea_18c3

USER jenkins