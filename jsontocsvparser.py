import csv

payload = {
    "admin_permissions": {
        "dashboard_page": {
            "access": True
        },
        "users_page": {
            "access": True
        },
        "conversations_page": {
            "access": True
        },
        "appointments_page": {
            "access": True
        },
        "mass_notification_page": {
            "access": True
        },
        "manage_page": {
            "access": True
        },
    },

    "member_permissions": {
        "dashboard_page": {
            "access": True
        },
        "users_page": {
            "access": True
        },
        "conversations_page": {
            "access": False
        },
        "appointments_page": {
            "access": True
        },
        "mass_notification_page": {
            "access": True
        },
        "manage_page": {
            "access": False
        },
    },

    "biller_permissions": {
        "dashboard_page": {
            "access": True
        },
        "users_page": {
            "access": True
        },
        "conversations_page": {
            "access": False
        },
        "appointments_page": {
            "access": False
        },
        "mass_notification_page": {
            "access": False
        },
        "manage_page": {
            "access": False
        },
    }
}

f = csv.writer(open("test.csv", "w+"))

for key in payload.keys():
    print(key)
    user = key.split('_')[0]
    print(user)
    for task in payload[key].keys():
        if payload[key][task]['access']==True:
            f.writerow(['p',f'{user}',task,"read"])








