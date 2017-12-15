# -*- coding: utf-8 -*-


import re # mac adreslerini bulmak için
from time import sleep # kontrolü saniyede 1 yapmak için
import notify2 # masaüstü bildirimleri için

isnotified = False
while(not sleep(5)): #bu döngü programın sonsuza dek çalışmasını sağlar, her döngü içinde 5 sn bekler
    arp_file = open("/proc/net/arp") # arp tablosu burada bulunuyor
    arp_out = arp_file.read()
    macs_out = re.findall(r"((\w{2,2}\:{0,1}){6})",arp_out) # arp dosyası içindeki mac adresleri ayrıştırılıyor
    macs = []
    for mac_out in macs_out:
        macs.append(mac_out[0]) # sadece mac adreslerinin bulunduğu dizi elde ediliyor
    for mac in macs: # herbir mac adresinin dizide bir kopyası olup olmadığına bakılıyor
        macs_womac = macs[:] # (macs without this mac) şu anda olup olmadığına bakılan mac adresinin bulunmadığı dizi
        macs_womac[macs.index(mac)] = ""
        if(mac in macs_womac): # eğer mac adresinin kopyası varsa ARP zehirleme vardır.
            print("ARP ZEHİRLEME")
            if not isnotified: # eğer daha önce bu konu hakkında bildirim gönderilmemişse bildirim gönder
                notify2.init('foo')
                n = notify2.Notification('Güvenlik Tehdidi', 'Ağınızda ARP zehirleme girişimi tespit edildi.')

                n.show()
                isnotified = True
            else:
                isnotified = False
            break
    print(macs) # mac adreslerini yazdırır