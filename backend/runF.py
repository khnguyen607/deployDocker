import aiohttp
import asyncio
import json
import time
count = 0
def login(tk,mk):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-images")
    options.add_argument("--disable-plugins")

    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    url = 'https://authorization.product.cloudhms.io/authorize?connection=prod-vinpearl&audience=https%3A%2F%2Fpremium-api.product.cloudhms.io&client_id=sVXK0EVKo9fUQOcGk1f8hDdW2ykyUR1F&redirect_uri=https%3A%2F%2Fportal-booking.product.cloudhms.io%2Flogin%2Fcallback&scope=openid%20profile%20email%20offline_access&response_type=code&response_mode=query&state=MHlEMUpYYzViMkgwbFl6Yk14VDdoZ0J4ZzJuT20uZjhpLVduajdLakJuSQ%3D%3D&nonce=RkFJRUlDZmFTMDJDMGEtdVVXY01scnNYZXVaSX5XWXU4NmRaUFlJb3k5aw%3D%3D&code_challenge=pHi5YNSRG7-laBLFACSV1tea5_yS5iIXIRPCRxs9EcY&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtcmVhY3QiLCJ2ZXJzaW9uIjoiMS4yLjAifQ%3D%3D'
    driver = webdriver.Chrome(options=options)  # Đảm bảo bạn đã cài đặt Chrome driver
    # Mở trang web
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    try:
        # Đăng nhập tài khoản
        driver.find_element("id", "username").send_keys(tk)
        driver.find_element("id", "password").send_keys(mk)
        driver.find_element("xpath", "/html/body/div/main/section/div/div/div/form/div[2]/button").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'form-control')]"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "react-autowhatever-1--item-0"))).click()
        driver.find_element(By.XPATH, "//span[text()='Search']").click()
        time.sleep(1)

        logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]

        # Tìm giá trị "authorization" trong tệp JSON
        for row in logs:
            try: 
                authorization_value=row['params']['request']['headers']['authorization']
                break
            except:
                continue
        
        for row in logs:
            try: 
                distributionChannelId = json.loads(row['params']['request']['postData'])['distributionChannelId']
                break
            except:
                continue
        
        def changedata(key1,value1,key2,value2):
            with open("data.json", "r") as json_file:
                loaded_data = json.load(json_file)
            loaded_data[key1] = value1
            loaded_data[key2] = value2
            with open("data.json", "w") as json_file:
                json.dump(loaded_data, json_file, indent=4)
        
        changedata("authorization",authorization_value,"distributionChannelId",distributionChannelId)
        return authorization_value
    except:
        print("Đã đăng nhập")
        return -1

