# Plot-Morning-star-Data
This project is intended to ease the process of plotting financial data downloaded from Morning-star website. It can make line chart from data of mulitple companies which makes it easy for comparison. Besides, you can also save data to csv file if you wish to use excel to make prettier graphs. 


Instructions of using this tool
--------------
- Download financial data from Morning-star website. (e.g. http://financials.morningstar.com/ratios/r.html?t=MRK&region=USA&culture=en_US)
- Run the script, add file/files, then click 'add file complete button'.
- Plot single figure or save data to cvs file for future usage.


Things that you should be aware of
--------------
- The tool doesn't support companies using currency other than USD, because comparing USD with any other currency directly is meaningless.
- If you wish to run the script with python, libs like pandas and matplotlib may be required.
- Downloaded file from Morningstar website shouldn't be renamed, otherwise it would not be accepted.
- Zero in data means there is missing data in original file.

