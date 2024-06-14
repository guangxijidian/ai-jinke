from aip import AipSpeech
import recoder

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
wavfile = "./test.wav"
recoder.rec(wavfile, 3)
result = client.asr(get_file_content("test.wav"),'wav',16000,{'dev_pid':1537,})
print(result["result"][0])


