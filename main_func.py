import pandas
import Tkinter as tk
import ttk
import tkFileDialog as fd
import matplotlib.pyplot as plt
import datetime
from numpy import NaN

old_index = ['Revenue USD Mil', 'Gross Margin %', 'Operating Income USD Mil', 'Operating Margin %',
             'Net Income USD Mil', 'Earnings Per Share USD', 'Dividends USD', 'Payout Ratio %', 'Shares Mil',
             'Book Value Per Share USD', 'Operating Cash Flow USD Mil', 'Cap Spending USD Mil',
             'Free Cash Flow USD Mil', 'Free Cash Flow Per Share USD', 'Working Capital USD Mil',
             'Key Ratios -> Profitability', 'Margins % of Sales', 'Revenue', 'COGS', 'Gross Margin', 'SG&A', 'R&D',
             'Other', 'Operating Margin', 'Net Int Inc & Other', 'EBT Margin', 'Profitability', 'Tax Rate %',
             'Net Margin %', 'Asset Turnover (Average)', 'Return on Assets %', 'Financial Leverage (Average)',
             'Return on Equity %', 'Return on Invested Capital %', 'Interest Coverage', 'Key Ratios -> Growth', NaN,
             'Revenue %', 'Year over Year', '3-Year Average', '5-Year Average', '10-Year Average', 'Operating Income %',
             'Year over Year', '3-Year Average', '5-Year Average', '10-Year Average', 'Net Income %', 'Year over Year',
             '3-Year Average', '5-Year Average', '10-Year Average', 'EPS %', 'Year over Year', '3-Year Average',
             '5-Year Average', '10-Year Average', 'Key Ratios -> Cash Flow', 'Cash Flow Ratios',
             'Operating Cash Flow Growth % YOY', 'Free Cash Flow Growth % YOY', 'Cap Ex as a % of Sales',
             'Free Cash Flow/Sales %', 'Free Cash Flow/Net Income', 'Key Ratios -> Financial Health',
             'Balance Sheet Items (in %)', 'Cash & Short-Term Investments', 'Accounts Receivable', 'Inventory',
             'Other Current Assets', 'Total Current Assets', 'Net PP&E', 'Intangibles', 'Other Long-Term Assets',
             'Total Assets', 'Accounts Payable', 'Short-Term Debt', 'Taxes Payable', 'Accrued Liabilities',
             'Other Short-Term Liabilities', 'Total Current Liabilities', 'Long-Term Debt',
             'Other Long-Term Liabilities', 'Total Liabilities', "Total Stockholders' Equity",
             'Total Liabilities & Equity', 'Liquidity/Financial Health', 'Current Ratio', 'Quick Ratio',
             'Financial Leverage', 'Debt/Equity', 'Key Ratios -> Efficiency Ratios', 'Efficiency',
             'Days Sales Outstanding', 'Days Inventory', 'Payables Period', 'Cash Conversion Cycle',
             'Receivables Turnover', 'Inventory Turnover', 'Fixed Assets Turnover', 'Asset Turnover']

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

revenue_index_dic = dict(zip(
    ['Revenue', 'Gross Margin', 'Operating Income', 'Operating Margin', 'Net Income', 'Earnings Per Share',
     'Dividends', 'Payout Ratio', 'Shares', 'Book Value Per Share', 'Operating Cash Flow', 'Cap Spending',
     'Free Cash Flow', 'Free Cash Flow Per Share', 'Working Capital'],
    ['Revenue USD Mil', 'Gross Margin %', 'Operating Income USD Mil', 'Operating Margin %',
     'Net Income USD Mil', 'Earnings Per Share USD', 'Dividends USD', 'Payout Ratio %', 'Shares Mil',
     'Book Value Per Share USD', 'Operating Cash Flow USD Mil', 'Cap Spending USD Mil',
     'Free Cash Flow USD Mil', 'Free Cash Flow Per Share USD', 'Working Capital USD Mil']))
