"""
Assume we have File class.
    ._file_type
    ._size
    ._file_name

Find Recursive function
array = []
- For every file in current_directory.__files
    - If isInstance(Directory)
        - Recursive calls into directory
    - Else  (is a file)
        - apply filters and add to array
"""

# Parent class
class Filter:  # abstract class
    def apply(self, file):
        if not isinstance(file, File):  # file validation
            raise TypeError

class TypeFilter(Filter):
    def __init__(self, file_type):
        self._file_type = file_type

    def apply(self, file):
        # call parent method to check that this is file
        super().apply(file)

        if file.file_type == self._file_type:
            return True
        return False


class FindCommand:
    def find_all(self, curr_dir, filters):
        # array to hold all applicable files
        all_files = []
        # look in all files in directory. Note, no base case needed. We only recursive call IF it is a valid directory
        for file in curr_dir.files:
            # if file is directory, recursively call find_all for this directory
            if isinstance(file, Directory):
                all_files += self.find_all(file, filters)
            # else: this is file. Apply all filters to file
            for f in filters:
                if f.apply(file):
                    all_files.append(file.name)
        return all_files
