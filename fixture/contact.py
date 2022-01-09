from model.contact import Contact


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
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_edit(self):
        self.delete_edit_some(0)

    def delete_edit_some(self, index): # Удаление через форму редактирования
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
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

    def edit (self):
        self.edit_some(0)

    def edit_some(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
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
            n = 1
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                lastname_text = element.find_element_by_xpath("//tr[@name='entry']["+str(n)+"]/td[2]").text
                firstname_text = element.find_element_by_xpath("//tr[@name='entry']["+str(n)+"]/td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id))
                n = n+1
        return list(self.contact_cache)
