import yaml
from backend.StoryNode import StoryNode
from backend.Choice import Choice

class StoryTree:
    def __init__(self):
        self.nodes = {}  # Dict of node_id: StoryNode

    def add_node(self, node: StoryNode):
        self.nodes[node.node_id] = node

    def get_node(self, node_id: str):
        return self.nodes.get(node_id)

    def load_from_file(self, filepath: str):
        """
        Loads story nodes from a YAML file
        """
        
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            print(data)

        for node_id, node_data in data.items():
            node = StoryNode(
                node_id=node_id,
                text=node_data.get("text", ""),
                checkpoint=node_data.get("checkpoint", False)
            )
            for choice_data in node_data.get("choices", []):
                choice = Choice(
                    choice_data.get("option", ""),
                    choice_data.get("next", ""),
                    choice_data.get("attribute_changes", {})
                )
                node.add_choice(choice)

            self.add_node(node)
