import os
os.system("nmap -A -p80 --script http-xssed.nse howtoforge.com testphp.vulnweb.com -oX emircanErgin.xml")


#TARATMADA AÇIKLAMALAR
#Sitede cloudflare tespiti yaptım
#HTTP Metodlarınan hata ve normal mesaj dönüşlerini gördük
#Sayfanın headerları hakkında bilgiler aldık
#-A parametresi Full Detail Scan yapar



#KAYNAK OLARAK KULLANDIGIM SAYFA ADRESI : https://nmap.org/nsedoc/scripts/http-xssed.html
#AÇIKLAMA İÇERİĞİ VE ORNEK KULLANIMI

#This script will search the xssed.com database and it will output any
#results. xssed.com is the largest online archive of XSS vulnerable
#websites.

#PORT   STATE SERVICE REASON
#80/tcp open  http    syn-ack
#| http-xssed:
#|   xssed.com found the following previously reported XSS vulnerabilities marked as unfixed:
#|
#|     /redirect/links.aspx?page=http://xssed.com
#|
#|     /derefer.php?url=http://xssed.com/
#|
#|   xssed.com found the following previously reported XSS vulnerabilities marked as fixed:
#|
#|_    /myBook/myregion.php?targetUrl=javascript:alert(1);

#TARATMADA AÇIKLAMALAR
#Sitede cloudflare tespiti yaptım
#HTTP Metodlarınan hata ve normal mesaj dönüşlerini gördük
#Sayfanın headerları hakkında bilgiler aldık