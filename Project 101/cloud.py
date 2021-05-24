import dropbox
import os

class Transferdata:

    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from ,'rb')
        dbx.files_upload(f.read(),file_to)
       

def main():
    access_token='Hbm3FY_AmqQAAAAAAAAAATY_MTR3ikw7MkpCTRUb43On7tHAOxtkScBTOSj3QWm5'
    transferdata = Transferdata(access_token)

    file_from = input("Enter The File path To bo transfered")
    file_to =  input("Enter the full path to dropbox ")

    transferdata.upload_files(file_from,file_to)

    print("File Has been moved")

main()
