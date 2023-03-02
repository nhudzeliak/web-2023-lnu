class Client:
    def insert_lightning_connector_into_computer(self, com):
        print("Client inserts Lightning connector into computer.")
        com.insert_into_lightning_port()


class Computer:
    def insert_into_lightning_port(self):
        pass


class Mac(Computer):
    def insert_into_lightning_port(self):
        print("Lightning connector is plugged into mac machine.")


class Windows:
    def insert_into_usb_port(self):
        print("USB connector is plugged into windows machine.")


class WindowsAdapter(Computer):
    def __init__(self, windows_machine):
        self.windows_machine = windows_machine

    def insert_into_lightning_port(self):
        print("Adapter converts Lightning signal to USB.")
        self.windows_machine.insert_into_usb_port()


if __name__ == '__main__':
    client = Client()
    mac = Mac()
    client.insert_lightning_connector_into_computer(mac)

    windows_machine = Windows()
    windows_machine_adapter = WindowsAdapter(windows_machine)
    client.insert_lightning_connector_into_computer(windows_machine_adapter)