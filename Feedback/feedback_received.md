## Feedback 1

**Specific documentation checked:** Code comments for currency converter class    
**Feedback from:** Brendon & Tanya      
**Date of feedback:** 04/12/2024     
**Feedback Provided:**     
- In the CurrencyConverter class, it might be usfule to add some extra error messages for cases like invalide currency codes, so users can understand what went wrong.  
- Possibly include a section in the ReadMe that touches on any ethic considerations, like how the app ensures fair exchange rates and how it handles user's data.  
- Code comments - module level docstrings and clarity on classes.

**Actions to be complete based on feedback:**    
- It would be helpful to add some user-friendly error messsages in the CurrencyConverter class for errors such as unrecognised currencies. 
- Maybe prompt users to try again if they make a mistake.  
- A small section in the ReadMe about ethical considerations would be great addition, letting users know how you ensure the exchange rates are fair and how you handle any date privacy.  
- Review of code comments

**My notes and plan of action based on feedback:**  
- Error messages for incorrect currency code input are captured in currency_converter_functions.py: - no action  
- The application captures real-time exchange rate base on the market using APi key from http://api.exchangeratesapi.io.: - updated in ReadMe with a link to license & service agreement   
- Review code comments: - reviewed and updated to include code examples   

---

## Feedback 2  

**Specific documentation checked:** Currency Converter Terminal CLI Application    
**Feedback from:** Angus   
**Date of feedback:** 04/12/2024     
**Feedback Provided:**     
- Readme - Installation instructions are very clear (great for none coding users!).    
- Application is easy to use and easy to navigate ( i couldn't get the convert currencies using live FX rate working but everything else was simple and easy to use).    
- Only suggestion is maybe add a check after the first currency code (AUD) is selected to let me know that it has worked.    
- Overall great application and would use in my travels.    

**Actions to be complete based on feedback:**  

**My notes and plan of action based on feedback:**  
- The paid API membership has expired since the application assignment. The free access has EUR as the base currency.  
- If the currency code is inccorect an error message will notify the user and will allow 3 attempts.
![screenshot for currency code error](screenshots/convert_using_live_rates.png)

---

## Feedback 3

**Specific documentation checked:** Code Comments for conversion_history class
**Feedback from:** Evan & Jack 
**Date of feedback:** 05/12/2024
**Feedback Provided:** 
- This Class is very comprehensive and well written and does exactly as intended. Very detailed notes explain all aspects of the code and answer any question I would’ve had about it. I am honestly hard up for feedback great use of error to handling, JSON serialisation using best practise, and each method has it’s own responsibility and doing so well and concisely.
**Actions to be complete based on feedback:**

--- 
## Feedback 4

**Specific documentation checked:** ReadMe, main.py, and requirements.txt
**Feedback from:** Declan W & Earvin 
**Date of feedback:** 06/12/2024
**Feedback Provided:** 
- Well-structured Table of Contents and clear navigation.
- Installation steps and dependency details are comprehensive.
- Ethical considerations regarding licenses are well-documented.
- Code in main.py is functional, with meaningful outputs and well-written docstrings.

**Actions to be complete based on feedback:**
ReadMe:  
- Add visual aids (e.g., screenshots or diagrams).  
main.py:  
- Add inline comments for complex logic.  
- Clarify variable names for better readability.
requirements.txt:
- Differentiate essential vs. optional dependencies.

- Ethical Concern: * Privacy of Conversion History: The application saves user conversion history locally. If not properly secured, this data could expose sensitive financial information.
