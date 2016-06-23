# -*- coding: utf-8 -*-

from model.contact_info import Contact_info

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact_info(firstname="abcde", middlename="fghijk", lastname="hijklm", nickname="eclipse", title="bpc", company_name="abc", company_address="Prospect mira", company_home_num="10", company_home_phone="123456789", add_company_name="qwe", company_fax="321654", email1="abcde@abc", email2="fghijk@abc", email3="hijklm@abc", company_site="abc.ru", year_of_birth="1990", anniversary_year="2020", add_address="123", add_phone="10", notes="987654"))
    app.session.logout()

def test_add_contact2(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact_info(firstname="1", middlename="1", lastname="1", nickname="1",
                                 title="1", company_name="1", company_address="1", company_home_num="1",
                                 company_home_phone="1", add_company_name="1", company_fax="1",
                                 email1="1", email2="1", email3="1", company_site="1",
                                 year_of_birth="1", anniversary_year="1", add_address="1", add_phone="1",
                                 notes="987654"))
    app.session.logout()


