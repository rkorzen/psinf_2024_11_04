from abc import ABC, abstractmethod


class ISender(ABC):

    @abstractmethod
    def send(self):
        raise NotImplementedError

    # @abstractmethod
    # def notify(self):
    #     raise NotImplementedError



class SmsSender(ISender):
    def send(self):
        print("wysyłam sms")



class MailSender(ISender):
    def send(self):
        print("Wysyłam email")


class System:

    def __init__(self, send_class: ISender):
        self.send_class = send_class

    def send(self):
        self.send_class.send()


# s = ISender()
sms = SmsSender()
email = MailSender()
s = System(email)
s.send()