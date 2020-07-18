#Author:    Zeyad Azima "Cyber-Atom"
#Github:    https://github.com/Cyber-Atom
#Facebook:  https://www.facebook.com/elkingzeyad.azeem
#Website:   https://cyberatom.org/

import requests,json,colored,time,shodan
from optparse import *
from colored import stylize
from bs4 import BeautifulSoup

logo = """

███╗   ██╗███████╗███████╗██████╗       ██╗██████╗ 
████╗  ██║██╔════╝██╔════╝██╔══██╗      ██║██╔══██╗
██╔██╗ ██║█████╗  █████╗  ██║  ██║█████╗██║██████╔╝
██║╚██╗██║██╔══╝  ██╔══╝  ██║  ██║╚════╝██║██╔═══╝ 
██║ ╚████║███████╗███████╗██████╔╝      ██║██║     
╚═╝  ╚═══╝╚══════╝╚══════╝╚═════╝       ╚═╝╚═╝     
                                                   
                    @ZeyadAzima
"""
def Start():
    choose = OptionParser()
    choose.add_option("-s","--search",dest="search",help="Version or device you want to search for")
    return choose.parse_args()


def Censys(Search):
    pages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    cookies = {'__cfduid':'d7efc15d0aa28b3fd4a4d0dad221032871594688372','_ga':'GA1.2.1914203087.1594688377','__hstc':'149053801.5c64348de56d85aa300f7c53eed03507.1594688377991.1594937353752.1594945271371.6','hubspotutk':'5c64348de56d85aa300f7c53eed03507','_gid':'GA1.2.683185275.1594853893',
               'censys.io.beaker.session.id':'ec8f0373c9cf783e4c246e17e8173d71c8861778LKHghwZiBM+s0VG3UJB33b99zzaJR2OqSCCBKE8uaJN7UoVtp3oDqj0VyefPmo8JxlXEGLtDH9APj5fckJzhrjNNRBmaeH7yMXFGrextWDD46PE+HCfzqCSwoIu0lIuT9df1ttLfu8xpOuV1Cb8KSlAaat0l9Z605ljTz0YSBJmgEMZB9UAGFyMElWN2Kw28+m+rXDSkkceog3NaK0SUpgSBrPd8R2BSXBu/blo8TuaFCuQ0OXUfIhWXMC9b0fbKz7Jn0Gu8xucX2f8JAgeDpIERddO6CyZN2so=','ajs_user_id':'%2299e108a0cc844ce39a067a351efa6f4e%22','ajs_anonymous_id':'%2224bdfbc2-4afd-4ad4-a931-020350f2bf14%22','__hssrc':'1',
               'auth_tkt':'ba5e5571a906860fea02c253b803eed733edff95e65eabec0af317d04f5def874095fafd232ae95841628dcbc0f3ef21e0317cb9920ded238261dced9e3bb1375f10eecdbmVjYW4yNDEyMg%3D%3D!userid_type:b64unicode','CENSYS-INTERNAL-JWT':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTUwMTAwMjksImNzcmZfdG9rZW4iOiI5MTIwM2NiMi1kZDA4LTQzODgtYWFhNS1hNjIxODQ5NGNjMDUiLCJncm91cHMiOlsic2VhcmNoIl0sInRlYW1fdXVpZCI6ImY4NWE2MDdkMDM4NTQ2YTdhMjA4YjA5MzdlZWY5YWZjIiwidXNlcl91dWlkIjoiOTllMTA4YTBjYzg0NGNlMzlhMDY3YTM1MWVmYTZmNGUiLCJ0ZWFtX25hbWUiOiJhemltYSAoQXppbWEpIiwidXNlcl9uYW1lIjoiQXppbWEifQ.frA97C7yhrkSJqXwJwxOptfa5TrRdUbPme3jjvmhGfc','X-CSRF':'91203cb2-dd08-4388-aaa5-a6218494cc05','__hssc':'149053801.1.1594945271371',}
    for res in pages:
        url = f'https://censys.io/ipv4/_search?q=80.http.get.title%3A+{Search}&page={res}'
        r = requests.get(url, headers=header, cookies=cookies)
        result = r.text
        soup = BeautifulSoup(result,'lxml')
        azi = soup.find_all('span',{'class':'dns'})
        for i in azi:
            print(stylize(i.get('id'),colored.fg('red')))


def Shodan(Search):
    SHODAN_API_KEY = "O5OelZdRUzWPUebMCkZfskqkRmwcQHML"
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        results = api.search(Search)
        for result in results['matches']:
            print(stylize(result['ip_str'],colored.fg('red')))
    except shodan.APIError as e:
        print('Error: {}'.format(e))

def ZoomEye(Search):
    pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
          'Accept': 'application/json, text/plain, */*',
          'Cube-Authorization': ''}
    cookies = {'__cdnuid_s': '4ac1995ba3c870f5ddeb699fde659f70',
           'Hm_lvt_3c8266fabffc08ed4774a252adcb9263': '1594777869,1594832173,1594935867,1594937361',
           '__cdn_clearance': '1595030413.613|0|7dlsp1KyQ66MYJ3g2O%2BVjMCSelU%3D','Hm_lpvt_3c8266fabffc08ed4774a252adcb9263':'1595030073'}

    for p in pages:
        r = requests.get(f'https://www.zoomeye.org/search?q={Search}&p={p}', headers=header, cookies=cookies, verify=True)
        res = r.text

        f = open('data.json', 'w+')
        f.write(res)
        f.close()
        with open('data.json', 'r+') as lst:
            azima = json.load(lst)

            for ip in azima['matches']:
                print(stylize(ip['ip'], colored.fg('red')))

print(stylize(logo,colored.fg('red')))


(options, arguments) = Start()

try:
    print(stylize(f"""[+] Search for: {options.search}\n[+] Searching in Shodan...\n[+] Searching in Censys.....\n[+] Searching in Zoomeye.......""",colored.fg('red')))
    print(stylize("--------------------------------------------------------------------",colored.fg("red")))
    time.sleep(10)
    Censys(options.search)
    time.sleep(5)
    Shodan(options.search)
    time.sleep(5)
    ZoomEye(options.search)
    print(stylize("--------------------------------------------------------------------", colored.fg("red")))
    print(stylize("[+] Search Done",colored.fg('red')))
except Exception as e:
    print(e)
    print(stylize("""[-] Please specify Search
    ex: python3 Need-IP.py Device type or version""", colored.fg('blue')))

