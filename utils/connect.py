import sqlalchemy as sa

stats_engine = sa.create_engine("postgresql://admin:admin@127.0.0.1:5432/cookie_stats")
db = stats_engine.connect()