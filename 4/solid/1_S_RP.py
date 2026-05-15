class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report: {self.data}"

class ResortSaver:
    @staticmethod
    def save_to_file(report, filename):
        with open (filename,'w') as file:
            file.write(report.generate()+'\n' )