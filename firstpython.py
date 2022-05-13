Extracting and Visualizing Stock Data
Description
In this project, Tesla stock data are extracted and analyzed. Then it's graphed to show the patterns and trends.

Install Modules
!pip install yfinance==0.1.67
!pip install plotly==5.3.1
Requirement already satisfied: yfinance==0.1.67 in c:\users\tham\anaconda3\lib\site-packages (0.1.67)
Requirement already satisfied: multitasking>=0.0.7 in c:\users\tham\anaconda3\lib\site-packages (from yfinance==0.1.67) (0.0.10)
Requirement already satisfied: lxml>=4.5.1 in c:\users\tham\anaconda3\lib\site-packages (from yfinance==0.1.67) (4.6.4)
Requirement already satisfied: pandas>=0.24 in c:\users\tham\anaconda3\lib\site-packages (from yfinance==0.1.67) (1.1.3)
Requirement already satisfied: numpy>=1.15 in c:\users\tham\anaconda3\lib\site-packages (from yfinance==0.1.67) (1.19.2)
Requirement already satisfied: requests>=2.20 in c:\users\tham\anaconda3\lib\site-packages (from yfinance==0.1.67) (2.26.0)
Requirement already satisfied: pytz>=2017.2 in c:\users\tham\anaconda3\lib\site-packages (from pandas>=0.24->yfinance==0.1.67) (2021.1)
Requirement already satisfied: python-dateutil>=2.7.3 in c:\users\tham\anaconda3\lib\site-packages (from pandas>=0.24->yfinance==0.1.67) (2.8.1)
Requirement already satisfied: charset-normalizer~=2.0.0; python_version >= "3" in c:\users\tham\anaconda3\lib\site-packages (from requests>=2.20->yfinance==0.1.67) (2.0.12)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\tham\anaconda3\lib\site-packages (from requests>=2.20->yfinance==0.1.67) (1.26.9)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\tham\anaconda3\lib\site-packages (from requests>=2.20->yfinance==0.1.67) (2020.6.20)
Requirement already satisfied: idna<4,>=2.5; python_version >= "3" in c:\users\tham\anaconda3\lib\site-packages (from requests>=2.20->yfinance==0.1.67) (2.10)
Requirement already satisfied: six>=1.5 in c:\users\tham\anaconda3\lib\site-packages (from python-dateutil>=2.7.3->pandas>=0.24->yfinance==0.1.67) (1.15.0)
Requirement already satisfied: plotly==5.3.1 in c:\users\tham\anaconda3\lib\site-packages (5.3.1)
Requirement already satisfied: six in c:\users\tham\anaconda3\lib\site-packages (from plotly==5.3.1) (1.15.0)
Requirement already satisfied: tenacity>=6.2.0 in c:\users\tham\anaconda3\lib\site-packages (from plotly==5.3.1) (8.0.1)
Import Libraries
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
Define Graphing Function
In this section, we define the function make_graph. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
Use yfinance to Extract Stock Data
Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is TSLA.

tesla = yf.Ticker("TSLA")
tesla
yfinance.Ticker object <TSLA>
Using the ticker object and the function history, extract stock information and save it in a dataframe named tesla_data. Set the period parameter to max so we get information for the maximum amount of time.

tesla_data = tesla.history(period="max")
tesla_data
Open	High	Low	Close	Volume	Dividends	Stock Splits
Date							
2010-06-29	3.800000	5.000000	3.508000	4.778000	93831500	0	0.0
2010-06-30	5.158000	6.084000	4.660000	4.766000	85935500	0	0.0
2010-07-01	5.000000	5.184000	4.054000	4.392000	41094000	0	0.0
2010-07-02	4.600000	4.620000	3.742000	3.840000	25699000	0	0.0
2010-07-06	4.000000	4.000000	3.166000	3.222000	34334500	0	0.0
...	...	...	...	...	...	...	...
2022-05-09	836.450012	845.630005	781.150024	787.109985	30270100	0	0.0
2022-05-10	819.309998	825.359985	774.250000	800.039978	28133900	0	0.0
2022-05-11	795.000000	809.770020	727.200012	734.000000	32408200	0	0.0
2022-05-12	701.000000	759.659973	680.000000	728.000000	46771000	0	0.0
2022-05-13	773.479980	787.349915	751.565002	764.269897	28709973	0	0.0
2991 rows × 7 columns

Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and display the first five rows of the tesla_data dataframe using the head function.

tesla_data.reset_index(inplace=True)
tesla_data.head()
index	Date	Open	High	Low	Close	Volume	Dividends	Stock Splits
0	0	2010-06-29	3.800	5.000	3.508	4.778	93831500	0	0.0
1	1	2010-06-30	5.158	6.084	4.660	4.766	85935500	0	0.0
2	2	2010-07-01	5.000	5.184	4.054	4.392	41094000	0	0.0
3	3	2010-07-02	4.600	4.620	3.742	3.840	25699000	0	0.0
4	4	2010-07-06	4.000	4.000	3.166	3.222	34334500	0	0.0
Use Webscraping to Extract Tesla Revenue Data
Use the requests library to download the webpage https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue. Save the text of the response as a variable named html_data.

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

html_data  = requests.get(url).text
Parse the html data using beautiful_soup.

soup = BeautifulSoup(html_data, 'html5lib')
Using BeautifulSoup, extract the table with Tesla Quarterly Revenue and store it into a dataframe named tesla_revenue. The dataframe should have columns Date and Revenue.

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    
    # Finally we append the data of each row to the table
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)    
    
tesla_revenue
Date	Revenue
0	2021	$53,823
1	2020	$31,536
2	2019	$24,578
3	2018	$21,461
4	2017	$11,759
5	2016	$7,000
6	2015	$4,046
7	2014	$3,198
8	2013	$2,013
9	2012	$413
10	2011	$204
11	2010	$117
12	2009	$112
Execute the following line to remove the comma and dollar sign from the Revenue column.

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue
Date	Revenue
0	2021	53823
1	2020	31536
2	2019	24578
3	2018	21461
4	2017	11759
5	2016	7000
6	2015	4046
7	2014	3198
8	2013	2013
9	2012	413
10	2011	204
11	2010	117
12	2009	112
Execute the following lines to remove an null or empty strings in the Revenue column.

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue
Date	Revenue
0	2021	53823
1	2020	31536
2	2019	24578
3	2018	21461
4	2017	11759
5	2016	7000
6	2015	4046
7	2014	3198
8	2013	2013
9	2012	413
10	2011	204
11	2010	117
12	2009	112
Display the last 5 row of the tesla_revenue dataframe using the tail function.

tesla_revenue.tail()
Date	Revenue
8	2013	2013
9	2012	413
10	2011	204
11	2010	117
12	2009	112
Plot Tesla Stock Graph
Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph. The structure to call the make_graph function is make_graph(tesla_data, tesla_revenue, 'Tesla').

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2022-5-13']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2022-5-13']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    
make_graph(tesla_data, tesla_revenue, 'Tesla')
