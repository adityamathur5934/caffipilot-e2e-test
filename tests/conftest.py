import sys, os
# Add the repository root (parent of tests directory) to sys.path for module imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
