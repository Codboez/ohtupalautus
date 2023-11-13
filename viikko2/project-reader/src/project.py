class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _stringify_list(self, name, list):
        s = name + ":\n"

        for i in range(len(list)):
            s += f"- {list[i]}\n"

        return s

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\nAuthors: {self._stringify_list('Authors', self.authors)}"
            f"\nDependencies: {self._stringify_list('Dependencies', self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_list('Development dependencies', self.dev_dependencies)}"
        )
