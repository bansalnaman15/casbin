import casbin
from casbin.model import Model

e = casbin.Enforcer("model.conf", "policy.csv")

sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

if e.enforce(sub, obj,act):
    # e.load_model()
    perms = [x[1] for x in e.get_permissions_for_user('alice')]
    # print(e.get_permissions_for_user('alice'))
    print(perms)
    # e.add_policy('a','b','c')
    print("in")
    pass
else:
    # deny the request, show an error
    pass

print(e.get_policy())
