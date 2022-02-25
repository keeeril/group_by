import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://kir:1111@localhost:5432/music_test')
connection = engine.connect()

connection.execute("""SELECT title, duration FROM tracks
    ORDER BY duration DESC
    LIMIT 1""").fetchall()