margins_pct_of_sales_index_dic = dict(zip(
    ['Revenue', 'COGS', 'Gross Margin', 'SG&A', 'R&D', 'Other', 'Operating Margin', 'Net Int Inc & Other',
     'EBT Margin'],
    ['Revenue', 'COGS', 'Gross Margin', 'SG&A', 'R&D', 'Other', 'Operating Margin', 'Net Int Inc & Other',
     'EBT Margin']))
profitability_index_dic = dict(zip(
    ['Tax Rate', 'Net Margin', 'Asset Turnover', 'Return on Assets', 'Financial Leverage', 'Return on Equity',
     'Return on Invested Capital', 'Interest Coverage'],
    ['Tax Rate %', 'Net Margin %', 'Asset Turnover (Average)', 'Return on Assets %',
     'Financial Leverage (Average)', 'Return on Equity %', 'Return on Invested Capital %',
     'Interest Coverage']))
growth_index_dic = dict(zip(
    ['Revenue Year over Year', 'Revenue 3-Year Average', 'Revenue 5-Year Average', 'Revenue 10-Year Average',
     'Operating Income Year over Year', 'Operating Income 3-Year Average', 'Operating Income 5-Year Average',
     'Operating Income 10-Year Average', 'Net Income Year over Year', 'Net Income 3-Year Average',
     'Net Income 5-Year Average', 'Net Income 10-Year Average', 'EPS Year over Year', 'EPS 3-Year Average',
     'EPS 5-Year Average', 'EPS 10-Year Average'],
    ['Revenue Year over Year', 'Revenue 3-Year Average', 'Revenue 5-Year Average', 'Revenue 10-Year Average',
     'Operating Income Year over Year', 'Operating Income 3-Year Average', 'Operating Income 5-Year Average',
     'Operating Income 10-Year Average', 'Net Income Year over Year', 'Net Income 3-Year Average',
     'Net Income 5-Year Average', 'Net Income 10-Year Average', 'EPS Year over Year', 'EPS 3-Year Average',
     'EPS 5-Year Average', 'EPS 10-Year Average']))
cash_flow_ratios_index_dic = dict(zip(
    ['Operating Cash Flow Growth % YOY', 'Free Cash Flow Growth % YOY', 'Cap Ex as a % of Sales',
     'Free Cash Flow/Sales', 'Free Cash Flow/Net Income'],
    ['Operating Cash Flow Growth % YOY', 'Free Cash Flow Growth % YOY', 'Cap Ex as a % of Sales',
     'Free Cash Flow/Sales %', 'Free Cash Flow/Net Income']))
balance_sheet_items_in_pct_index_dic = dict(zip(
    ['Cash & Short-Term Investments', 'Accounts Receivable', 'Inventory', 'Other Current Assets',
     'Total Current Assets', 'Net PP&E', 'Intangibles', 'Other Long-Term Assets', 'Total Assets',
     'Accounts Payable', 'Short-Term Debt', 'Taxes Payable', 'Accrued Liabilities',
     'Other Short-Term Liabilities', 'Total Current Liabilities', 'Long-Term Debt',
     'Other Long-Term Liabilities', 'Total Liabilities', "Total Stockholders' Equity",
     'Total Liabilities & Equity'],
    ['Cash & Short-Term Investments', 'Accounts Receivable', 'Inventory', 'Other Current Assets',
     'Total Current Assets', 'Net PP&E', 'Intangibles', 'Other Long-Term Assets', 'Total Assets',
     'Accounts Payable', 'Short-Term Debt', 'Taxes Payable', 'Accrued Liabilities',
     'Other Short-Term Liabilities', 'Total Current Liabilities', 'Long-Term Debt',
     'Other Long-Term Liabilities', 'Total Liabilities', "Total Stockholders' Equity",
     'Total Liabilities & Equity']))
liquidity_index_dic = dict(zip(
    ['Current Ratio', 'Quick Ratio', 'Financial Leverage', 'Debt/Equity'],
    ['Current Ratio', 'Quick Ratio', 'Financial Leverage', 'Debt/Equity']))
