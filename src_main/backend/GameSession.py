from backend.StoryTree import StoryTree
from backend.StoryNode import StoryNode
from backend.Choice import Choice
from backend.Character import Character

class GameSession:
    def __init__(self, story_tree, character):
        self.story_tree = story_tree
        self.character = character
        self.current_node_id = None
        self.checkpoints = []

    def start(self, start_node_id):
        self.current_node_id = start_node_id

    def choose(self, choice_index):
        current_node = self.story_tree.get_node(self.current_node_id)
        if not current_node or choice_index >= len(current_node.choices):
            raise ValueError("Invalid choice index")

        choice = current_node.choices[choice_index]

        # Apply attribute changes to character
        for attr, delta in choice.attribute_changes.items():
            self.character.modify_attribute(attr, delta)

        # Move to next node
        self.current_node_id = choice.next_node_id

        # If this node is checkpoint, save it
        next_node = self.story_tree.get_node(self.current_node_id)
        if next_node and next_node.checkpoint:
            self.checkpoints.append(self.current_node_id)

    def get_current_text(self):
        node = self.story_tree.get_node(self.current_node_id)
        return node.text if node else ""

    def save(self):
        # Implement save logic, e.g. serialize current state to file or DB
        # Example:
        return {
            "current_node_id": self.current_node_id,
            "character_attributes": self.character.attributes,
            "checkpoints": self.checkpoints,
        }

    def load(self, saved_data):
        self.current_node_id = saved_data["current_node_id"]
        self.character.attributes = saved_data["character_attributes"]
        self.checkpoints = saved_data["checkpoints"]
