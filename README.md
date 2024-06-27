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
- [Running Tests from command line](#Running-Tests-from-command-line)
- [Notes](#Notes)
- [Contributing](#Contributing)
- [License](#License)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker Desktop

To run outside docker container:
- Python 3.x
- Pip

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

### Set up a Jenkins job and configure it to use the repository.

Once the docker container with the project is up and running open web browser and open this link: [localhost:8080/](localhost:8080/)

Jenkins will ask for Admin password. To get the password run docker command:

```commandline
docker container logs toolshop
```
1. Copy the password, enter it into administrator password field and click Continue button.
2. At Customize Jenkins select option Install Selected plugins. 
3. Wait until Jenkins completes installation of plugins. 
4. At Create First Admin User screen populate Username, Password, Confirm Password, Full Name, E-mail address and click Save and Continue. 
5. At Instance Configuration click Save and Finish. 
6. At confirmation screen (Jenkins is ready!) click Start using Jenkins button.

### Install Allure Plugin (required to run reports)
1. At dashboard screen click Manage Jenkins.
2. At Manage Jenkins screen click Plugins button. 
3. At Plugins page click on Available plugins list. Use Search input to find Allure plugin.
4. Check flag against Allure plugin and click Install button.
5. Click on Installed plugins and confirm Allure plugin is in the list with Enabled flag.

### Install Allure Command Line (required to run reports)
1. Open Manage Jenkins page. 
2. Click on Tools item. 
3. At Tools screen under Allure Commandline installations click Add Allure Commandline button.
4. Populate Name field.
5. Click Apply and Save buttons.

### Create new pipeline
1. Click New Item button.
2. Populate item name.
3. Select Pipeline item and click OK 
4. At configuration screen in Pipeline section set Definition option to Pipeline script from SCM. 
5. Set SCM option to Git. 
6. Populate Repository URL filed: https://github.com/isFrost/toolshop_test_automation.git
7. In Branch Specifier field enter */main. 
8. Click Save button. 
9. Click Build Now to build the pipeline.

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

## Running Tests from command line

To run the test from command line:

1) Make sure python and pip are installed in the system.
```commandline
python3 --version
```
```commandline
pip3 --version
```
2. Install dependencies from requirements.txt file. Navigate to project folder and enter command:
```commandline
pip install -r requirements.txt
```
3. create and activate virtual Python environment for your project. For example, the commands to create and activate a venv
```commandline
python -m venv .venv
```
```
source .venv/bin/activate
```
3. To run the test enter command:
```commandline
python3 -m pytest tests/ --alluredir reports
```
4. To open generate allure report enter:
```commandline
allure serve reports
```
*Note: You many need to install Allure in venv to open generated reports in browser. Below is the example how to do it:*
```commandline
# Download and set up Allure command-line tool

VERSION=2.13.9  # Replace with the latest version

wget https://github.com/allure-framework/allure2/releases/download/${VERSION}/allure-${VERSION}.tgz

tar -zxvf allure-${VERSION}.tgz -C venv/

mv venv/allure-${VERSION} venv/allure

# Add Allure to PATH
echo 'export PATH="$VIRTUAL_ENV/allure/bin:$PATH"' >> venv/bin/activate

# Reload environment
source venv/bin/activate
```
*Also note that allure will require Java Runtime to be installed in the system*
## Notes
Although Dockerfile is composed to detect CPU architecture and use proper browser it looks like webdrivers curently do not support linux/aarch64 combination. Workaround is not yet added to this project.

## Contributing

This is a test project build to improve knowledge of python/selenium automation skills. No contribution is required.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

