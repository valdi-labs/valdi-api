# VALDI API

This code is intended as a stopgap for customers who wish to programmatically interface with VALDI. Eventually, VALDI 
will launch a public API that can be accessed directly. For now, these scripts can be used either as a CLI or imported 
Python library.

## Usage

### Install dependencies

You should probably create a virtual environment first, using something like virtualenv.

```
pip install -r requirements.txt
```

### Enter your credentials

Create a file called `.env` in the top-level directory of this repository containing the following:

```
EMAIL=your_valdi_account_email@your_domain.com
PASSWORD=your_valdi_account_password
```

### Run the script

For now, the code is only capable of starting or stopping existing VMs in your account.

To start a VM:
```
python change_vm_state.py [vm_id] start
```

To stop a VM:
```
python change_vm_state.py [vm_id] stop
```