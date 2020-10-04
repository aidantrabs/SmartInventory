import csv, sqlite3

con = sqlite3.connect("sales_train.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE t (date, date_block_num, shop_id, item_id, item_price, item_cnt_day);") # use your column names here

with open('sales_train.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    reader = csv.DictReader(fin) # comma is default delimiter
    count = 0
    for i in reader:
        to_db = [(i['date'], i['date_block_num'], i['shop_id'], i['item_id'], i['item_price'], i['item_cnt_day'])]
        count +=1
        if count == 100:
            break

cur.executemany("INSERT INTO t (date, date_block_num, shop_id, item_id, item_price, item_cnt_day) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()