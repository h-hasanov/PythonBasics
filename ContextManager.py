# Example of a context manager is with

class XMLTag:
    def __init__(self, tag):
        self.tag = tag
    
    def __enter__(self):
        print("<%s>" % self.tag)
        return self # Always return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("</%s>" % self.tag)
        return False # True for interpreter to handle whatever
        # exception occurs and False otherwise
    
with XMLTag('head') as head:
    print("This is the body of the xml head")