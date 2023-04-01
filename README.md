# aiohttp-qrcode-generator

### Using GET http Method to generate the qrcode canvas
Paste this to your web browser
```
http:127.0.0.1:8081/generataqrcode?datatoencode=56051e722e9b4e7fa4870d62ed050c23&scale=7
```
![qrcode-generator](https://user-images.githubusercontent.com/59841476/228797823-9fa7e359-1e26-4a65-9c65-71346fb19d1d.png)


## Using POST http Method
```
POST: http://127.0.0.1:8082/generateqrcode/
```
## Generate the response file resource made by the post method of Http Method
```
Body: 56051e722e9b4e7fa4870d62ed050c23.png
```
image-here


### Get the response file using GET Http Method
```
GET: http://127.0.0.1:8082/generateqrcode/56051e722e9b4e7fa4870d62ed050c23.png
```

## Using GET http Method to retrieve the qrcode file resource
```
GET: http://127.0.0.1:8082/generateqrcode/codefiledata.png
```
image-here
