from todo.database import User, session_factory, Phone


def create_phone_for_user(user_id):
    session = session_factory()
    phone1 = Phone(id=1, phone_number="89005003040", user_id=user_id)
    session.add(phone1)
    session.commit()
    session.close()


def main1():
    session = session_factory()
    user = session.query(User).first()
    print(user)
    # create_phone_for_user(user.id)
    print(user.phones)
    phone_first = user.phones[0]
    print(phone_first.user)
    session.close()


def main2():
    session = session_factory()
    users = session.query(User).all()
    for user in users:
        print(user, *map(lambda x: x.language, user.languages))
    session.close()


# main1()
main2()

