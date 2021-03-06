import os
import unittest
import supersecret as secrets

class TestSecrets(unittest.TestCase):
    def testFileSecret(self):
        """Tests entire lifecycle of a secret"""
        SCOPE = "testSecrets"
        KEY = "testKey"
        KEY2 = "testKey2"
        SECRET = "Abracdabra"
        SECRET2 = "Abracdabra2"

        # Create provider
        provider = secrets.FileSystemProvider("data/secrets/")
        secrets.provider = provider

        # Create a Scope
        secrets.removeAllSecrets(SCOPE)
        self.assertFalse(os.path.exists(provider.scope_path(SCOPE)))

        # Store Secret
        secrets.storeSecret(SCOPE, KEY, SECRET)
        stored_secret = secrets.getSecret(SCOPE, KEY)
        self.assertEqual(SECRET, stored_secret)

        # Store Another Secret, verify original
        secrets.storeSecret(SCOPE, KEY2, SECRET2)
        stored_secret = secrets.getSecret(SCOPE, KEY)
        self.assertEqual(SECRET, stored_secret)

        # Verify new secret
        stored_secret = secrets.getSecret(SCOPE, KEY2)
        self.assertEqual(SECRET2, stored_secret)

        # Destroy Scope
        secrets.removeAllSecrets(SCOPE)
        self.assertFalse(os.path.exists(provider.scope_path(SCOPE)))
