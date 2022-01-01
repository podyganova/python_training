class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Создание новой группы
        wd.find_element_by_name("new").click()
        self.form_filling(group)
        # Представление группы
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def form_filling(self, group):
        wd = self.app.wd
        # Заполнение формы
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # edit
        wd.find_element_by_name("edit").click()
        self.form_filling(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def modify_first(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.form_filling(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
