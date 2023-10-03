# Example authorize module (authorize.py)

# A simple authorization function that checks if a user has a specified role.
# You can replace this with your own authorization logic.

def authorize(uname, sessionid, roles):
    # In this example, we check if the user has one of the specified roles.
    # If the user has one of the roles, they are authorized.
    if "admin" in roles:
        return True
    return False

# You can add more complex authorization logic as needed.