class PriceRoom:
    def __init__(self, arrivalDate, departureDate, hotelName, distributionChannelId, authorization, adult, child):
        # khai báo biến 
        self.arrivalDate = arrivalDate 
        self.departureDate = departureDate
        self.distributionChannelId = distributionChannelId
        self.adult = adult
        self.child = child
        self.authorization = authorization
        self.propertyCode, self.propertyID = self.getID(hotelName)
        
        self.OBJ_Data = []
    def getID(self, name):
        global propertyCode, propertyID, arrivalDate, departureDate
        typeVilla={
        "Vinpearl Beachfront Nha Trang" : {
            "propertyCode"  :   "VPCOBFNT",
            "propertyID"    :   "24386cea-907e-93d5-0755-b4b1d8f5858a"
        },

        "Vinpearl Resort & Golf Nam Hội An" : {
            "propertyCode"  :   "VPNHARG",
            "propertyID"    :   "2c2389a5-947f-4dc9-79fc-6d7d6b7521bb"
        },

        "Vinpearl Wonderworld Phú Quốc" : {
            "propertyCode"  :   "VPDS1PQ",
            "propertyID"    :   "f89849e9-0a10-17c0-16e7-7abaa8f06808"
        },

        "Vinpearl Sealink Nha Trang" : {
            "propertyCode"  :   "VPLGLRV",
            "propertyID"    :   "340e8b59-4b88-9b69-5283-9922b91c6236"
        },

        "Vinpearl Resort & Spa Phú Quốc" : {
            "propertyCode"  :   "VPQR",
            "propertyID"    :   "bb871f8a-9159-a65b-a2cd-f39a19030afa"
        },

        "Vinpearl Resort & Spa Nha Trang Bay" : {
            "propertyCode"  :   "VPLNTRV",
            "propertyID"    :   "8ad87144-51ba-24bc-5d79-6aa98dd275ab"
        },

        "Vinpearl Resort Nha Trang" : {
            "propertyCode"  :   "VPLNTR",
            "propertyID"    :   "1dc9c659-8c61-0370-20b3-1234f6664721"
        },

        "Vinpearl Luxury Nha Trang" : {
            "propertyCode"  :   "VLNT",
            "propertyID"    :   "e894baa6-4bc4-0911-4a08-2d89d2d093cb"
        },

        "Vinpearl Resort & Spa Hội An" : {
            "propertyCode"  :   "VHARV",
            "propertyID"    :   "33cc8c26-2e7e-169f-a2a9-42b03489958f"
        },

        "Vinpearl Resort & Spa Đà Nẵng" : {
            "propertyCode"  :   "VDNOCRV",
            "propertyID"    :   "3d24aff1-83f7-02be-5dae-38dc61123534"
        },

        "Vinpearl Golflink Nha Trang" : {
            "propertyCode"  :   "VPDS3NT",
            "propertyID"    :   "5ed1abc6-4b25-4e2f-8683-2396a5b3ac63"
        },

        "VinHolidays Fiesta Phú Quốc" : {
            "propertyCode"  :   "VHD1PQ",
            "propertyID"    :   "5ef5c725-d49d-4413-a9ce-3f5966906972"
        },

        "Vinpearl Resort & Spa Hạ Long" : {
            "propertyCode"  :   "VPLHLR",
            "propertyID"    :   "9f474bc1-62f4-666b-1c63-7e7330412cfd"
        },

        "Hòn Tằm Resort" : {
            "propertyCode"  :   "HTNT",
            "propertyID"    :   "668bb33b-09b0-4d7a-a5ba-38ae1f9abf17"
        }
        }
        if name in typeVilla:
            return typeVilla[name]['propertyCode'], typeVilla[name]['propertyID']
    
    async def fetch_data(self, url, session, page):
        data = {
            "arrivalDate": self.arrivalDate,
            "departureDate": self.departureDate,
            "distributionChannelId": self.distributionChannelId,
            "limit": 100,
            "numberOfRoom": 1,
            "organizationCode": "vinpearl",
            "page": page,
            "propertyCode": self.propertyCode,
            "propertyID": self.propertyID,
            "roomOccupancy": {
                "numberOfAdult": self.adult,
                "otherOccupancies": [
                    {"otherOccupancyRefID": "child", 
                    "otherOccupancyRefCode": "child", 
                    "quantity": self.child}
                ]
            }
        }
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': self.authorization
        }

        async with session.post(url, headers=headers, json=data) as response:
            response_json = await response.json()
            if 'message' in response_json and response_json['message'] == 'Unauthorized':
                self.OBJ_Data = 'Unauthorized'
                return
            if 'data' in response_json and 'roomAvailabilityRates' in response_json['data'] and response_json['data']['roomAvailabilityRates']:
                temp = response_json['data']['roomAvailabilityRates']
                self.OBJ_Data.extend(temp)
                # print(page)
            else:
                return False

    async def main(self, key = None):
        url = 'https://premium-api.product.cloudhms.io/proxy-booking-portal/v1/get-room-availability'
        global count
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    await asyncio.wait_for(
                        asyncio.gather(*[self.fetch_data(url, session, i) for i in range(5)]),
                        timeout=5
                    )
                    if self.OBJ_Data == 'Unauthorized':
                        return 'Unauthorized'
                    count +=1
                    print(count)
                    
                    result = {}
                    for room in self.OBJ_Data:
                        try:
                            if any(room["ratePlan"]["rateCode"].endswith(suffix) for suffix in ('KM', 'KR', 'CM', 'CH', 'JP')):
                                continue
                            result.setdefault(room['roomType']['roomTypeName'], {}).setdefault(room["ratePlan"]["rateCode"], {})['Price'] = int(float(room['averageAmount']['amount'])/1000)
                        except:
                            result[room['roomType']['roomTypeName']] = False
                    if(key):
                        result['key'] = key

                    # Xóa dấu cách thừa từ các khóa trong từ điển
                    for key in list(result.keys()):
                        cleaned_key = key.strip()
                        result[cleaned_key] = result.pop(key)
                    return result

                    # break
                except asyncio.TimeoutError:
                    print("Thực hiện lại vì quá thời gian tối đa")

