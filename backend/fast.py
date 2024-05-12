from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, time, json

class MyItem(BaseModel):
    ks:str 
    date:str

class Data(BaseModel):
     token: str

     user: str
     pwd: str
     c_user: str
     c_pwd: str
     villa2: str
     villa3: str
     villa4: str
     villa5: str
     diff: str
     ddo: str
     d7: str
     d12: str
     d15: str
     surddo: str
     surd7: str
     surd12: str
     surd15: str
     ads: str

class Account(BaseModel):
    user:str 
    password:str

class AccountAdmin(BaseModel):
    user:str 
    password:str
    token:str

def check__token(token):
    from hashpass import check_password
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return check_password(token, data['accountAdmin']['password'].encode('utf-8'))

app = FastAPI()

# Đặt cấu hình CORS cho phép yêu cầu từ tất cả các nguồn
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def home():
    return "API by https://m.me/khnguyen.607"

@app.get("/getads")
async def getads():   
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['ads']

@app.post("/submit")
def submit(item: MyItem):
    from run import run
    ks = str(item.ks)
    date = str(item.date)
   
    # Tách dữ liệu thành các phần bằng dấu '-' làm điểm chia
    date_parts = date.split(" - ")

    # Lấy phần đầu tiên làm datein và phần thứ hai làm dateout
    datein = date_parts[0]
    dateout = date_parts[1]

    try:
        start_time = time.time()
        result = run(datein,dateout,ks)
        print(result)
        end_time = time.time()
        print(f"Thời gian trả kết quả {end_time-start_time} giây")
        return result
    except:
        return []
    
@app.post("/submitF")
def submit(item: MyItem):
    from runF import runF
    ks = str(item.ks)
    date = str(item.date)
   
    # Tách dữ liệu thành các phần bằng dấu '-' làm điểm chia
    date_parts = date.split(" - ")

    # Lấy phần đầu tiên làm datein và phần thứ hai làm dateout
    datein = date_parts[0]
    dateout = date_parts[1]

    try:
        start_time = time.time()
        result = runF(datein,dateout,ks)
        print(result)
        end_time = time.time()
        print(f"Thời gian trả kết quả {end_time-start_time} giây")
        return result
    except:
        return []
    
@app.post("/checked")
async def checked(item:Account):
    user = str(item.user)
    password = str(item.password)
    with open('data.json', 'r') as file:
        data = json.load(file)
    if user == data['account']['user'] and password == data['account']['password']:
        return 1
    else:
        return 0

# KHU VỰC CHO QUẢN TRỊ VIÊN 
@app.post("/checkadmin")
def checkadmin(item: Account):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    user = str(item.user)
    password = str(item.password)
    check = user == data['accountAdmin']['user'] and check__token(password)
    return check

@app.post("/changeinfo")
def changeinfo(item: AccountAdmin):
    if not (check__token(item.token)):
        return False
    user = str(item.user)
    password = str(item.password)
    from hashpass import hash_password
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    data['accountAdmin']['user'] = user
    data['accountAdmin']['password'] = hash_password(password).decode('utf-8')
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    return True

@app.get("/datamain")
async def datamain(access: str =''):
    if not (check__token(access)):
        return False
    
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

@app.get("/delete")
async def delete(access: str =''):
    if not (check__token(access)):
        return False
    
    with open('data.json', 'r') as file:
        data = json.load(file)
    # Sửa dữ liệu
    data["authorization"] = ""
    # Lưu lại vào tệp
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    return "Dữ liệu đã được xóa"

@app.post("/updatemain")
async def updatemain(item: Data):
    if not check__token(str(item.token)):
        return False

    user = str(item.user)
    pwd = str(item.pwd)
    c_user = str(item.c_user)
    c_pwd = str(item.c_pwd)
    villa2 = str(item.villa2)
    villa3 = str(item.villa3)
    villa4 = str(item.villa4)
    villa5 = str(item.villa5)
    diff = str(item.diff)
    ddo = str(item.ddo)
    d7 = str(item.d7)
    d12 = str(item.d12)
    d15 = str(item.d15)
    surddo = str(item.surddo)
    surd7 = str(item.surd7)
    surd12 = str(item.surd12)
    surd15 = str(item.surd15)
    ads = str(item.ads)

    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Sửa dữ liệu
    data["user"] = user
    data["pass"] = pwd
    data["account"]["user"] = c_user
    data["account"]["password"] = c_pwd
    data["Villa 2"] = villa2
    data["Villa 3"] = villa3
    data["Villa 4"] = villa4
    data["Villa 5"] = villa5
    data["other"] = diff
    data["DO"] = ddo
    data["D07"] = d7
    data["D12"] = d12
    data["D15"] = d15
    data["surddo"] = surddo
    data["surd7"] = surd7
    data["surd12"] = surd12
    data["surd15"] = surd15
    data["ads"] = ads

    # Lưu lại vào tệp
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    return "Dữ liệu đã được sửa và lưu lại thành công."

if __name__ == "__main__":
    uvicorn.run("fast:app", host="0.0.0.0", port=8000, reload=True)


