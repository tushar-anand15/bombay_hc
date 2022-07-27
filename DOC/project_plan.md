# Code

## Two components:

- everyday cause-lists
- daily orders


## Previous code components

### Code components:

- scraper.py: to handle all functions
- backtrace function to restart scraper from the point it stops working
- *homepage* function to parse the landing page
- *case params* to set the date, case types: get list of cases
- *case details* to get the case types: save all PDFs found

### Additions:

- add the causelist functionality


# Algorithm

## File structure

- scraper.py: main control script
- homepage.py : for processing homepage: causelist and case status functions
- case_params.py : to set case details parameters for parsing the data
- case_details.py: to save the data fir each case
- causelist_params.py: to set causelist parameters for parsing the data
- backtrace.py: to restart the script if it stops, progress bar?
- config files: with case types, dates, other parameters to run the script
