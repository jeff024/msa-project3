from app import db

from datetime import datetime
import dateutil.tz

# Models
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.Text)
    date = db.Column(db.String(32), nullable=False,
        default=datetime.now(dateutil.tz.tzlocal()).strftime('%B %d %Y - %H:%M:%S'))
    author = db.Column(db.String(32))

    def __repr__(self):
        return '<Post %r>' % self.title