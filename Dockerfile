FROM jenkins/jenkins:lts

USER root

# Install custom plugins
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:2.31.1 build-timeout:1.32 github-branch-source:1789.v5b_0c0cea_18c3

# Set environment variables
# ENV <ENV_VARIABLE_1> <VALUE>
# ENV <ENV_VARIABLE_2> <VALUE>

USER jenkins