from typing import List, Optional

class Choice:
    def __init__(self, option: str, next_node_id: str, attribute_changes: Optional[dict] = None):
        """
        description: Text shown for the choice
        next_node_id: ID of the next StoryNode in the tree after this choice
        attribute_changes: dict of character attribute changes {attr: delta}
        """
        self.option = option
        self.next_node_id = next_node_id
        self.attribute_changes = attribute_changes or {}

    def __str__(self):
        return f"Choice(option='{self.option}', next_node_id='{self.next_node_id}')"
