import googlemaps
import json

gmaps_key = 'AIzaSyAyqKvSk2mzMnHVNvTS7Y3kXCGosGmlP1A'  
gmaps = googlemaps.Client(key=gmaps_key)

# 대학 정보가 담긴 JSON 데이터
# JSON 파일 불러오기
with open('university.json', 'r', encoding='utf-8') as file:
    universities = json.load(file)

# 새로운 대학 정보를 담을 리스트
new_universities = []

# 대학별로 정보를 가져와서 처리
for university_info in universities:
    university_name = university_info["university"]
    
    # 주소를 geocode에 전달하여 해당 주소에 대한 정보를 가져옵니다.
    geocode_result = gmaps.geocode(university_name, language='ko')

    # 결과가 있을 경우에만 처리
    if geocode_result:
        # 첫 번째 결과의 위치 정보를 가져옵니다.
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        formatted_address = geocode_result[0]['formatted_address']

        # 새로운 대학 정보를 리스트에 추가
        new_universities.append({
            "university": university_name,
            "lat": latitude,
            "lng": longitude,
            "location": formatted_address
        })

# 새로운 대학 정보를 JSON 파일에 저장
with open("uni_map_data.json", "w", encoding="utf-8") as f:
    json.dump(new_universities, f, ensure_ascii=False, indent=4)