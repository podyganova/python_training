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
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # select
        wd.find_element_by_name("selected[]").click()
        # submit
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select
        wd.find_element_by_name("selected[]").click()
        # edit
        wd.find_element_by_name("edit").click()
        self.form_filling(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
