# Plot-Morning-star-Data
This is a Django/Html version of previous built morning-star data plotter. Now you can use this tool online without setting up python on your pc/mac.


# Check it out online:
[http://crf1028.pythonanywhere.com/pdo/](http://crf1028.pythonanywhere.com/pdo/)


Instructions of using this tool
--------------
- Enter this website by: [CLICK ME](http://crf1028.pythonanywhere.com/pdo/)
- Enter the company you want to add and add it one by one.
- After adding all the companies, click submit.
- Choose the financial data you want to see on the left.


Things that you should be aware of
--------------
- The tool doesn't support companies using currency other than USD, because comparing USD with any other currency directly is meaningless.
- If you wish to run the script with python, libs like pandas and django may be required.
- Simply download the files won't do the trick, you have to set up your own django server locally.
- Missing data point on graph means there is missing data in the original file.


Credits
--------------
- Market Data APIs (v2) is used to get company names, for more info: [LINK](http://dev.markitondemand.com/MODApis/)
- Unofficial API of morning-star website is used,  for more info: [LINK](https://gist.github.com/hahnicity/45323026693cdde6a116)
- Bootstrap is used for easing html design
- Easy-autocomplete is used for auto completing
- Jqplot is used for drawing graphs