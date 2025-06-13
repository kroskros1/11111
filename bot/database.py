database = {
    'thresholds': {
        'cutting': 50, 'arming': 50, 'welding': 50,
        'cleaning': 50, 'glazing': 50, 'control': 50
    },
    'settings': {'language': 'UA', 'update_frequency': 30},
    'users': {}
}

def get_threshold(section):
    return database['thresholds'].get(section, 50)

def set_threshold(section, value):
    database['thresholds'][section] = value

def get_settings():
    return database['settings']

def set_setting(key, value):
    database['settings'][key] = value

def add_user(user_id):
    database['users'][user_id] = True