from app import app, db
from app.models import Post

db.drop_all()
db.create_all()

titles = [
    'post 1',
    'post 2',
    'post 3'
]

for title in titles:
    new_post = Post(title=title, content='Content', author="Jeff")
    db.session.add(new_post)
db.session.commit()