efficiency_ratios_index_dic = dict(zip(
    ['Days Sales Outstanding', 'Days Inventory', 'Payables Period', 'Cash Conversion Cycle',
     'Receivables Turnover', 'Inventory Turnover', 'Fixed Assets Turnover', 'Asset Turnover'],
    ['Days Sales Outstanding', 'Days Inventory', 'Payables Period', 'Cash Conversion Cycle',
     'Receivables Turnover', 'Inventory Turnover', 'Fixed Assets Turnover', 'Asset Turnover']))
index_dic = dict(zip(
    ['Revenue In USD (Mil)', 'Margins % of Sales', 'Profitability', 'Growth', 'Cash Flow Ratios',
     'Balance Sheet Items (in %)', 'Liquidity/Financial Health', 'Efficiency Ratios'],
    [revenue_index_dic, margins_pct_of_sales_index_dic, profitability_index_dic, growth_index_dic,
     cash_flow_ratios_index_dic, balance_sheet_items_in_pct_index_dic, liquidity_index_dic,
     efficiency_ratios_index_dic]))
cbs_dic = dict(zip(
    ['Revenue In USD (Mil)', 'Margins % of Sales', 'Profitability', 'Growth', 'Cash Flow Ratios',
     'Balance Sheet Items (in %)', 'Liquidity/Financial Health', 'Efficiency Ratios'],
    [[], [], [], [], [], [], [], []]))

file_pth2open_lst = []
file_pth2save = datetime.datetime.now().strftime('%Y%m%d%H%M') + 'output.csv'
last_packed = ['none']
last_selected_i = ['none']
last_selected_i_list = []
item_saved = []
name_list = []
com_list = []
year_list = []
year_list2use = []


