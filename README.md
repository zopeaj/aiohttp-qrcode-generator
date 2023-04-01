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
![qrcode-data](https://user-images.githubusercontent.com/59841476/229288834-a7b5974a-0b1f-41e0-b9d7-b8b03e860b17.png)

## Generate the response file resource made by the post method of Http Method
```
Body: 56051e722e9b4e7fa4870d62ed050c23.png
```
![qrcode-data](https://user-images.githubusercontent.com/59841476/229288834-a7b5974a-0b1f-41e0-b9d7-b8b03e860b17.png)

### Get the response file using GET Http Method
```
GET: http://127.0.0.1:8082/generateqrcode/56051e722e9b4e7fa4870d62ed050c23.png
```
![generated-data](https://user-images.githubusercontent.com/59841476/229289058-9dc3ffe0-ce71-4c62-b31d-47d7d82ce599.png)

## Using GET http Method to retrieve the qrcode file resource
```
GET: http://127.0.0.1:8082/generateqrcode/codefiledata.png
```
