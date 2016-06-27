

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_pages(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_pages()
        # add new group
        wd.find_element_by_name("new").click()
        # filling
        self.fill_group_form(group)
        # submit
        wd.find_element_by_name("submit").click()
        self.return_to_groups_pages()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_pages()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_pages()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_pages()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #filling new data
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_groups_pages()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_pages()
        self.select_first_group()
        #open_modification_form
        wd.find_element_by_name("edit").click()
        #filling
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_pages()

    def return_to_groups_pages(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
