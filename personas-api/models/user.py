from mongoengine import Document, StringField, BooleanField


class User(Document):
    meta = {'collection': 'users'}
    username = StringField(required=True)
    password = StringField(required=True)
    is_admin = BooleanField(default=False)

    def create_user(_username, _password):
        return User(username=_username, password=_password).save()

    def get_user(_username):
        return User.objects(username=_username).first()