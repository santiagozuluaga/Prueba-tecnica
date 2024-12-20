import os

def getEnvString(key, defaultValue):
    value = os.getenv(key)

    if value:
        return value
    
    return defaultValue

def getEnvArrayString(key, defaultValue):
    value = os.getenv(key)

    if value:
        return value.split(',')
    
    return defaultValue

def getEnvBool(key, defaultValue):
    value = os.getenv(key)

    if value:
        return bool(value)
    
    return defaultValue