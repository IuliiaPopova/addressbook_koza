from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify(Contact(first_name="Dh", last_name="Sttsro"))


def test_modify_contact_name(app):
    app.contact.modify(Contact(first_name="Sttr"))
