import pdblp

con = pdblp.BCon(debug=True, port=8194, timeout=5000)
con.start()

# use the bdh method to query data from connection
# bdh has the following parameters
# - Securtiy/Item
# -
con.bdh('SPY US Equity', 'PX_LAST', '20150629', '20150630')

