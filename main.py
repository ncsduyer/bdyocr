import os

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16603462'
API_KEY = '22VkcS3vIXuMeGDEM6PlwwHa'
SECRET_KEY = '2ap2Drbuew5tV3aAXGPkSQC7bODDPujC'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def getTxt(path):
    image = get_file_content(os.path.join(root, path))
    """ 调用通用文字识别（高精度版） """
    objs = client.basicAccurate(image)
    # print(objs)
    if "words_result" in objs:
        with open(textpath+'/'+path+ '.txt', 'w', encoding='utf-8') as f:
            for obj in objs['words_result']:
                # print(obj)
                for k,v in obj.items():
                    # print(v)
                    f.write(v+'\n')
path=os.path.abspath('.')
textpath=path+'/txts'
if not os.path.exists(textpath):
    os.makedirs(textpath)

for root,dirs,files in os.walk(path):
    for name in files:
        if name.endswith('.jpg'):
            print(name)
            try:
                getTxt(name)
            except Exception as e:
                continue

print('输出完成')

# """ 如果有可选参数 """
# options = {}
# options["detect_direction"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别（高精度版） """
# client.basicAccurate(image, options)