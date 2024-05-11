pipeline {
    agent any

    environment {
        PYTHON_VERSION = 'latest'
        ALLURE_VERSION = 'latest'
    }

    stages {
        stage('Clone Repo'){
            steps{
                git branch: 'main', url: 'https://github.com/isFrost/toolshop_test_automation.git'
            }
        }
        stage('Setup') {
            steps {
                // install python and dependencies
                sh "pyenv install -s $PYTHON_VERSION"
                sh "pyenv global $PYTHON_VERSION"
                sh "pip install -r requirements.txt"
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
            }
        }
    }
}