import pyqrcode
from uuid import uuid4

class QRCodeGeneratorService:
    def __init__(self):
        self.filename = f'{uuid4().hex}.png'

    def generateQRCode(self, filename, datatoencode, scalenumber):
        return self.generateData(filename, datatoencode, scalenumber)

    def lookUpQRCode(self, filename):
        return self.lookUpData(filename)

    def generateData(self, filename, datatoencode, scalenumber):
        code_response = None
        if filename is not None and scalenumber is not None:
            qrcode = pyqrcode.create(datatoencode)
            filenamedata = f'{filename}.png'
            qrcode.png(filenamedata, scale=scalenumber)
            code_response = replacedFileData(fileData)
            return code_response
        else:
            qrcode = pyqrcode.create(datatoencode)
            qrcode.png(self.filename, scale=scalenumber)
            code_response = replacedFileData(self.filename)
            return code_response

    def lookUpData(self, filename):
        filenamedata = None
        if filename is not None:
            filenamedata = f'{filename}.png'
            with open(filenamedata, 'rb') as f:
                content = f.read()
                return content
        return None

    def replacedFileData(self, fileData):
        return fileData.replace('.png', '')

# qrcodeGenerateService = QRCodeGeneratorService()
# filenamedata = qrcodeGenerateService.generateQRCode("qrcodedata", "f65acbb5e937426a9c403b1c97d6f287", 8)
# datalookup = qrcodeGenerateService.lookUpQRCode(filenamedata)
# print(filenamedata)
