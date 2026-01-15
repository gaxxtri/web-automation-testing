Subject: Test Plan – Multi-Website Functional Testing

# Test Plan — Multi-Website Functional Testing

## 1. Objective

Automate core user journeys across public websites to validate basic search and data retrieval without authentication.

Sites Tested:

* Wikipedia
* Amazon India
* Zomato Chennai
* OpenWeatherMap

## 2. Scope

In Scope:

* Homepage load validation
* Search functionality
* Result verification
* Negative search inputs (blank)

Out of Scope:

* Login or account features
* Checkout, ordering, booking
* Mobile/responsive UI
* Location permissions and advanced filters

## 3. Test Environment

* Windows 10/11
* Python 3.10+
* Selenium WebDriver (Chrome)
* WebDriver Manager
* Chrome Browser latest version
* Stable Internet Connection

## 4. Assumptions

* Sites are publicly accessible
* UI locators remain stable
* Internet connectivity supports dynamic APIs
* Pop-ups can appear unpredictably

## 5. Test Cases

### Wikipedia

TC01 — Homepage loads
Expected: Page title contains “Wikipedia”

TC02 — Search “India”
Expected: Page navigates to results

TC03 — Negative blank search
Expected: Page stays or shows help

### Amazon

TC04 — Homepage loads
Expected: Title contains “Amazon”

TC05 — Search “phone”
Expected: Results list displays items

TC06 — Negative blank search
Expected: Page reloads gracefully

### OpenWeatherMap

TC07 — Homepage loads
Expected: Title contains “Weather”

TC08 — Search “Chennai”
Expected: Result page loads city weather

TC09 — Temperature widget displays
Expected: Temperature element visible
Actual: Fails intermittently — likely API/UI delay

TC10 — Negative blank search
Expected: Page handles no input

### Zomato

TC11 — Chennai city page loads
Expected: Zomato title visible

TC12 — Search “pizza”
Expected: Restaurants list appears

TC13 — Result cards visible
Expected: One or more items displayed
Actual: Often fails due to popups or geo-blocking

TC14 — Blank search
Expected: Controlled UI response (skipped because blocked)

## 6. Risks & Limitations

* Third-party sites update UI frequently
* Rate-limiting can impact OpenWeather tests
* Zomato blocks automated scripts intermittently
* Locator reliability dependent on dynamic DOM changes

## 7. Deliverables

* Automated test scripts (4 files + combined file)
* Execution logs
* Bug report
* README documentation
* Future improved framework (pytest/POM optional)
