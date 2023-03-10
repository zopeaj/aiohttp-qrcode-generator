# aiohttp-qrcode-generator


## How to use it
# POST: http://127.0.0.1:8000/generateqrcode/
# Data To Post
#  {
     "filename": "filename",
     "datatoencode": "a data to be encoded",
     "scale": "sizes between 4-8 to generate adequate size"
#  }
#
#
#
# response data with be a generated filename
# filename.png

# GET: http://127.0.0.1:8000/generateqrcode/filename.png


# Or

# GET: http://127.0.0.1:8000/generateqrcode/?filename=filename&datatoencode=f65acbb5e937426a9c403b1c97d6f287&scale=8