class Surchange:
    def __init__(self, data):
        self.data = data

    # nhóm các pack vào loại tương ứng 
    def GroupPack(self):
        data = self.data
        for room in data:
            # khởi tạo các gói
            b= {
                "RO" : {},
                "BB" : {},
                "HL" : {},
                "HD" : {},
                "BV/BX" : {},
                "HB" : {},
                "FB" : {},
                "FV/FX" : {}
            }

            # nhóm các gói tương ứng 
            for pack in data[room]:
                if ("KM" in pack) or ("KR" in pack) or ("CM" in pack) or ("CH" in pack):
                    continue
                if ("BB" in pack) and ("FBB" not in pack) and ("FBBR" not in pack) and ("HBBR" not in pack):
                    b['BB'][pack] = data[room][pack]
                elif "HL" in pack:
                    b['HL'][pack] = data[room][pack] 
                elif "HD" in pack:
                    b['HD'][pack] = data[room][pack] 
                elif "BV" in pack or "BX" in pack :
                    b['BV/BX'][pack] = data[room][pack]
                elif "FB" in pack:
                    b['FB'][pack] = data[room][pack] 
                elif "FV" in pack or "FX" in pack:
                    b['FV/FX'][pack] = data[room][pack] 
                elif "HB" in pack and "HBRO" not in pack:
                    b['HB'][pack] = data[room][pack] 
                elif "RO" in pack:
                    b['RO'][pack] = data[room][pack]
            
            # xóa gói k cần thiết
            delkey = []
            for key in b:
                if not b[key]:
                    delkey.append(key)
            for delete in delkey:
                del b[delete]
            data[room] = b.copy()  
        return data
    
    # thêm hoa hồng cho các gói
    def calcProfit(self):
        # tính lãi
        def tipPack(room, pack):
            with open('data.json', 'r') as file:
                tip = json.load(file)
            # tính lãi theo loại phòng
            def tipRoom(room): 
                if "Villa 2" in room or ("Family" in room and "Villa" not in room) or "2-" in room or "Quadruple" in room: 
                    return int(tip['Villa 2'])
                elif "Villa 3" in room:
                    return int(tip["Villa 3"])
                elif "Villa 4" in room:
                    return int(tip["Villa 4"])
                elif "Villa 5" in room:
                    return int(tip["Villa 5"])
                else:
                    return int(tip["other"])

            subscript = {
                "DO"    : 0.9,
                "D07"   : 0.93, 
                "D10"   : 0.9,
                "D12"   : 0.875,
                "D15"   : 0.85
            }

            sur = {
                "DO"    : 'surddo',
                "D07"   : 'surd7', 
                "D10"   : 'surddo',
                "D12"   : 'surd12',
                "D15"   : 'surd15'
            }
            for sub in subscript:
                if pack.endswith(sub):
                    if sub == "D10":
                        sub = "DO"
                    t = tip[sub].split('++')
                    if '++' in tip[sub]:
                        data[room][pack]['Price'] = data[room][pack]['Price']/subscript[sub]*float(t[0]) + float(t[1])
                    else:
                        data[room][pack]['Price'] = data[room][pack]['Price']/subscript[sub]*float(t[0]) + tipRoom(room)
                    # data[room][pack]['adult'] = data[room][pack]['adult']/subscript[sub]*float(tip[sur[sub]])
                    # data[room][pack]['child'] = data[room][pack]['child']/subscript[sub]*float(tip[sur[sub]])

                    data[room][pack]['Price'] = int(data[room][pack]['Price'])
                    # data[room][pack]['adult'] = int(data[room][pack]['adult'])
                    # data[room][pack]['child'] = int(data[room][pack]['child'])
                    return
            data[room][pack]['Price'] += tipRoom(room)

        data = self.data
        for room in data:
            for pack in data[room]:
                tipPack(room, pack)
        return data
    
