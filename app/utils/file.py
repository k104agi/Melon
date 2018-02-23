import magic
import requests
from io import BytesIO


def download(url):
    # url에서 파일을 다운받아서 해당 파일의 확장자를 알아낸 후
    # (주어진 file_name과 확장자를 합친 파일명, 임시로 생성된 BytesIO 개체)
    # 위 튜플을 리턴
    response = requests.get(url)
    binary_data = response.content
    temp_file = BytesIO()
    temp_file.write(binary_data)
    temp_file.seek(0)
    return temp_file

def get_buffer_ext(buffer):
    buffer.seek(0)
    mime_info = magic.from_buffer(buffer.read(), mime=True)
    buffer.seek(0)
    return mime_info.split('/')[-1]

    # url = artist.url_img_cover
    #
    # params = {
    #     'file_name': file_name,
    # }
    # response = requests.get(url, params)
    # source = response.text
    # soup = BeautifulSoup(source, 'lxml')
    # info = soup.select_one('.wrap_atist_info')
    # src = soup.select_one('.wrap_dtl_atist .wrap_thumb #artistImgArea img').get('src')
    #
    # temp_file.seek(0)
    # mime_type = magic.from_buffer(temp_file.read(), mime=True)
    # file_name = '{artist_id}.{ext}'.format(
    #     artist_id=artist_id,
    #     ext=mime_type.split('/')[-1],
    # )
    #
    # name1 = str(file_name,확장자)
    # tuple1 = (name1, BytesIO Object)
    # return tuple1