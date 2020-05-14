# GoUnlimited
Unofficial Python API form GoUnlimited.to

Features:
 - Truly Unlimited
 - HD Ready
 - Fast Streaming
 - No Restrictions
 - 100% Free
 - Powerful Panel

Usage:

```python
from gounlimited import GoUnlimited

gu = GoUnlimited('YOUR_API_KEY')

# Get Account info
gu.account_info()

# Get account statistics
gu.account_statistics()

# Get upload server address
gu.upload_server()

# Upload video from local
gu.upload_local(server_url='UPLOAD_SERVER_URL', filepath='VIDEO_FILE_PATH')

# Upload video from link
gu.upload_remote(url='VIDEO_URL')

# Get info/check file(s)
gu.file_info(file_code='FILE_ID')

# Get files list
gu.file_list(page=1, per_page=20, folder_id=12345, public=1, created='DATE', title='TITLE')

# Rename file(s)
gu.file_rename(file_code='FILE_ID', title='TITLE')

# Clone file(s)
gu.file_clone(file_code='FILE_ID')

# Get direct link of file(s) for selected quality
gu.file_direct_link(file_code='FILE_ID', quality='QUALITY')

# Set file(s) folder
gu.file_set_folder(file_code='FILE_ID', folder_id=12345)

# Get folders list
gu.folder_list(folder_id=12345)

# Create new folder
gu.folder_create(parent_id=12345, name='NAME')

# Rename folder
gu.folder_rename(folder_id=12345, name='NAME')

# Get last files deleted
gu.files_deleted(limit=10)

# Get files schedules for DMCA delete
gu.files_dmca(limit=10)

```
