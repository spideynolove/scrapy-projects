import sqlite3
import os

dirname = os.path.dirname(__file__)
conn = sqlite3.connect(f"{dirname}/quotes.db")

curr = conn.cursor()

# curr.execute("""create table quotes_tb(title text,author text,tag text)""")
# curr.execute("""insert into quotes_tb values('My name is Ngoc','Ngoc','intro, yourname')""")
# curr.execute("""delete from quotes_tb where author='Hung'""")
# curr.execute("""select * from quotes_tb""")

conn.commit()
conn.close()

remember = """
https://stackoverflow.com/questions/21944936/error-1045-28000-access-denied-for-user-rootlocalhost-using-password-y
    - using: mysql -u root -p
"""
