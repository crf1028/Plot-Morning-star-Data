import pandas
import Tkinter as tk
import ttk
import tkFileDialog as fd
import matplotlib.pyplot as plt
import datetime


class MainWindow(object, tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack(fill='both')

        style = ttk.Style()
        style.theme_use("vista")

        file2open_pth = []
        self.file2save_pth = datetime.datetime.now().strftime('%Y%m%d%H%M')+'output.csv'
        self.last_packed = 'none'
        self.last_selected_i = 'none'
        self.last_selected_i_list = []
        self.item_saved = []
        self.name_list = []
        self.com_list = []

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

        top_f = ttk.Frame(self)
        top_f.pack(anchor='w', padx=50, pady=(30, 0), fill='both', expand=1)
        ttk.Button(top_f, text='Add File', command=lambda: add_pth_to_list(file2open_pth, out)).pack(side='left',
                                                                                                     padx=(0, 25))
        ttk.Button(top_f, text='Add File Complete',
                   command=lambda: self.make_com_list_name_list(file2open_pth, bot_f)).pack(side='left', padx=25)
        ttk.Button(top_f, text='Plot Last Selected Item',
                   command=lambda: plot_item(self.com_list, self.name_list, self.last_selected_i, index_dic, out)).pack(
            side='left', padx=25)
        ttk.Button(top_f, text='Save to File', command=lambda: self.save2file(index_dic, out)).pack(side='left',
                                                                                                    padx=25)
        out = ttk.Label(top_f, text='Started!')
        out.pack(side='left', padx=25)

        bot_f = ttk.Frame(self)
        bot_f_1 = ttk.Frame(bot_f)
        bot_f_1.pack(side='left', padx=(0, 25), fill='both', expand=1)
        ttk.OptionMenu(bot_f_1, tk.StringVar(), *(['Choose Your Option'] + sorted(index_dic.keys())),
                       command=lambda x: self.pack_cbs(x, cbs_dic)).pack(anchor='w', pady=10)
        for i in index_dic:
            for k in sorted(index_dic[i]):
                cbs_dic[i].append(ttk.Checkbutton(bot_f_1, text=k, command=lambda x=i+","+k: self.a(x, out)))

    def pack_cbs(self, list_name, wid_list):
        if self.last_packed != 'none':
            for i in wid_list[self.last_packed]:
                i.pack_forget()
        for i in wid_list[list_name]:
            i.pack(anchor='w')
        self.last_packed = list_name

    def a(self, b, widget):
        if b in self.last_selected_i_list:
            widget.config(text=b.split(',')[1]+' Unselected!')
            self.last_selected_i_list.remove(b)
            self.last_selected_i = 'Unselected'
        else:
            widget.config(text=b.split(',')[1]+' Selected!')
            self.last_selected_i_list.append(b)
            self.last_selected_i = b

    def save2file(self, index_dict, widget):
        if self.name_list != [] and self.com_list != []:
            if self.last_selected_i_list != self.item_saved:
                df_list2save = [k for k in self.last_selected_i_list if k not in self.item_saved]
                if df_list2save:
                    try:
                        for i in df_list2save:
                            lst = i.split(',')
                            idx = index_dict[lst[0]][lst[1]]
                            ndf = new_df(self.com_list, self.name_list, idx)
                            ndf.index.name = lst[0] + ' -> ' + lst[1]
                            ndf.to_csv(self.file2save_pth, mode='a')
                        widget.config(text='File saved!')
                        self.item_saved += df_list2save
                    except:
                        widget.config(text='Error occurred!')

    def make_com_list_name_list(self, pth, bot_f):
        if pth:
            bot_f.pack(anchor='w', padx=50, pady=10, fill='both', expand=1)
            for i in pth:
                self.name_list.append(i.split('/')[-1][:-15])
                self.com_list.append(reset_index(pandas.read_csv(i, skiprows=2, index_col=0, thousands=',', na_values=["0"])))
            list2del = ['2006-12', '2007-12', '2008-12', '2009-12', '2015-12', 'TTM']           # TODO add csv file validation and delete validation
            for i in self.com_list:
                # i.rename(index={'Year over Year': 'R Year over Year'}, inplace=True)
                for k in list2del:
                    del i[k]


def add_pth_to_list(lst, widget):
    new_pth = fd.askopenfilename()
    if new_pth in lst:
        widget.config(text='Pls add a new file!')
    elif new_pth.split('/')[-1][-14:] != 'Key Ratios.csv':
        widget.config(text='Pls add a valid file!')
    else:
        lst.append(new_pth)
        widget.config(text=lst[-1].split('/')[-1]+' added!')


def plot_item(com_list, name_list, selected, index_dict, widget):
    if name_list != [] and com_list != []:
        if selected == 'Unselected':
            widget.config(text='Pls select an item after unselecting!')
        elif selected == 'none':
            widget.config(text='Pls select an item!')
        else:
            lst = selected.split(',')
            idx = index_dict[lst[0]][lst[1]]
            new_df(com_list, name_list, idx).plot(title=lst[0] + ' -> ' + lst[1])
            plt.show()


def new_df(com_list, name_list, index_usd):
    new_s = []
    for i in range(len(name_list)):
        new_s.append(com_list[i].ix[index_usd])
        new_s[-1].name = name_list[i]
        for k in range(len(new_s[-1])):
            if pandas.isnull(new_s[-1][k]):
                new_s[-1][k] = 0
            elif type(new_s[-1][k]) != float:
                if ',' in new_s[-1][k]:
                    new_s[-1][k] = float(new_s[-1][k].replace(',', ''))
                else:
                    new_s[-1][k] = float(new_s[-1][k])
    return reduce((lambda x, y: pandas.concat([x, y], axis=1)), new_s)


def reset_index(df):
    #   TODO maybe a rowcnt first
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
