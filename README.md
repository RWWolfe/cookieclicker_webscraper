
# Cookie Clicker Webscraper

This is a webscraper that clicks to one million cookies automatically.

![A gif should be here](./readme_assets/cookie_3.gif)

## Cookie Clicker

[Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) has been having some trouble loading recently I have found, though having the website open on your browser while running the program has remedied the issue for me.

## Installation

```bash
pip install sqlalchemy
pip install selenium
pip install psycopg2
```

If you are using wsl like I am [vnc viewer](https://www.realvnc.com/en/connect/download/viewer/)
and [x11vnc](https://linux.die.net/man/1/x11vnc) will get you a display if desired.
```bash
pip install Xvfb
```

[This will help you get chromdriver set up](https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/)

[Selenium](https://selenium-python.readthedocs.io/)

[SQLAlchemy](https://www.sqlalchemy.org/)

[psycopg2](https://pypi.org/project/psycopg2/)

For psql I made a db called cookie_stats, a schema called stats, and the following table:

```SQL
DROP TABLE IF EXISTS cookie_stats.stats.start;
CREATE TABLE cookie_stats.stats.start
(run_id SERIAL PRIMARY KEY, 
 run_name VARCHAR(100),
 run_time FLOAT
)
;
```




## Usage

Once everything is up and running all you have to do is enter a name for the run. When it is over, you will see the run time and both the name and time will be inserted into sql automatically. Invoke __main__.py directly.

```bash
python3 __main__.py
```

## To do

Add more strategies and menuing to allow for viewing the database within the program.