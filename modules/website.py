"""Import some modules"""


class Website:
    """Class for an instance of a website"""

    toml = {}

    def read_toml(self, theme: str):
        """read in the contents of a toml file"""
        print(theme)
        return NotImplemented

    def write_toml(self):
        """write the contents of self.toml to a toml file"""
        return NotImplemented

    def update_title(self, title):
        """Update the title variable"""
        self.toml["title"] = title
        return title

    def update_description(self, description):
        """Update the description variable"""
        self.toml["description"] = description
        return description
