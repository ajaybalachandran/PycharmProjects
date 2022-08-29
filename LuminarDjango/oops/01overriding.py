class Editor:
    def functionalities(self):
        return ['create file', 'execute']
class Pycharm(Editor):
    def functionalities(self):
        specs = super().functionalities()
        specs.append('debug')
        return specs
py = Pycharm()
print(py.functionalities())