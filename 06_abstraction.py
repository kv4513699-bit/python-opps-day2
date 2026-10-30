from abc import ABC, abstractmethod

class FlipCart(ABC):  # abstract class
    def mobile_dashboard(self):
        print("Welcome to dashboard.....")

    def web_dashboard(self):
        print("Welcome to dashboard.....")

    @abstractmethod  # abstract method
    def login(self):
        print("Please enter your credentials.....")

class MobileApp(FlipCart):
    def login(self):
        print("Please enter your credentials.....")

class WebApp(FlipCart):
    def login(self):
        print("Please enter your credentials.....")

mobile_obj = MobileApp()
mobile_obj.mobile_dashboard()
mobile_obj.login()

web_obj = WebApp()
web_obj.web_dashboard()