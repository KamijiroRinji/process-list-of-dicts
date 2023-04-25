class TreeStore:
    """
    Processes lists of dictionaries.

    :param input_list: list of dicts to process
    """

    def __init__(self, input_list: list) -> None:
        self.input_list = input_list

    def get_all(self) -> list:
        """
        Gets list contents.

        :return: initial list of dicts
        :rtype: list
        """
        return self.input_list

    def get_item(self, item_id: int) -> dict:
        """
        Gets list item by 'id'.

        :param item_id: id of the item to retrieve
        :type item_id: int

        :return: dictionary with given 'id' value
        :rtype: dict
        """
        return next((item for item in self.input_list if item["id"] == item_id), None)

    def get_children(self, parent_id: int) -> list:
        """
        Gets all children of the parent with id 'parent_id'.

        :param parent_id: id of the parent item to retrieve its children
        :type parent_id: int

        :return: list of children dicts
        :rtype: list
        """
        return [item for item in self.input_list if item["parent"] == parent_id]

    def get_all_parents(self, child_id: int) -> list:
        """
        Gets all ancestors of item with id 'child_id'.

        :param child_id: id of the child item to retrieve its ancestors
        :type child_id: int

        :return: list of ancestor dicts
        :rtype: list
        """
        # Creating auxiliary dict for convenience
        parents_map = {item["id"]: [item["parent"]] for item in self.input_list}
        # Creating auxiliary variable 'intermediary_parents'
        #   to keep every iteration's parent id(s) in it
        intermediary_parents, parents = (parents_map[child_id][:], [])
        while intermediary_parents:
            # Get last parent id in list and remove it from intermediary_parents
            parent_id = intermediary_parents.pop()
            # Get parent's parent id and remove it from parents_map
            intermediary_parents.extend(parents_map.pop(parent_id, []))
            # Exclude 'root' parent - it's not present in the given example list as an item
            if type(parent_id) == int:
                # Adding parent item to resulting list
                parents.append(
                    next(item for item in self.input_list if item["id"] == parent_id)
                )
        return parents



if __name__ == "__main__":
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None},
    ]
    ts = TreeStore(items)
