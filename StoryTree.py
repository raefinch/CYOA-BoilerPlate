import json

class StoryTree:
    def __init__(self):
        self.nodes = {}  # Dict of node_id: StoryNode

    def add_node(self, node):
        self.nodes[node.node_id] = node

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def load_from_file(self, filepath):
        """
        Loads story nodes from a JSON formatted file with nodes and choices.
        This is an example format and method; actual format can differ.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for node_data in data["nodes"]:
            node = StoryNode(
                node_id=node_data["id"],
                text=node_data["text"],
                checkpoint=node_data.get("checkpoint", False)
            )
            for choice_data in node_data.get("choices", []):
                choice = Choice(
                    description=choice_data["description"],
                    next_node_id=choice_data["next_node_id"],
                    attribute_changes=choice_data.get("attribute_changes")
                )
                node.add_choice(choice)
            self.add_node(node)

