# Tool Shop Test Automation Pet Project

This repository contains a Selenium-based test framework for automated testing of a website https://practicesoftwaretesting.com/#/. 

The framework is built with Python and uses Docker to manage the test environment. Jenkins is used to build and execute the test pipeline.

The purpose of the project is to improve personal test automation skills.

Auto tests are based on the manual tests listed in the following spreadsheet: [Link](https://docs.google.com/spreadsheets/d/1ktdpGH0tEea1sl_GIplo943XJddfm8ibyrXEPgCS47s/edit?usp=sharing)

## Table of Contents

- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Continuous Integration](#Continuous-Integration)
- [Project Structure](#Project-Structure)
- [Running Tests from command line]
- [Notes]
- [Contributing]
- [License]

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker Desktop

## Installation

1. Clone the repository:
```commandline
git clone https://github.com/isFrost/toolshop_test_automation.git
```
2. Navigate to the project's folder:
```commandline
cd toolshop_test_automation
```
3. Build the Docker container:
```commandline
docker build -t toolshop .
```
4. Run the container:
```commandline
docker container run -d -p 8080:8080 --name toolshop toolshop
```

## Continuous Integration
This project uses Jenkins for continuous integration. The Jenkins pipeline is defined in the Jenkinsfile.

Set up a Jenkins job and configure it to use the repository.

Once the docker container with the project is up and running open web browser and open this link: [localhost:8080/](localhost:8080/)

Jenkins will ask for Admin password. To get the password run docker command:

```commandline
docker container logs toolshop
```
Copy the password, enter it into administrator password field and click Continue button.
At Customize Jenkins select option Install Selected plugins.
Wait until Jenkins completes installation of plugins.
At Create First Admin User screen populate Username, Password, Confirm Password, Full Name, E-mail address and click Save and Continue.
At Instance Configuration click Save and Finish.
At confirmation screen (Jenkins is ready!) click Start using Jenkins button.

Install Allure Plugin (required to run reports)
At dashboard screen click Manage Jenkins.
At Manage Jenkins screen click Plugins button. 
At Plugins page click on Available plugins list. Use Search input to find Allure plugin.
Check flag against Allure plugin and click Install button.
Click on Installed plugins and confirm Allure plugin is in the list with Enabled flag.

Install Allure Command Line (required to run reports)
Open Manage Jenkins page. 
Click on Tools item. 
At Tools screen under Allure Commandline installations click Add Allure Commandline button.
Populate Name field.
Click Apply and Save buttons.

Create new pipeline:
Click New Item button.
Populate item name.
Select Pipeline item and click OK
At configuration screen in Pipeline section set Definition option to Pipeline script from SCM.
Set SCM option to Git.
Populate Repository URL filed: https://github.com/isFrost/toolshop_test_automation.git
In Branch Specifier field enter */main.
Click Save button.
Click Build Now to build the pipeline.


## Project Structure

```commandline
toolshop_test_automation/
├── Dockerfile
├── Jenkinsfile
├── README.md
├── requirements.txt
├── logs
│   └── __init__.py
├── pages
│   ├── __init__.py
│   ├── account_page.py
│   ├── base_page.py
│   ├── cart_address_page.py
│   ├── cart_page.py
│   ├── cart_payment_page.py
│   ├── cart_sign_in_page.py
│   ├── category_page.py
│   ├── contact_page.py
│   ├── favourites_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── profile_page.py
│   ├── register_page.py
│   ├── rental_page.py
│   └── rentals_page.py
├── test_data
│   ├── __init__.py
│   ├── base_url.json
│   ├── invalid_user_data.json
│   ├── registered_user.json
│   └── user.json
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_authentication.py
│   ├── test_cart_management.py
│   ├── test_favourite_list.py
│   ├── test_message_management.py
│   ├── test_order_management.py
│   ├── test_product_browsing.py
│   ├── test_product_filtering.py
│   ├── test_product_search.py
│   ├── test_product_sorting.py
│   └── test_rentals.py
├── utils
│   ├── __init__.py
│   ├── data_provider.py
│   ├── driver_manager.py
│   └── login_helper.py
└── venv
```



Run the Docker container:

sh
Copy code
docker-compose up
Execute the tests:

sh
Copy code
docker exec -it selenium-container pytest --html=reports/test_report.html
Continuous Integration
This project uses Jenkins for continuous integration. The Jenkins pipeline is defined in the Jenkinsfile.

Set up a Jenkins job and configure it to use the repository.

The Jenkinsfile includes stages for building the Docker image, running the tests, and generating the test report.

groovy
Copy code
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('selenium-test-framework')
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('selenium-test-framework').inside {
                        sh 'pytest --html=reports/test_report.html'
                    }
                }
            }
        }

        stage('Report') {
            steps {
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: 'reports', reportFiles: 'test_report.html', reportName: 'Test Report'])
            }
        }
    }
}
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

License

This project is licensed under the MIT License. See the LICENSE file for details.

