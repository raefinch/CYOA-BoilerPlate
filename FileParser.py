class FileParser:
    @staticmethod
    def parse_text_to_storytree(file_content):
        """
        Parses a formatted text file content into a StoryTree instance.
        The exact parsing logic depends on the text format decided.
        """
        # Placeholder example for a simple text format parsing:
        # Could parse JSON, YAML, or custom markup
        # For the example, expect JSON-like structure in string
        data = json.loads(file_content)
        tree = StoryTree()
        for node_data in data["nodes"]:
            node = StoryNode(
                node_id=node_data["id"],
                text=node_data["text"],
                checkpoint=node_data.get("checkpoint", False)
            )
            for choice_data in node_data.get("choices", []):
                choice = Choice(
                    choice_data["description"],
                    choice_data["next_node_id"],
                    choice_data.get("attribute_changes", {})
                )
                node.add_choice(choice)
            tree.add_node(node)
        return tree
