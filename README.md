# Selenium Python POM Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![PyTest](https://img.shields.io/badge/PyTest-Testing-orange)
![Automation](https://img.shields.io/badge/Testing-Automation-purple)
![POM](https://img.shields.io/badge/Framework-Page%20Object%20Model-red)

## 📌 Project Overview

This project is a **Selenium Web Automation Testing Framework** developed using **Python and PyTest**.

The framework follows the **Page Object Model (POM)** design pattern to create a clean, reusable, maintainable, and scalable automation structure.

The project demonstrates automated testing of the login functionality of the **SauceDemo** web application.

The framework includes:

- Page Object Model architecture
- Reusable Selenium methods
- Explicit waits
- PyTest fixtures
- Environment variable management
- Automated login test scenarios
- Failure screenshot capture
- HTML test report generation
- Custom report styling
- PyTest test execution

---

# 🎯 Project Objectives

The main objectives of this project are:

1. To build a structured Selenium automation framework using Python.
2. To implement the Page Object Model design pattern.
3. To separate test logic from page-specific implementation.
4. To create reusable automation methods.
5. To handle web elements using explicit waits.
6. To execute multiple test scenarios using PyTest.
7. To capture screenshots automatically when tests fail.
8. To generate an HTML execution report.
9. To maintain project dependencies using `requirements.txt`.
10. To follow basic industry-standard automation framework practices.

---

# 🛠️ Technologies & Tools

| Technology / Tool | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Web browser automation |
| PyTest | Test execution and framework |
| Page Object Model | Framework design pattern |
| python-dotenv | Environment variable management |
| pytest-html | HTML test reporting |
| CSS | Report customization |
| Chrome WebDriver | Browser automation |
| Git | Version control |
| GitHub | Source code management |

---

# 🏗️ Framework Architecture

The framework follows the **Page Object Model (POM)** architecture.

### High-Level Flow

```text
Test Case
    ↓
Login Page Object
    ↓
Base Page
    ↓
Selenium WebDriver
    ↓
Chrome Browser
    ↓
SauceDemo Application

📂 Project Structure

Selenium_POM_Framework/
│
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_login.py
│
├── screenshots/
│   └── Failure screenshots
│
├── reports/
│   └── report.html
│
├── css/
│   └── report.css
│
├── screenshot_utility.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt

📄 Framework Components
1. Base Page
File:
pages/base_page.py

The BasePage class contains reusable Selenium operations used across different page objects.
It provides methods for:
- Opening URLs
- Finding elements
- Clicking elements
- Entering text
- Retrieving element text
- Checking element visibility
- Explicit waiting
This reduces code duplication and makes the framework easier to maintain.

2. Login Page
File:
pages/login_page.py

It contains:
- Username locator
- Password locator
- Login button locator
- Error message locator
It also provides reusable actions such as:
load()
login()
get_error_message()
The test cases interact with the page through these methods instead of directly interacting with Selenium elements.

3. Test Cases
File:
tests/test_login.py
The test layer contains PyTest test cases for validating login functionality.
Example scenarios include:
- Valid login
- Invalid username
- Invalid password
- Empty username
- Empty password
The test layer focuses on what needs to be tested, while the Page Object layer handles how the application is interacted with.

🧪 Test Scenarios
The framework covers the following login scenarios:
| Test Scenario | Expected Result |
|---|---|
| Valid username and password | User successfully logs in |
| Invalid username | Appropriate error message displayed |
| Invalid password | Appropriate error message displayed |
| Empty username | Username validation message displayed |
| Empty password | Password validation message displayed |

⏱️ Explicit Waits
The framework uses Selenium's WebDriverWait with expected conditions.
Instead of using unnecessary fixed delays such as:
time.sleep(5)
the framework waits for the required element condition.
For example:
WebDriverWait(driver, timeout=10)
This improves test stability and reduces unnecessary waiting.

🔐 Configuration Management
The project uses a .env file to store environment-specific configuration such as:
BASE_URL
SAUCE_USERNAME
SAUCE_PASSWORD
The application configuration is loaded using:
python-dotenv
The .env file is excluded from Git version control through .gitignore.
This approach helps prevent configuration values from being hard-coded directly into test scripts.

📸 Failure Screenshot Capture
The framework includes automatic screenshot capture for failed test cases.
When a test fails, the screenshot utility captures the browser state and stores the screenshot inside:
screenshots/
Screenshot filenames contain the test name and timestamp, making failed executions easier to identify and investigate.
Example:
FAILED_test_login_20261005_203000.png
This provides useful evidence for debugging failed automation tests.

📊 HTML Test Reporting
The framework uses pytest-html to generate an HTML execution report.
The report includes:
- Test execution summary
- Passed tests
- Failed tests
- Test duration
- Test details
- Execution timestamp
The generated report is stored in:
reports/report.html
The report also uses custom CSS styling to improve readability.


🎨 Custom Report Styling
Custom CSS is maintained separately in:
css/report.css
The report is customized with a clean dark theme and improved title and summary presentation.
This demonstrates separation of:
- Test execution
- Reporting
- Report presentation

▶️ Installation
Prerequisites
Make sure the following are installed:
- Python 3.x
- Google Chrome
- Git
- Visual Studio Code

1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/Selenium_POM_Framework.git

2. Navigate to the Project
cd Selenium_POM_Framework

3. Install Dependencies
python -m pip install -r requirements.txt

▶️ Running the Tests
To execute all PyTest test cases:
python -m pytest
For a more detailed test execution:
python -m pytest -v

📊 Generate HTML Test Report
To generate the customized HTML report:
python -m pytest --html=reports/report.html --css=css/report.css --self-contained-html
After execution, open:
reports/report.html

📈 Test Execution Result
The framework successfully executes automated login test scenarios and generates an HTML test execution report.
The report provides visibility into:
- Number of tests executed
- Passed tests
- Failed tests
- Execution duration
- Test details
- Execution timestamp

🔄 Automation Workflow
The overall automation workflow is:
Start
  ↓
Load Environment Configuration
  ↓
Initialize Chrome WebDriver
  ↓
Open SauceDemo Login Page
  ↓
Execute Login Test
  ↓
Validate Expected Result
  ↓
Test Passed?
  ├── Yes → Continue
  │
  └── No → Capture Screenshot
  ↓
Generate HTML Report
  ↓
End

🧩 Key Framework Features
✅ Page Object Model
Separates page-specific implementation from test cases.
✅ Reusable Base Page
Common Selenium operations are implemented once and reused.
✅ Explicit Waits
Improves synchronization and test stability.
✅ PyTest Fixtures
Provides reusable setup and test configuration.
✅ Environment Configuration
Keeps application configuration separate from test code.
✅ Failure Screenshots
Automatically captures screenshots when tests fail.
✅ HTML Reporting
Provides a readable test execution report.
✅ Maintainable Structure
The framework can be extended with additional pages and test modules.

🚀 Future Enhancements
The framework can be further extended with:
- Additional page objects
- More functional test scenarios
- Data-driven testing
- Parameterized PyTest tests
- Cross-browser testing
- Parallel test execution
- CI/CD integration
- Jenkins pipeline integration
- GitLab CI/CD integration
- Docker-based test execution
- Advanced test reporting

💡 What This Project Demonstrates
This project demonstrates practical knowledge of:
- Python programming
- Selenium WebDriver
- Web automation
- PyTest
- Page Object Model
- Test case design
- Explicit waits
- Test fixtures
- Failure handling
- Screenshot capture
- HTML reporting
- Environment configuration
- Git and GitHub
- Automation framework structure

👩‍💻 Author
Keerthi Kandula
MCA Graduate | Software Testing | Python | Selenium | SQL

📌 Project Summary
This project demonstrates the design and implementation of a maintainable Selenium automation framework using Python and PyTest.
The framework combines Page Object Model, reusable components, explicit waits, automated test execution, failure screenshots, and HTML reporting to provide a structured approach to web application automation testing.

Selenium_POM_Framework
│
├── pages
├── tests
├── screenshots
├── reports
├── css
│
├── screenshot_utility.py
├── .env
├── .gitignore       
├── README.md        
└── requirements.txt 