def inorderTraversal(root):
	visited = []
	if root == None:
		return visited
	stack = []
	while(root is not None or len(stack)>0):
		while root is not None:
			stack.append(root)
			root = root.left
		root = stack.pop(-1)
		visited.append(root)
		root = root.right

	return visited
