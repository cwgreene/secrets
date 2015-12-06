import json
import os
import tempfile
import shutil

class FileSystemProvider(object):
    def __init__(self, path=os.path.expanduser("~/.secrets"), creds=None):
        if creds == None:
            creds = credentials
        self.path = path
        self.creds = creds

    def scope_path(self, scope):
        return "%s/%s" % (self.path, scope)

    def getSecrets(self, scope):
        scope_path = self.scope_path(scope)
        if not os.path.exists(scope_path):
            with open(scope_path, "w") as initial:
                initial.write("{}")
        with open(scope_path) as secretFile:
            return json.loads(secretFile.read())

    def removeAllSecrets(self, scope):
        if os.path.exists(self.scope_path(scope)):
            os.remove(self.scope_path(scope))

    def getSecret(self, scope, key):
        return self.getSecrets(scope)[key]

    def storeSecret(self, scope, key, value):
        secrets = self.getSecrets(scope)
        secrets[key] = value
        # File swap
        with tempfile.NamedTemporaryFile(delete=False) as temp_secret_file:
            json.dump(secrets, temp_secret_file)
        shutil.move(temp_secret_file.name, self.scope_path(scope))

    def getScopes(self):
        result = []
        for file in os.listdir(self.path):
            result.append(file)
        return result

    def dumpScope(self, scope):
        print self.getSecrets(scope)

    def dumpSecrets(self):
        for scope in self.getScopes():
            print scope
            self.dumpScope(scope)

credentials = None
provider = FileSystemProvider()

def getSecret(scope, key):
    return provider.get(scope, key)

def removeAllSecrets(scope):
    return provider.removeAllSecrets(scope)

def storeSecret(scope, key, value):
    return provider.storeSecret(scope, key, value)

def setCredentials(creds):
    creds = creds

def dumpSecrets():
    provider.dumpSecrets()

def listScopes():
    return provider.listScopes()

def showScope(scope):
    provider.showScope(scope)
