from random import randrange

from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:#checking we have any group or no
        app.contact.create(Contact(first_name="Elena", last_name="Bikova"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact_id = old_contact_list[index].id
    contact = Contact(first_name="Dh", last_name="Sttsro", id = contact_id)
    app.contact.modify(index=index,contact=contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list), f"Old list '{old_contact_list}' != new list '{new_contact_list}'"
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)



# def test_modify_contact_name(app):
#     app.contact.modify(Contact(first_name="Sttr"))
