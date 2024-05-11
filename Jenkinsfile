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
                sh "python3 -m venv .venv"
                sh ". .venv/bin/activate"
                sh ".venv/bin/python3 -m pip install -r requirements.txt"
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh "ls"
                        sh ".venv/bin/python3 -m pytest tests alluredir=allure-results"
                    }
                    catch (Exception e) {
                        echo "Exception occurred " + e.toString()
                        sh "exit 0"
                    }
                }
                sh "pytest /tests"
            }
            post {
                always {
                    echo "Finished"
                }
                success {
                    echo "Success"
                }
                unstable {
                    echo "Unstable"
                }
                failure {
                    echo "Failed"
                }
            }
        }

        stage('Report') {
            steps {
                // generate Allure report
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
    post {
        always {
            cleanWs()
        }
    }
}