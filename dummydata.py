from FlaskApp import db
from FlaskApp.models import User, Video, Comment
from werkzeug.security import generate_password_hash
from datetime import datetime

db.drop_all()
db.create_all()

U1 = User(Username="GuyManDeHomem",Password=generate_password_hash("password"),Description="A Guy who's human after all",Location="Paris,France")
U2 = User(Username="JoelZimmer",Password=generate_password_hash("password"),Description="Just strobing",Location="Toronto,Canada")
U3 = User(Username="NormanCook",Password=generate_password_hash("password"),Description="Funk soul brotha",Location="Brighton,UK")


V1 = Video(Title="Funny Clone Wars",FileName="CloneWarsMeme.mp4",Uploader_id=1)
V2 = Video(Title="Mario Kart meme",FileName="HeyLu.mp4",Uploader_id=1)
V3 = Video(Title="Linux ShitPost",FileName="LinuxUsersBeLike.mp4",Uploader_id=2)

C1 = Comment(Content='Lame video',Commenter_id=1,Video_id=1)
C2 = Comment(Content='Signature Look of Superiority',Commenter_id=3,Video_id=1)
C3 = Comment(Content='She sucks at driving!!',Commenter_id=1,Video_id=2)
C4 = Comment(Content='Poor Luigi!',Commenter_id=2,Video_id=2)
C5 = Comment(Content='I use Arch BTW',Commenter_id=2,Video_id=3)


db.session.add(U1)
db.session.add(U2)
db.session.add(U3)
db.session.add(V1)
db.session.add(V2)
db.session.add(V3)
db.session.add(C1)
db.session.add(C2)
db.session.add(C3)
db.session.add(C4)
db.session.add(C5)
db.session.commit()

print("Data added")