def runF(datein, dateout, hotel):
    # đọc và gán dữ liệu cho phần xác thực ng dùng
    with open('data.json', 'r') as file:
        data = json.load(file)
    authorization = data['authorization']
    distributionChannelId = data['distributionChannelId']

    base = {}
    # hàm tính hiệu 2 json 
    def subtract(a, b, key):
        for room in a:
            for pack in a[room]:
                if pack in b[room]:
                    b[room][pack][key] = a[room][pack]['Price'] - b[room][pack]['Price']
        return b

    async def fetch():
        nonlocal base
        surchange = {
            'adult' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 3, 0),
            'child' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 2, 1),

            # 'adult2' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 4, 0),
            # 'adult2-' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 5, 0),
            # 'child2' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 4, 0),
            # 'child2-' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 4, 1),
            # 'child3' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 6, 0),
            # 'child3-' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 6, 1),
            # 'child4' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 8, 0),
            # 'child4-' : PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 8, 1)
        }

        # if hotel == 'Vinpearl Beachfront Nha Trang' or hotel == 'Vinpearl Resort & Spa Hạ Long':

        # Chạy các đối tượng PriceRoom bất đồng bộ
        re = await asyncio.gather(*(value.main(key) for key, value in surchange.items()))
        for sur in re:
            if 'key' not in sur:
                continue

            # các loại phòng thường 
            if sur['key']=='adult' or sur['key']=='child':
                key = sur['key']
                del sur['key']
                base = subtract(sur, base, key)

            # đối với villa2 
            elif sur['key']=='child2':
                del sur['key']
                delkey = []
                for room in sur:
                    if not ("Villa 2" in room or ("Family" in room and "Villa" not in room) or "2-" in room or "Quadruple" in room): 
                        delkey.append(room)
                temp = next((obj for obj in re if obj.get("key") == "child2-"), None)
                del temp["key"]
                for delete in delkey:
                    del sur[delete]
                    del temp[delete]
                temp = subtract(temp, sur, 'child')
                for room in temp:
                    for pack in temp[room]:
                        if room in base and pack in base[room]:
                            base[room][pack]['child'] = temp[room][pack]['child']

            # đối với villa3 
            elif sur['key']=='child3':
                del sur['key']
                delkey = []
                for room in sur:
                    if "Villa 3" not in room: 
                        delkey.append(room)
                temp = next((obj for obj in re if obj.get("key") == "child3-"), None)
                del temp["key"]
                for delete in delkey:
                    del sur[delete]
                    del temp[delete]
                temp = subtract(temp, sur, 'child')
                for room in temp:
                    for pack in temp[room]:
                        if room in base and pack in base[room]:
                            base[room][pack]['child'] = temp[room][pack]['child']    
                       
            # đối với villa4
            elif sur['key']=='child4':
                del sur['key']
                delkey = []
                for room in sur:
                    if "Villa 4" not in room:
                        delkey.append(room)
                temp = next((obj for obj in re if obj.get("key") == "child4-"), None)
                del temp["key"]
                for delete in delkey:
                    del sur[delete]
                    del temp[delete]
                temp = subtract(temp, sur, 'child')
                for room in temp:
                   for pack in temp[room]:
                        if room in base and pack in base[room]:
                            base[room][pack]['child'] = temp[room][pack]['child'] 
    
        if hotel == 'Vinpearl Beachfront Nha Trang' or hotel == 'Vinpearl Resort & Spa Hạ Long':
            for sur in re:
                if 'key' not in sur:
                    continue

                # đối với phòng 5NL - 4NL
                if sur['key']=='adult2':
                    del sur['key']
                    delkey = []
                    for room in sur:
                        if room not in ['Grand 2-Bedroom Ocean View', 'Family Suite']:
                            delkey.append(room)
                    temp = next((obj for obj in re if obj.get("key") == "adult2-"), None)
                    del temp["key"]
                    for delete in delkey:
                        try:
                            del sur[delete]
                            del temp[delete]
                        except:
                            pass
                    temp = subtract(temp, sur, 'adult')
                    for room in temp:
                        for pack in temp[room]:
                            if room in base and pack in base[room]:
                                base[room][pack]['adult'] = temp[room][pack]['adult'] 

    # tính giá ban đầu
    try:
        base = asyncio.run(PriceRoom(datein, dateout, hotel, distributionChannelId, authorization, 2, 0).main())
        if base == 'Unauthorized':
            login(data['user'], data['pass'])
        if isinstance(base, dict) and not base:
            return -1
    except:
        return False
    # asyncio.run(fetch())

    base = Surchange(base).calcProfit()
    base = Surchange(base).GroupPack()

    # hàm lọc ra gói có giá nhỏ nhất
    def minkey(data):
        # Lọc ra các gói có giá lớn hơn 0
        valid_data = {k: v for k, v in data.items() if v["Price"] > 0}
        if not valid_data:
            return None  # Trả về None nếu không có gói hợp lệ
        min_price_key = min(valid_data, key=lambda k: valid_data[k]["Price"])
        result_dict = {min_price_key: valid_data[min_price_key]}
        return result_dict

    for room in base:
        for pack in base[room]:
            base[room][pack] = minkey(base[room][pack])

    def sort_room(data):
        # Chuyển dict về mảng
        arr = []
        for room in data:
            arr.append({room : data[room]})

        # sắp xếp mảng
        def sort_m(x):
            # giá
            price = x.copy()
            price = price[next(iter(price))]
            price = price[list(price)[-1]]
            price = price[next(iter(price))]['Price']

            # Định nghĩa ưu tiên sắp xếp cho giá trị thứ nhất
            room_type = {
                            'King' : 0,
                            'Double' : 1,
                            'Queen'   : 2,
                            'Twin'  : 3
                        }
            s_room = len(room_type)
            for room in room_type:
                if room in next(iter(x)):
                    s_room = room_type[room]
                    break
            return price, s_room
        arr.sort(key=sort_m)
        
        # Chuyển mảng về dict
        dic = {}
        for room in arr:
            dic[next(iter(room))] = room[next(iter(room))]
        return dic

    base = sort_room(base)
    with open('temp.json', 'w') as file:
        json.dump(base, file, indent=4)
    return base
          
# Chạy hàm main
# s = time.time()
# resultFinal = runF('2024-05-11', '2024-05-12', 'Vinpearl Resort Nha Trang')
# print(resultFinal)
# e = time.time()
# print('thời gian chạy: '+ str(e-s))