class MainWindow(object, tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack(fill='both')

        style = ttk.Style()
        style.theme_use("vista")

        top_f_2 = ttk.Frame(self)
        top_f_2.pack(anchor='w', padx=50, pady=(30, 0), fill='both', expand=1)
        ttk.Button(top_f_2, text='Plot Last Selected Item', command=lambda: plot_item(status_label)).pack(side='left', padx=(0, 25))
        ttk.Button(top_f_2, text='Save to File', command=lambda: save2file(status_label)).pack(side='left', padx=25)
        status_label = ttk.Label(top_f_2, text='Started!')
        status_label.pack(side='left', padx=25)

        top_f = ttk.Frame(self)
        top_f.pack(anchor='w', padx=50, pady=(30, 0), fill='both', expand=1)
        b_af = ttk.Button(top_f, text='Add File', command=lambda: add_csv_file(status_label))
        b_af.pack(side='left', padx=(0, 25))
        b_afc = ttk.Button(top_f, text='Add File Complete', command=lambda: add_file_complete_func(top_f, b_af, b_afc, b_syc))
        b_afc.pack(side='left', padx=(25, 50))
        b_syc = ttk.Button(top_f, text='Select years complete!', command=lambda: select_years_complete(top_f, bot_f))

        bot_f = ttk.Frame(self)
        bot_f_1 = ttk.Frame(bot_f)
        bot_f_1.pack(side='left', padx=(0, 25), fill='both', expand=1)
        ttk.OptionMenu(bot_f_1, tk.StringVar(), *(['Choose Your Option'] + sorted(index_dic.keys())),
                       command=lambda x: pack_cbs(x, cbs_dic)).pack(anchor='w', pady=10)
        for i in index_dic:
            for k in sorted(index_dic[i]):
                cbs_dic[i].append(ttk.Checkbutton(bot_f_1, text=k, command=lambda x=i+","+k: cb_func(x, status_label)))


def add_csv_file(widget):
    new_pth = fd.askopenfilename()
    if new_pth in file_pth2open_lst:
        widget.config(text='Pls add a new file!')
    elif new_pth.split('/')[-1][-14:] != 'Key Ratios.csv':
        widget.config(text='Pls add a valid file!')
    else:
        temp_df = pandas.read_csv(new_pth, skiprows=2, index_col=0, thousands=',', na_values=["0"])
        del temp_df['TTM']
        if temp_df.index.tolist() == old_index:
            com_list.append(reset_index(temp_df))
            file_pth2open_lst.append(new_pth)
            widget.config(text=file_pth2open_lst[-1].split('/')[-1] + ' added!')
            name_list.append(new_pth.split('/')[-1][:-15])
        else:
            widget.config(text='Pls add a valid file!')


def add_file_complete_func(top_f, b1, b2, b3):
    if file_pth2open_lst:
        b1.pack_forget()
        b2.pack_forget()
        for i in com_list:
            for k in i.columns.tolist():
                if k not in year_list:
                    year_list.append(k)
        for i in year_list:
            ttk.Checkbutton(top_f, text=i[:4], command=lambda x=i: modify_year_list(x)).pack(anchor='w')
        b3.pack(anchor='w')


def modify_year_list(x):
    if x in year_list2use:
        year_list2use.remove(x)
    else:
        year_list2use.append(x)


def select_years_complete(top_f, bot_f):
    top_f.pack_forget()
    bot_f.pack(anchor='w', padx=50, pady=10, fill='both', expand=1)
    year2del = [i for i in year_list if i not in year_list2use]
    for i in com_list:
        for k in year2del:
            try:
                del i[k]
            except:
                print 'error'


def pack_cbs(list_name, wid_list):
    if last_packed[0] != 'none':
        for i in wid_list[last_packed[0]]:
            i.pack_forget()
    for i in wid_list[list_name]:
        i.pack(anchor='w')
    last_packed[0] = list_name


def cb_func(b, widget):
    if b in last_selected_i_list:
        widget.config(text=b.split(',')[1]+' Unselected!')
        last_selected_i_list.remove(b)
        last_selected_i[0] = 'Unselected'
    else:
        widget.config(text=b.split(',')[1]+' Selected!')
        last_selected_i_list.append(b)
        last_selected_i[0] = b


def plot_item(widget):
    if name_list != [] and com_list != []:
        if last_selected_i[0] == 'Unselected':
            widget.config(text='Pls select an item after unselecting!')
        elif last_selected_i[0] == 'none':
            widget.config(text='Pls select an item!')
        else:
            lst = last_selected_i[0].split(',')
            idx = index_dic[lst[0]][lst[1]]
            new_df(idx).plot(title=lst[0] + ' -> ' + lst[1])
            plt.show()


def save2file(widget):
    if name_list != [] and com_list != []:
        if last_selected_i_list != item_saved:
            df_list2save = [k for k in last_selected_i_list if k not in item_saved]
            if df_list2save:
                try:
                    for i in df_list2save:
                        lst = i.split(',')
                        idx = index_dic[lst[0]][lst[1]]
                        ndf = new_df(idx)
                        ndf.index.name = lst[0] + ' -> ' + lst[1]
                        ndf.to_csv(file_pth2save, mode='a')
                    widget.config(text='File saved!')
                    item_saved.extend(df_list2save)
                except:
                    widget.config(text='Error occurred!')


def new_df(index_usd):
    new_s = []
    for i in range(len(name_list)):
        new_s.append(com_list[i].ix[index_usd])
        new_s[-1].name = name_list[i]
        for k in range(len(new_s[-1])):
            if pandas.isnull(new_s[-1][k]):     # could be modified to show missing data instead of showing '0'
                new_s[-1][k] = 0
            elif type(new_s[-1][k]) != float:
                if ',' in new_s[-1][k]:
                    new_s[-1][k] = float(new_s[-1][k].replace(',', ''))
                else:
                    new_s[-1][k] = float(new_s[-1][k])
    return reduce((lambda x, y: pandas.concat([x, y], axis=1)), new_s)


def reset_index(df):
    df.insert(len(df.columns), 'new_index', new)
    df = df.set_index('new_index')
    return df


def main():
    root = tk.Tk()
    root.geometry('1000x600')
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
