from random import randrange
from model.contact import Contact

def test_delete_contact(app):


    if app.contact.count() == 0:#checking we have any group or no
        app.contact.create(Contact(first_name="Elena", last_name="Bikova"))#if don't have any group we create one group before delete
    old_contact_list = app.contact.get_contact_list()
    #randrange returns a random int from range(start, stop[, step])
    index = randrange(len(old_contact_list))
    app.contact.delete(index)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list), f"Old list '{old_contact_list}' != new list '{new_contact_list}'"
    old_contact_list[index:index + 1] = []
    assert old_contact_list == new_contact_list
