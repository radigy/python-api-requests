import requests
import datetime
import json

# base url
base_url = "https://gorest.co.in/"

# auth for 90min
auth_token = "Bearer 7b80a5caf9eece584a06f69a5dc3e9b58f95c0cfbf90dc1b214b6b12e719960e"

# create data
def generate_unique_email():
    date = datetime.datetime.now()
    unique_suffix = date.strftime("%Y-%m-%d-%H-%M-%S")
    return unique_suffix + "@automation.com"


# get request
def get_request():
    url = base_url + "public/v2/users"
    print("get url: " + url)
    headers = {"Authorization": auth_token}

    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print("--------------")


# post request
def post_request():
    url = base_url + "public/v2/users"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "miron ciasteczko",
        "email": generate_unique_email(),
        "gender": "male",
        "status": "inactive"
}

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "miron ciasteczko"
    print("json POST respone body", json_str)
    print("--------------")
    return user_id


# put request
def put_request(user_id):
    url = base_url + f"public/v2/users/{user_id}"
    print("put url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "miron ciasteczko updated name",
        "email": generate_unique_email(),
        "gender": "male",
        "status": "active"
}

    response = requests.put(url, headers=headers, json=data)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    assert json_data["id"] == user_id
    assert json_data["name"] == "miron ciasteczko updated name"
    print("json PUT response body", json_str)
    print("--------------")


# delete request
def delete_request(user_id):
    url = base_url + f"public/v2/users/{user_id}"
    print("delete url: " + url)
    headers = {"Authorization": auth_token}

    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("... user is deleted ...")


get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
