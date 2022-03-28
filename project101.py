import os
import dropbox
from dropbox.files import WriteModedw

class Upload :
    def __init__(self , accessToken) :
        self.accessToken = accessToken

    def uploadFile(self , source , destination):

        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(source):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, source)
                dropbox_path = os.path.join(destination, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


        with open(source , 'rb') as f:
            dbx.files_upload(f.read() , destination)



def main():
    accessToken = "sl.BEoWRmdCBFVENb5s7nhHazq-JwfJbC1e19b-ZkNfprcj5MradfwnwKE06IAeNhpnyBsCUbpVsvJAU5sYarz6lS2ZC5x3ZQaiDiP7ra-BPzUOycYyI8uQ3DuzmWwDRJasmtanY12vRrVR"

    obj = Upload(access_token)

    source = str(input("Enter the folder path to transfer : -"))
    destination = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

  
    obj.uploadFile(source,destination)
    print("file has been moved !!!")

main()