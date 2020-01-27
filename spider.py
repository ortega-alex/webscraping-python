# import bs4 import BeautifulSoup
# import requests

# html_dic = requests.get('https://servicios.igssgt.org/Servicios/Afiliados/ConsultaContribuciones.aspx')




import requests
from bs4 import BeautifulSoup

with requests.Session() as c:
    url = "https://servicios.igssgt.org/Servicios/Afiliados/ConsultaContribuciones.aspx"
    c.get(url)
    _data = dict(txtNumAfiliado='22710239801011',ddlDocumentos='DPI',ddlOrdenCedula='A01',txtDocumento='22710239801011',btnConsultar='Consultar')
    c.post(url,data=_data,headers={"Referer":"https://servicios.igssgt.org/Servicios/Afiliados/ConsultaContribuciones.aspx"})
    page = c.get('https://servicios.igssgt.org/Servicios/Afiliados/ConsultaContribuciones.aspx')
    # print(page.content)
    
# print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

# print(soup.find_all(id='ctl00_content_lblNombreAfiliado'))


# print(soup.find_all('table'))
# print(soup.find_all(class_='datos'))