class Character:
    def __init__(self, name, attributes=None):
        """
        name: Name of the main character
        attributes: Dictionary of attribute name to value (e.g. {'mana': 50, 'health': 100})
        """
        self.name = name
        self.attributes = attributes or {}

    def modify_attribute(self, attr, amount):
        """Add or subtract amount from attribute attr"""
        if attr in self.attributes:
            self.attributes[attr] += amount
        else:
            self.attributes[attr] = amount
