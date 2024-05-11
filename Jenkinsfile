pipeline {
    agent any

    environment {
        PYTHON_VERSION = 'latest'
        ALLURE_VERSION = 'latest'
    }

    stages {
        stage('Clone Repo'){
            steps{
                git "https://github.com/isFrost/toolshop_test_automation.git"
            }
        }
        stage('Setup') {
            steps {
                // install python and dependencies
                sh "pyenv install -s $PYTHON_VERSION"
                sh "pyenv global $PYTHON_VERSION"
                sh "pip install-r requirements.txt"

                // download and setup allure
                sh "latest_allure_version=$(curl -s https://api.github.com/repos/allure-framework/allure2/releases/latest | grep -oP '\"tag_name\": \"\K(.*)(?=\")') && \
                    wget -O allure-commandline.tar.gz https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/$latest_allure_version/allure-commandline-$latest_allure_version.tar.gz && \
                    tar -zxvf allure-commandline.tar.gz -C $JENKINS_HOME/tools/ && \
                    ln -s $JENKINS_HOME/tools/allure-$latest_allure_version/bin/allure /usr/bin/allure"
            }
        }

        stage('Test') {
            steps {
                sh "pytest /tests"
            }
        }

        stage('Report') {
            steps {
                // generate Allure report
                sh "allure generate allure-results -o allure-report"
                // publish Allure report
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}