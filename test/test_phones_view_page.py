def test_phones_on_contact_view_page(app):
    contact_details = app.contact.get_contact_details(0)
    contact_edit = app.contact.get_contact_edit(0)
    assert contact_details.home_phone == contact_edit.home_phone
    assert contact_details.mobile == contact_edit.mobile
    assert contact_details.work_phone == contact_edit.work_phone
    assert contact_details.phone2 == contact_edit.phone2
