import pandas
tables_on_page = pandas.read_html("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
table = tables_on_page[0]
table.to_json("table.json", index=False, orient='table')