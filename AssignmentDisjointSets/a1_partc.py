from a1_partb import SetList

class DisjointSet:
	def __init__(self):
		self.disjointSet = {}

	def make_set(self, element):
		if element in self.disjointSet:
			return False
		set_list = SetList()
		set_list.make_set(element)
		self.disjointSet[element] = set_list.representative_node()
		return True

	def get_set_size(self, element):
		count = 0
		for key, value in self.disjointSet.items():
			if key == element:
				count = len(value.get_set())
		return count

	def find_set(self, element):
		for key, value in self.disjointSet.items():
			if key == element:
				node=value.get_set().representative()
				return node
		return None
	# def union_set(self, element1, element2):
	#     set1 = SetList()
	#     set2 = SetList()
	#     for key, value in self.disjointSet.items():
	#         setlistt = value.get_set()
	#         node = setlistt.get_front()
	#         if node.data == element1:
	#             set1 = node.get_set()
	#         if node.data == element2:
	#             set2 = node.get_set()
	#     if set1 is set2 or len(set1) == 0 or len(set2) == 0:
	#         return False
	#     set1.union_set(set2)
	#     del (self.disjointSet[element2])
	#     return True

	def union_set(self, element1, element2):
		set1 = SetList()
		set2 = SetList()
		for key, value in self.disjointSet.items():
			current_set = value.get_set()
			if current_set.find_data(element1) is not None:
				node = current_set.find_data(element1)
				set1 = node.get_set()
			if current_set.find_data(element2) is not None:
				node = current_set.find_data(element2)
				set2 = node.get_set()
		if set1 is set2 or len(set1) == 0 or len(set2) == 0:
			return False
		set1.union_set(set2)
		# del (self.disjointSet[element2])
		return True

	def get_num_sets(self):
		unique_list = set()
		for key, value in self.disjointSet.items():
			unique_list.add(value.get_set())
		return len(unique_list)

	def __len__(self):
		return len(self.disjointSet)

# ds = DisjointSet()
# ds.make_set("cat")
# ds.make_set("dog")
# ds.make_set("fish")
# ds.union_set("cat", "dog")
# ds.union_set("cat", "fish")
# ds.find_set("cat")


# class DisjointSet:
#     def __init__(self):
#         self.disjointSet = {}
#
#     def make_set(self, element):
#         if element in self.disjointSet:
#             return False
#         set_list = SetList()
#         set_list.make_set(element)
#         self.disjointSet[element] = set_list.representative_node()
#         return True
#
#     def get_set_size(self, element):
#         count = 0
#         for key, value in self.disjointSet.items():
#             if key == element:
#                 count = len(value.get_set())
#         return count
#
#     def find_set(self, element):
#         for key, value in self.disjointSet.items():
#             if key == element:
#                 return value.get_set().representative()
#
#     def union_set(self, element1, element2):
#         set1 = SetList()
#         set2 = SetList()
#         for key, value in self.disjointSet.items():
#             for node in value.get_set().setList:
#                 if node.get_data() == element1:
#                     set1 = node.get_set()
#                 if node.get_data() == element2:
#                     set2 = node.get_set()
#         if set1 is set2 or len(set1.setList) == 0 or len(set2.setList) == 0:
#             return False
#         set1.union_set(set2)
#         # del (self.disjointSet[element2])
#         return True
#
#     def get_num_sets(self):
#         unique_list = set()
#         for key, value in self.disjointSet.items():
#             unique_list.add(value.get_set())
#         return len(unique_list)
#
#     def __len__(self):
#         return len(self.disjointSet)


