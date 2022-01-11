from backend import setup_db, User, Phonebook


class Controller:
    def __init__(self):
        self.session = setup_db()

    def signUp(self, **kwargs):
        data = User(email=kwargs['email'], password=kwargs['password'], date=kwargs['date'])
        self.session.add(data)
        return self.session.commit()

    def signIn(self, **kwargs):
        user = self.session.query(User).filter_by(email=kwargs['login'], password=kwargs['password'])
        user = user.first()
        if user is not None:
            user.active = True
            self.session.commit()
            user_session = {'id': f'{user.id}', 'name': f'{user.email}'}
            return user_session
        else:
            return False

    def create(self, **kwargs):
        data = Phonebook(name=kwargs['name'], phone=kwargs['phone'], date=kwargs['date'])
        self.session.add(data)
        return self.session.commit()

    def delete(self, **kwargs):
        pass

    def edit(self, **kwargs):
        pass
