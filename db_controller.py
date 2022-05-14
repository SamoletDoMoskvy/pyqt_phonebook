from models import setup_db, User, Phonebook


class Controller:
    def __init__(self):
        self.session = setup_db()

    def remember_check(self):
        user = self.session.query(User).filter_by(remember_session=True)
        user = user.first()
        if user is not None:
            user_session = {'id': f'{user.id}', 'name': f'{user.email}'}
            user.active = True
            return user_session
        else:
            return False

    def sign_up(self, **kwargs):
        data = User(email=kwargs['email'], password=kwargs['password'], date=kwargs['date'])
        self.session.add(data)
        return self.session.commit()

    def sign_in(self, **kwargs):
        user = self.session.query(User).filter_by(email=kwargs['login'], password=kwargs['password'])
        user = user.first()
        if user is not None:
            if kwargs['remember_session']:
                user.remember_session = True
            user.active = True
            self.session.commit()
            user_session = {'id': f'{user.id}', 'name': f'{user.email}'}
            return user_session
        else:
            return False

    def logout(self, **kwargs):
        user = self.session.query(User).filter_by(id=kwargs['id'])
        user = user.first()
        user.active = False
        user.remember_session = False
        self.session.commit()

    def create(self, **kwargs):
        data = Phonebook(name=kwargs['name'], phone=kwargs['phone'], date=kwargs['date'])
        self.session.add(data)
        return self.session.commit()

    def get(self, filter=None):
        if filter is None:
            data = self.session.query(Phonebook).all()
            return data
        else:
            data = self.session.query(Phonebook).filter_by(id=filter)
            return data

    def delete(self, **kwargs):
        pass

    def edit(self, **kwargs):
        pass


class RequestsBuffer:
    def __init__(self):
        self.requests = []

    def add(self, *args):
        self.data = args[0]
        # self.data.append(args[0])