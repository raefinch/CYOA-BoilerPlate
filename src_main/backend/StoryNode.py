import yaml
from typing import List, Optional
from backend.Choice import Choice

class StoryNode:
    def __init__(self, node_id: str, text:str, choices: Optional[List[Choice]] = None, checkpoint: bool = False):
        """
        node_id: Unique identifier for this story node
        text: Narrative text of the node
        choices: list of Choice objects
        checkpoint: Boolean flag if this node is a checkpoint
        """
        self.node_id = node_id
        self.text = text
        self.choices = choices or []
        self.checkpoint = checkpoint

    def add_choice(self, choice: Choice):
        self.choices.append(choice)

    def __str__(self):
        return f"StoryNode({self.node_id}, {len(self.choices)} choices, checkpoint={self.checkpoint})"