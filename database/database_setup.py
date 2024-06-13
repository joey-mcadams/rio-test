from articles.create_articles import make_top_articles
from db_engine import *

peewee_db.connect()
peewee_db.create_tables([Author, Article])

a = Author.create(author_name="Sgt. Mayhem Battlinski",
                  style="an over the top Gene Okerlund")
a.save()
a = Author.create(author_name="Emo McSadsadyface",
                  style="like a depressed H.P. Lovecraft")
a.save()

make_top_articles()
peewee_db.close()
print("Done with DB setup.")