from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'runodayspring' # Must be replaced by your <storage_account_name>
    account_key = 'yHMZWoaup9QJmuhIiGxqVE+ScKW/KwUoIXt1PMtFOJ/T37USsmvU3QURUydIO511KU39/tCzTooMtrwPFBajsw==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

# class AzureStaticStorage(AzureStorage):
#     account_name = 'djangoaccountstorage' # Must be replaced by your storage_account_name
#     account_key = 'your_key_here' # Must be replaced by your <storage_account_key>
#     azure_container = 'static'
#     expiration_secs = None