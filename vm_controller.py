from api_utils import start_vm, stop_vm
from user_auth import UserAuth


class VmController:
    def __init__(self, user_auth: UserAuth, vm_id: str):
        self.user_auth = user_auth
        self.vm_id = vm_id

    def stop_vm(self):
        stop_vm(self.user_auth.access_token, self.vm_id)

    def start_vm(self):
        start_vm(self.user_auth.access_token, self.vm_id)
