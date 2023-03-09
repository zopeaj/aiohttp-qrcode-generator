import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.core.business.abstracts.QRCodeGeneratorService import QRCodeGeneratorService
from aiohttp.web import RouteTableDef, Response, StreamResponse

qrcodeGenroutes = RouteTableDef()
qrcodeGeneratorService = QRCodeGeneratorService()

@qrcodeGenroutes.post("/generateqrcode/")
async def postDatatoGenerateQRCode(request):
    data = await request.json()
    filename = data['filename']
    datatoencode = data["datatoencode"]
    scale = data["scale"]
    if filename is not None:
        filenamedata = qrcodeGeneratorService.generateQRCode(filename, datatoencode, scale)
        return Response(text=filenamedata, status=201)
    filetext = qrcodeGeneratorService.generateQRCode(None, datatoencode, scale)
    return Response(text=filetext, status=201)

@qrcodeGenroutes.get("/generateqrcode/{filename}")
def getDatalookQRCode(request):
    filename = request.match_info.get("filename")
    if filename is not None:
        content = qrcodeGeneratorService.lookUpQRCode(filename)
        return Response(body=content, status=200, content_type='image/png')
    return Response(body={"detail": "qrcode unable to be generated"}, status=400)


@qrcodeGenroutes.get("/generateqrcode/")
def generateDataCodes(request):
    datatoencode = request.query.get("datatoencode")
    scale = request.query.get('scale')
    filename = request.query.get("filename")
    if filename is not None:
        filenamedata = qrcodeGeneratorService.generateQRCode(filename, datatoencode, scale)
        content = qrcodeGeneratorService.lookUpQRCode(filenamedata)
        return Response(body=content, status=200, content_type='image/png')

    filedata = qrcodeGeneratorService.generateQRCode(None, datatoencode, scale)
    content = qrcodeGeneratorService.lookUpQRCode(filedata)
    return Response(body=content, status=200, content_type='image/png')



# /generateqrcode/?datatoencode=f65acbb5e937426a9c403b1c97d6f287&scale=8
