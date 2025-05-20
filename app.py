import os

# Hardcoded AWS keys (for demo purposes only)
aws_access_key = "AKIAFAKEACCESSKEY12345"
aws_secret_key = "abc123fakeAwsSecretKeyXYZ987"

# Hardcoded Slack webhook
slack_webhook = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

print("Starting app with credentials...")
# Base64 encoded basic auth (demo only)
encoded_auth = "dXNlcjpwYXNzd29yZA=="  # base64 for user:password
