"""Import some modules"""
import toml


class Website:
    """Class for an instance of a website"""

    toml = {}

    def read_toml(self):
        """read in the contents of a toml file"""
        with open("hugo.toml", "r", encoding="utf-8") as tomlfile:
            self.toml = toml.load(tomlfile)

        return self.toml

    def write_toml(self):
        """write the contents of self.toml to a toml file"""
        with open("hugo.toml", "w", encoding="utf-8") as tomlfile:
            toml.dump(self.toml, tomlfile)

    def update_title(self, title):
        """Update the title variable"""
        self.toml["title"] = title
        return title

    def update_description(self, description):
        """Update the description variable"""
        self.toml["description"] = description
        return description

    def update_theme(self, theme):
        """Update the description variable"""
        self.toml["theme"] = theme
        return theme
