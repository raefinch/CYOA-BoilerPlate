class StoryNode:
    def __init__(self, node_id, text, choices=None, checkpoint=False):
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

    def add_choice(self, choice):
        self.choices.append(choice)
