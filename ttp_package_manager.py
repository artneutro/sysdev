import logger

class NoPackageFoundException(string):
    pass

class package_lists:

    def __init__(self):
        self.package_lists = {
            A:[B, C],
            B:[D, E, F],
            C:[F],
            F:[G]
        }
    def get_dependencies(self, package_name: str):
        try:
            return self.package_lists(package_name)
        except :
            raise NoPackageFoundException("Package not found: "+e) from e

class package:

    def __init__(self):
        self.name = None
        self.dependencies = []

    def get_package(self, package_name: str):
        self.name = package_name
        return self.name

    def get_dependencies(self, package_name: str):
        pl = package_lists()
        self.dependencies = pl.get_dependencies(package_name)
        return self.dependencies

    def install_package(self) :
        self.package.install_dependencies()
        system.install(self.name)

    def install_dependencies(self) :
        for item in self.get_dependencies(self.name) :
            dep = self.package()
            dep.get_package(item)
            dep = dep.get_dependencies(item)
            dep.install_package()

def main():
    new_package = self.package()
    new_package.get_package(A)
    new_package.get_dependencies(A)
    new_package.install_package(A)
    





