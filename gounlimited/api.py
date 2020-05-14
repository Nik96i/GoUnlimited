import requests
import sys
import re


class GoUnlimited:
    """
    GoUnlimited.to API.
    """

    BASE_URL = 'https://api.gounlimited.to/api/{}/{}'

    def __init__(self, api_key):
        """
        Initialize Class.
        :param str api_key: GoUnlimited api key
        """
        self.api_key = api_key

    def req(self, loc, action, params=None):
        """
        Requests to API.
        :param str loc: Request location
        :param str action: Request action
        :param dict params: Request parameters
        :return dict: Response result
        """
        if params is None:
            params = {}
        params['api_key'] = self.api_key
        url = self.BASE_URL.format(loc, action)
        try:
            r = requests.get(url, params=params)
            if r.status_code == 200:
                response = r.json()
                if response['msg'] != 'Invalid key':
                    return response
                else:
                    sys.exit("Invalid API key, please check your API key")
            else:
                sys.exit("Request failed, error code: {}".format(str(r.status_code)))
        except ConnectionError as e:
            sys.exit(f"ERROR : {e}")

    def upload(self, server_url, filepath):
        """
        Upload file from local.
        :param str server_url: Upload server URL
        :param str filepath: File address
        :return dict: Upload file result
        """
        data = {'api_key': self.api_key}
        file_name = filepath.split("/")[-1]
        files = {'file': (file_name, open(filepath, "rb"))}
        up = requests.post(server_url, data=data, files=files)
        st = re.findall(r'name="st">(.*?)</text', str(up.text))
        fn = re.findall(r'name="fn">(.*?)</text', str(up.text))
        if 'OK' == st[0]:
            return {
                'status': st[0],
                'file_id': fn[0],
                'file_url': 'https://gounlimited.to/{}'.format(fn[0]),
            }
        else:
            raise TypeError('Unsupported video format')

    def account_info(self):
        """
        Account info.
        :return dict: Account info result
        """
        return self.req(loc='account', action='info')

    def account_statistics(self, last=None):
        """
        Account stats.
        :param int last: Return stats for last X days
        :return dict: Account stats result
        """
        params = {}
        if last:
            params['last'] = last
        return self.req(loc='account', action='stats', params=params)

    def upload_server(self):
        """
        Get server upload address.
        :return dict: Server upload address result
        """
        return self.req(loc='upload', action='server')

    def upload_local(self, server_url, filepath):
        """
        Upload file.
        :param str server_url: Server url
        :param str filepath: File address
        :return dict: Upload file result
        """
        return self.upload(server_url=server_url, filepath=filepath)

    def upload_remote(self, url):
        """
        Add URL to upload queue.
        :param str url: URL to video file
        :return dict: Remote upload result
        """
        return self.req(loc='upload', action='url', params={'url': url})

    def file_info(self, file_code):
        """
        Get info/check file(s).
        :param str file_code: File code, or list separated by comma
        :return dict: File(s) information
        """
        return self.req(loc='file', action='info', params={'file_code': file_code})

    def file_list(self, page=None, per_page=None, folder_id=None, public=None, created=None, title=None):
        """
        Get files list.
        :param int page: Page number
        :param int per_page: Number of results per page
        :param int folder_id: Folder ID
        :param int public: Show public (1) or private (0) files only
        :param str created: Show only files uploaded after timestamp
        :param str title: Filter video titles
        :return dict: List of files
        """
        params = {}
        if page:
            params['page'] = page
        if per_page:
            params['per_page'] = per_page
        if folder_id:
            params['fld_id'] = folder_id
        if public:
            params['public'] = public
        if created:
            params['created'] = created
        if title:
            params['title'] = title
        return self.req(loc='file', action='list', params=params)

    def file_rename(self, file_code, title):
        """
        Rename file(s).
        :param str file_code: File code, or list separated by comma
        :param str title: New file title
        :return dict: Rename result
        """
        return self.req(loc='file', action='rename', params={
            'file_code': file_code,
            'title': title,
        })

    def file_clone(self, file_code):
        """
        Clone file(s).
        :param str file_code: File code, or list separated by comma
        :return dict: Cloned file(s)
        """
        return self.req(loc='file', action='clone', params={'file_code': file_code})

    def file_direct_link(self, file_code, quality=None):
        """
        Get direct link of file(s) for selected quality.
        :param str file_code: File code, or list separated by comma
        :param str quality: Video quality if exist
        :return dict: File(s) direct link(s)
        """
        params = {'file_code': file_code}
        if quality:
            params['q'] = quality
        return self.req(loc='file', action='direct_link', params=params)

    def file_set_folder(self, file_code, folder_id):
        """
        Set file(s) folder
        :param str file_code: File code, or list separated by comma
        :param int folder_id: Folder ID
        :return dict: Set result
        """
        return self.req(loc='file', action='set_folder', params={
            'file_code': file_code,
            'fld_id': folder_id,
        })

    def folder_list(self, folder_id):
        """
        Get folders list.
        :param int folder_id: Folder ID
        :return dict: List of folders
        """
        return self.req(loc='folder', action='list', params={'fld_id': folder_id})

    def folder_create(self, parent_id, name):
        """
        Create new folder.
        :param int parent_id: Parent folder ID
        :param str name: Folder name
        :return dict: Create result
        """
        return self.req(loc='folder', action='create', params={
            'parent_id': parent_id,
            'name': name,
        })

    def folder_rename(self, folder_id, name):
        """
        Rename folder.
        :param int folder_id: Folder ID
        :param str name: Folder name
        :return dict: Rename result
        """
        return self.req(loc='folder', action='rename', params={
            'fld_id': folder_id,
            'name': name,
        })

    def files_deleted(self, limit=None):
        """
        Get last files deleted.
        :param int limit: Number of files limit
        :return dict: Get deleted files result
        """
        params = {}
        if limit:
            params['last'] = limit
        return self.req(loc='files', action='deleted', params=params)

    def files_dmca(self, limit=None):
        """
        Get files schedules for DMCA delete.
        :param int limit: Number of files limit
        :return dict: Get DMCA files result
        """
        params = {}
        if limit:
            params['last'] = limit
        return self.req(loc='files', action='dmca', params=params)
