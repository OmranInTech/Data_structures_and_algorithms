#desiging borswer history
class BrowserHistory:
    def __init__(self, homepage):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()  # Clear forward history when visiting new page

    def back(self):
        if not self.back_stack:
            print("No pages to go back to.")
            return self.current
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        if not self.forward_stack:
            print("No pages to go forward to.")
            return self.current
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        return self.current

    def get_current_page(self):
        return self.current


# Example usage:

history = BrowserHistory("google.com")

history.visit("openai.com")
history.visit("github.com")
print("Current page:", history.get_current_page())  # github.com

print("Back to:", history.back())  # openai.com
print("Back to:", history.back())  # google.com
print("Forward to:", history.forward())  # openai.com

history.visit("stackoverflow.com")
print("Current page after new visit:", history.get_current_page())  # stackoverflow.com
print("Forward to:", history.forward())  # No pages to go forward to.
