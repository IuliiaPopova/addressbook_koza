from model.contact import Contact


def test_add_contact(app):
    """
    test: add contact
    """
    app.contact.create(Contact(first_name="Elena", last_name="Bikova"))

