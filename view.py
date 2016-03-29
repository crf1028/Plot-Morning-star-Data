from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import JsonResponse
import pandas


def pdo(request):
    t = get_template('pdo.html')
    html = t.render()
    return HttpResponse(html)


def json_receive(request):
    json_dict = {}
    if request.method == "POST":
        com_code_lst = [i.encode('utf-8') for i in request.POST.values()]
        df_list = [reset_index(
            pandas.read_csv("http://financials.morningstar.com/ajax/exportKR2CSV.html?t=" + com_code, skiprows=2,
                            index_col=0, thousands=',', na_values=["0"])) for com_code in com_code_lst]
        for i in range(len(com_code_lst)):
            json_dict.update({com_code_lst[i]: df_list[i].to_json(orient='index')})
    return JsonResponse(json_dict)


new = ['Revenue USD Mil', 'Gross Margin %', 'Operating Income USD Mil', 'Operating Margin %',
       'Net Income USD Mil', 'Earnings Per Share USD', 'Dividends USD', 'Payout Ratio %', 'Shares Mil',
       'Book Value Per Share USD', 'Operating Cash Flow USD Mil', 'Cap Spending USD Mil',
       'Free Cash Flow USD Mil', 'Free Cash Flow Per Share USD', 'Working Capital USD Mil',
       'Key Ratios -> Profitability', 'Margins % of Sales', 'Revenue', 'COGS', 'Gross Margin', 'SG&A', 'R&D',
       'Other', 'Operating Margin', 'Net Int Inc & Other', 'EBT Margin', 'Profitability', 'Tax Rate %',
       'Net Margin %', 'Asset Turnover (Average)', 'Return on Assets %', 'Financial Leverage (Average)',
       'Return on Equity %', 'Return on Invested Capital %', 'Interest Coverage', 'Key Ratios -> Growth', 'nan',
       'Revenue %', 'Revenue Year over Year', 'Revenue 3-Year Average', 'Revenue 5-Year Average',
       'Revenue 10-Year Average', 'Operating Income %', 'Operating Income Year over Year',
       'Operating Income 3-Year Average', 'Operating Income 5-Year Average', 'Operating Income 10-Year Average',
       'Net Income %', 'Net Income Year over Year', 'Net Income 3-Year Average', 'Net Income 5-Year Average',
       'Net Income 10-Year Average', 'EPS %', 'EPS Year over Year', 'EPS 3-Year Average', 'EPS 5-Year Average',
       'EPS 10-Year Average', 'Key Ratios -> Cash Flow', 'Cash Flow Ratios', 'Operating Cash Flow Growth % YOY',
       'Free Cash Flow Growth % YOY', 'Cap Ex as a % of Sales', 'Free Cash Flow/Sales %',
       'Free Cash Flow/Net Income', 'Key Ratios -> Financial Health', 'Balance Sheet Items (in %)',
       'Cash & Short-Term Investments', 'Accounts Receivable', 'Inventory', 'Other Current Assets',
       'Total Current Assets', 'Net PP&E', 'Intangibles', 'Other Long-Term Assets', 'Total Assets',
       'Accounts Payable', 'Short-Term Debt', 'Taxes Payable', 'Accrued Liabilities',
       'Other Short-Term Liabilities', 'Total Current Liabilities', 'Long-Term Debt',
       'Other Long-Term Liabilities', 'Total Liabilities', "Total Stockholders' Equity",
       'Total Liabilities & Equity', 'Liquidity/Financial Health', 'Current Ratio', 'Quick Ratio',
       'Financial Leverage', 'Debt/Equity', 'Key Ratios -> Efficiency Ratios', 'Efficiency',
       'Days Sales Outstanding', 'Days Inventory', 'Payables Period', 'Cash Conversion Cycle',
       'Receivables Turnover', 'Inventory Turnover', 'Fixed Assets Turnover', 'Asset Turnover']


def reset_index(df):
    try:                # TODO add more validation
        df.ix['Revenue USD Mil']        # to validate df that is in usd
    except KeyError:
        raise KeyError          # TODO add self-defined error
    else:
        df.insert(len(df.columns), 'new_index', new)
        df = df.set_index('new_index')
        return df
