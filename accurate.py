from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '27497952'
API_KEY = 'dVyisaZBAhaNcW2fjAMvRGAd'
SECRET_KEY = 'TpRtTdDtfjK5uwS83WPvTPg5gQcHxpsK'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取文件 """


def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()

def getwords(filePath):

    # image = get_file_content(r'.\picture\2.jpg')
    image = get_file_content(filePath)
    url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.xspic.com%2Fimg6%2F50%2F36%2F2040882_5.jpg&refer=http%3A%2F%2Fimg.xspic.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665908590&t=8803c0d17def07919224d60207dd1373"
    #pdf_file = get_file_content('文件路径')

    # 调用通用文字识别（高精度版）
    res_image = client.basicAccurate(image)
    # res_url = client.basicAccurateUrl(url)
    # res_pdf = client.basicAccuratePdf(pdf_file)
    res_image_word = res_image
    # print(res_image)
    # print(res_url)
    # print(res_pdf)

    # 如果有可选参数
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    res_image = client.basicAccurate(image, options)
    # res_url = client.basicAccurateUrl(url, options)
    # res_pdf = client.basicAccuratePdf(pdf_file, options)
    # print(res_image)
    # print(res_url)
    # print(res_pdf)

    n = len(res_image_word['words_result'])
    words = []
    for i in range(4):
        words.append((res_image_word['words_result'][i]['words']))
    return(words)