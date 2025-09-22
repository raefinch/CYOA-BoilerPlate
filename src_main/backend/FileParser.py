import yaml
from backend.StoryTree import StoryTree
from backend.StoryNode import StoryNode
from backend.Choice import Choice

class FileParser:
    @staticmethod
    def parse_text_to_storytree(file_content):
        """
        Parses a YAML file content into a StoryTree instance.
        Expects a dictionary, where each key is a node_id (e.g., chapter_1).
        """
        data = yaml.safe_load(file_content)  # data is a dict, not a list!
        tree = StoryTree()
        
        for node_id, node_data in data.items():
            node = StoryNode(
                node_id=node_id,
                text=node_data["text"],
                checkpoint=node_data.get("checkpoint", False)
            )
            
            for choice_data in node_data.get("choices", []):
                choice = Choice(
                    choice_data["option"],
                    choice_data["next"],
                    choice_data.get("attribute_changes", {})  # Optional
                )
                node.add_choice(choice)
            tree.add_node(node)
        return tree
