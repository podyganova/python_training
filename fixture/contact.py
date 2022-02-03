from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        # Add new
        wd.find_element_by_link_text("add new").click()
        self.form_filling(contact)
        # Отображение
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_home_page()
        self.contact_cache = None

    def form_filling(self, contact):
        wd = self.app.wd
        # Adding Data
        # ФИО
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # Компания
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        # Телефоны
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        # Почта
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        # Страница, День рождения
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        # Дополнительно
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        self.delete_some(0)

    def delete_some(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_some_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_edit(self):
        self.delete_edit_some(0)

    def delete_edit_some(self, index): # Удаление через форму редактирования
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # submit
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def delete_edit_id(self, id): # Удаление через форму редактирования
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        # submit
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def delete_all(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//input[@id='MassCB']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def edit(self):
        self.edit_some(0)

    def edit_some(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.form_filling(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_by_id(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % contact.id).click()
        self.form_filling(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_details(self):
        self.edit_details_some(0)

    def edit_details_some(self, index, contact): #Редактирование через форму просмотра
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()
        wd.find_element_by_name("modifiy").click()
        self.form_filling(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_details_id(self, contact):  # Редактирование через форму просмотра
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("a[href='view.php?id=%s']" % contact.id).click()
        wd.find_element_by_name("modifiy").click()
        self.form_filling(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_xpath("//tr[@name='entry']/td[1][@class='center']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            wd.find_element_by_name("MainForm")
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                lastname_text = element.find_element_by_xpath(".//td[2]").text
                firstname_text = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_xpath(".//td[6]").text
                address_text = element.find_element_by_xpath(".//td[4]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id,
                                                  all_phones=all_phones, address=address_text, all_emails=all_emails))
        return list(self.contact_cache)

    def get_contact_edit(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, mobile=mobile,
                       work_phone=work_phone, phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_details(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile=mobile, work_phone=work_phone, phone2=phone2)


