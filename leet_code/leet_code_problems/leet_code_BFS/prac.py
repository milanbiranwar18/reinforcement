# #71. Simplify Path

# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file
# system, convert it to the simplified canonical path.
#
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the
# directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this
# problem, any other format of periods such as '...' are treated as file/directory names.
#
# The canonical path should have the following format:
#
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no
# period '.' or double period '..')
# Return the simplified canonical path.
#
#
#
# Example 1:
#
# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
# Example 2:
#
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
# Example 3:
#
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
#

def simplify_path(path):
    # Split the path into its components
    components = path.split('/')
    stack = []
    # Traverse the components, using a stack to keep track of the directories visited
    for component in components:
        if component == '' or component == '.':
            # Ignore empty and current directory components
            continue
        elif component == '..':
            # Go up one directory level, by popping the last directory from the stack
            if stack:
                stack.pop()
        else:
            # Go down one directory level, by adding the current directory to the stack
            stack.append(component)
    # Join the directories in the stack into a simplified canonical path
    return '/' + '/'.join(stack)


def simplify_path1(path):

    compo = path.split('/')
    stack = []
    for component in compo:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    return '/' + '/'.join(stack)


if __name__ == '__main__':
    print(simplify_path1( "/home/"))
