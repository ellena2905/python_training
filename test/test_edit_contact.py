from model.contact_info import Contact_info


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact_info(firstname="2", middlename="2", lastname="2", nickname="2", title="2", company_name="2", company_address="1", company_home_num="1", company_home_phone="1", add_company_name="1", company_fax="1", email1="1", email2="1", email3="1", company_site="1", year_of_birth="1", anniversary_year="1", add_address="1", add_phone="1",
                                 notes="987654"))
    app.session.logout()