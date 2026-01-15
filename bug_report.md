Subject: Bug Report — Automation Results

# Bug Report — Multi-Website Automation

## Issue 1 — OpenWeather Temperature Not Displaying

**Site:** [https://openweathermap.org](https://openweathermap.org)
**Test Case:** TC09 — Temperature widget visible
**Observed:** FAIL consistently or intermittently
**Expected:** Temperature element `.weather-widget__temperature` is displayed
**Possible Cause:**

* API delay in data loading
* Widget hidden until network call resolves
* DOM class changed
  **Resolution Tried:**
* Increased wait time (10 → 15 sec)
* Explicit WebDriverWait added
  **Status:** Partial Pass — continue monitoring

---

## Issue 2 — Zomato Search Fails on Main Homepage

**Site:** [https://zomato.com](https://zomato.com)
**Test Case:** TC12/13 — Search results visible
**Observed:** FAIL on homepage

* No search field found
* Exception thrown (NoSuchElementException)
  **Possible Cause:**
* Homepage switched to login-first experience
* IP-based UI
* Cookie & location popups
* Anti-bot protections
  **Workaround:**
  ✔ Access city directly: `zomato.com/chennai`
  ✔ Close popups via automation
  ✔ Search bar using XPath & WebDriverWait
  **Result:** Partial Pass — working on city-specific page only


## Bug 3 — OpenWeather Temperature Widget Timeout (PyTest)
**Test:** test_openweather_search  
**Result:** FAIL  
**Expected:** Temperature widget visible after selecting city  
**Actual:** Timeout after 15s wait using explicit WebDriverWait  
**Insights:**  
- API not responding consistently  
- Widget loads slower than 15 seconds  
**Evidence:** pytest fail + HTML report  
**Status:** Open
---

## Bug 4 — Zomato Search Results Not Rendering (PyTest)
**Test:** test_zomato_search  
**Result:** FAIL (0 restaurant cards detected)  
**Expected:** ≥ 1 result card for “pizza”  
**Actual:** 0 cards found after 5 second wait  
**Hypothesis:**  
- Popups or delayed React rendering  
- Anti-bot UI might silently block  
- CSS class updated from `sc-1hp8d8a-0`  
**Next step:** Capture runtime HTML, revise selector  
**Status:** Open

---

## Test Verdict Summary

| Website     | Pass           | Fail                            |
| ----------- | ---------------| --------------------------------|
| Wikipedia   |  All           | None                            |
| Amazon      |  All           | None                            |
| OpenWeather |  Load & Search | Weather display API/UI delay    |
| Zomato      |  Load          | needs selector/popup fix        |
