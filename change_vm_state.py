from vm_controller import VmController
from helpers import is_valid_uuid
from user_auth import UserAuth
from dotenv import load_dotenv
import argparse
import os

load_dotenv()


def change_state(vm_id: str, target_state: str):
    if not is_valid_uuid(vm_id):
        raise ValueError('Invalid UUID.')
    if target_state.lower() != 'start' and target_state != 'stop':
        raise ValueError('target_state must be either start or stop.')

    user_auth = UserAuth(
        email=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD')
    )
    vm_controller = VmController(
        user_auth=user_auth,
        vm_id=vm_id
    )

    if target_state.lower() == 'start':
        vm_controller.start_vm()
    else:
        vm_controller.stop_vm()


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        prog='change_vm_state',
        description='Start or stop your VALDI VM programmatically.'
    )
    arg_parser.add_argument('vm_id', help='UUID of your VALDI Virtual Machine', type=str)
    arg_parser.add_argument('target_state', help='Target state, either start or stop', type=str)

    args = arg_parser.parse_args()
    change_state(vm_id=args.vm_id, target_state=args.target_state)
