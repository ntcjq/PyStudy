import json


def transfer():
    str = "{pool_key='FC100000133316077', sub_id=1000127710293959, call_id='0b6504079d077b14', phone_no='182****2019', secret_no='170****1921', peer_no='189****7726', called_display_no='170****1921', call_type=0, call_time='2023-09-15 15:28:29', start_time='2023-09-15 15:28:38', call_out_time='2023-09-15 15:28:29', ring_time='2023-09-15 15:28:30', free_ring_time='2023-09-15 15:28:33', release_time='2023-09-15 15:30:00', sms_number=null, release_dir=2, out_id='d0ddd0f6518440edaa56548d2a2550e3', unconnected_cause=0, release_cause=16}"
    str = str.replace("{", "")
    str = str.replace("}", "")
    arr = str.split(",")
    jsonStr = "{"
    for temp in arr:
        kvArr = temp.split("=")
        key = kvArr[0].strip() #去除两侧空格
        value = kvArr[1].strip()
        jsonStr += "\"" + key + "\":"
        jsonStr += value + ","
    jsonStr = jsonStr[0:len(jsonStr) - 1]
    jsonStr += "}"
    jsonStr = jsonStr.replace("\'", "\"")
    print(jsonStr)


if __name__ == "__main__":
    transfer()
