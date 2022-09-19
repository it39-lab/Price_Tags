from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


def download_products_file():

    file_list = drive.ListFile(
        {'q': "'root' in parents and trashed=false"}).GetList()

    for file in file_list:
        if file['title'] == "Products":
            file.GetContentFile(
                filename=file['title'] + '.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


            # mimetypes = {
            #     'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            # }
            # download_mimetype = None
            # if file['mimeType'] in mimetypes:
            #     download_mimetype = mimetypes[file['mimeType']]
            # file.GetContentFile(file['title'], mimetype=download_mimetype)
download_products_file()
