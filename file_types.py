# written by Patel

from file_types_abstract import FileTypesAbstract

class FileTypes(FileTypesAbstract):
    def create_file_type(self, extension):
        if extension in self.file_types.keys():
            return self.file_types[extension]
        else:
            return None

    def get_file_type(self, extension):
        return self.create_file_type(extension)

    def get_extension_types(self):
        file_type_list = []
        for key in self.file_types:
            file_type_list.append(key)
        return file_type_list
