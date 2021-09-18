import axiompy

class FileUtils:
    @staticmethod
    def load_acf(path):
        return axiompy.ACF(FileUtils.read_lines(path))
        
    
    @staticmethod
    def read_lines(path):
        with open(path) as f:
            return f.read().splitlines()
        