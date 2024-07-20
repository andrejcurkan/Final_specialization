class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            raise RuntimeError("Error occurred in try block")
        else:
            if self.count == 0:
                raise ValueError("Resource was not used")
            elif self.count > 1:
                raise ValueError("Resource was not properly closed")
            else:
                print("Resource was properly used and closed")
