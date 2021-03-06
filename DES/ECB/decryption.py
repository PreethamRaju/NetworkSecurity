from operator import xor
import random
import string
import binascii

def ip(din):
	dout = (din[57]+din[49]+din[41]+din[33]+din[25]+din[17]+din[9]+din[1]+din[59]+din[51]+din[43]+din[35]+din[27]+din[19]+din[11]+din[3]+din[61]+din[53]+din[45]+din[37]+din[29]+din[21]+din[13]+din[5]+din[63]+din[55]+din[47]+din[39]+din[31]+din[23]+din[15]+din[7]+din[56]+din[48]+din[40]+din[32]+din[24]+din[16]+din[8]+din[0]+din[58]+din[50]+din[42]+din[34]+din[26]+din[18]+din[10]+din[2]+din[60]+din[52]+din[44]+din[36]+din[28]+din[20]+din[12]+din[4]+din[62]+din[54]+din[46]+din[38]+din[30]+din[22]+din[14]+din[6]).zfill(64) 
	return dout

def invip(din):
	dout = (din[39]+din[7]+din[47]+din[15]+din[55]+din[23]+din[63]+din[31]+din[38]+din[6]+din[46]+din[14]+din[54]+din[22]+din[62]+din[30]+din[37]+din[5]+din[45]+din[13]+din[53]+din[21]+din[61]+din[29]+din[36]+din[4]+din[44]+din[12]+din[52]+din[20]+din[60]+din[28]+din[35]+din[3]+din[43]+din[11]+din[51]+din[19]+din[59]+din[27]+din[34]+din[2]+din[42]+din[10]+din[50]+din[18]+din[58]+din[26]+din[33]+din[1]+din[41]+din[9]+din[49]+din[17]+din[57]+din[25]+din[32]+din[0]+din[40]+din[8]+din[48]+din[16]+din[56]+din[24]).zfill(64)
	return dout

def shift1(lst):
	lstout = (lst[1]+lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]+lst[8]+lst[9]+lst[10]+lst[11]+lst[12]+lst[13]+lst[14]+lst[15]+lst[16]+lst[17]+lst[18]+lst[19]+lst[20]+lst[21]+lst[22]+lst[23]+lst[24]+lst[25]+lst[26]+lst[27]+lst[28]+lst[29]+lst[30]+lst[31]+lst[32]+lst[33]+lst[34]+lst[35]+lst[36]+lst[37]+lst[38]+lst[39]+lst[40]+lst[41]+lst[42]+lst[43]+lst[44]+lst[45]+lst[46]+lst[47]+lst[48]+lst[49]+lst[50]+lst[51]+lst[52]+lst[53]+lst[54]+lst[55]+lst[0]).zfill(56)
	return lstout

def shift2(lst):
	lstout = (lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]+lst[8]+lst[9]+lst[10]+lst[11]+lst[12]+lst[13]+lst[14]+lst[15]+lst[16]+lst[17]+lst[18]+lst[19]+lst[20]+lst[21]+lst[22]+lst[23]+lst[24]+lst[25]+lst[26]+lst[27]+lst[28]+lst[29]+lst[30]+lst[31]+lst[32]+lst[33]+lst[34]+lst[35]+lst[36]+lst[37]+lst[38]+lst[39]+lst[40]+lst[41]+lst[42]+lst[43]+lst[44]+lst[45]+lst[46]+lst[47]+lst[48]+lst[49]+lst[50]+lst[51]+lst[52]+lst[53]+lst[54]+lst[55]+lst[0]+lst[1]).zfill(56)
	return lstout

def pchoice2(keyin):
	pc2out = (keyin[13]+keyin[16]+keyin[10]+keyin[23]+keyin[0]+keyin[4]+keyin[2]+keyin[27]+keyin[14]+keyin[5]+keyin[20]+keyin[9]+keyin[22]+keyin[18]+keyin[11]+keyin[3]+keyin[25]+keyin[7]+keyin[15]+keyin[6]+keyin[26]+keyin[19]+keyin[12]+keyin[1]+keyin[40]+keyin[51]+keyin[30]+keyin[36]+keyin[46]+keyin[54]+keyin[29]+keyin[39]+keyin[50]+keyin[44]+keyin[32]+keyin[47]+keyin[43]+keyin[48]+keyin[38]+keyin[55]+keyin[33]+keyin[52]+keyin[45]+keyin[41]+keyin[49]+keyin[35]+keyin[28]+keyin[31]).zfill(48)
	return pc2out

def exp(din):
	dout = (din[31]+din[0]+din[1]+din[2]+din[3]+din[4]+din[3]+din[4]+din[5]+din[6]+din[7]+din[8]+din[7]+din[8]+din[9]+din[10]+din[11]+din[12]+din[11]+din[12]+din[13]+din[14]+din[15]+din[16]+din[15]+din[16]+din[17]+din[18]+din[19]+din[20]+din[19]+din[20]+din[21]+din[22]+din[23]+din[24]+din[23]+din[24]+din[25]+din[26]+din[27]+din[28]+din[27]+din[28]+din[29]+din[30]+din[31]+din[0]).zfill(48)
	return dout

def permf(din):
	dout = (din[15]+din[6]+din[19]+din[20]+din[28]+din[11]+din[27]+din[16]+din[0]+din[14]+din[22]+din[25]+din[4]+din[17]+din[30]+din[9]+din[1]+din[7]+din[23]+din[13]+din[31]+din[26]+din[2]+din[8]+din[18]+din[12]+din[29]+din[5]+din[21]+din[10]+din[3]+din[24]).zfill(32)
	return dout

sb1 = ([[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]])

sb2 = ([[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]])

sb3 = ([[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]])

sb4 = ([[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]])

sb5 = ([[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]])

sb6 = ([[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]])

sb7 = ([[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]])

sb8 = ([[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]])


def encrypt(li,ri,key):
	expand = exp(ri)
	print expand
	print k1

	expint = int(expand,2)
	k1int = int(key,2)
	print expint
	print k1int

	exor = (bin(expint^k1int)[2:]).zfill(48)

	a=int((exor[0]+exor[5]),2)
	b=int((exor[1]+exor[2]+exor[3]+exor[4]),2)

	print exor
	print a
	print b

	c=int((exor[6]+exor[11]),2)
	d=int((exor[7]+exor[8]+exor[9]+exor[10]),2)

	e=int((exor[12]+exor[17]),2)
	f=int((exor[13]+exor[14]+exor[15]+exor[16]),2)
	
	g=int((exor[18]+exor[23]),2)
	h=int((exor[19]+exor[20]+exor[21]+exor[22]),2)

	i=int((exor[24]+exor[29]),2)
	j=int((exor[25]+exor[26]+exor[27]+exor[28]),2)

	k=int((exor[30]+exor[35]),2)
	l=int((exor[31]+exor[32]+exor[33]+exor[34]),2)

	m=int((exor[36]+exor[41]),2)
	n=int((exor[37]+exor[38]+exor[39]+exor[40]),2)

	o=int((exor[42]+exor[47]),2)
	p=int((exor[43]+exor[44]+exor[45]+exor[46]),2)

	s1 = (bin(sb1[a][b]))[2:].zfill(4)
	s2 = (bin(sb2[c][d]))[2:].zfill(4) 
	s3 = (bin(sb3[e][f]))[2:].zfill(4) 
	s4 = (bin(sb4[g][h]))[2:].zfill(4)
	s5 = (bin(sb5[i][j]))[2:].zfill(4)
	s6 = (bin(sb6[k][l]))[2:].zfill(4)
	s7 = (bin(sb7[m][n]))[2:].zfill(4)
	s8 = (bin(sb8[o][p]))[2:].zfill(4)

	print s1
	print s2
	print s3
	print s4
	print s5
	print s6
	print s7
	print s8

	print (s1+s2+s3+s4+s5+s6+s7+s8)

	permin = permf(s1+s2+s3+s4+s5+s6+s7+s8)

	print permin

	lint = int(li,2)
	permint = int(permin,2)

	rx = ri
	ri = (bin(lint^permint)[2:]).zfill(32)
	li = rx

	print li
	print ri
	return(li,ri)


terminate = 0
keybin = '1101000101010011110101111101110000011101101100011110011000110010'

lst1 = list(keybin)
pchoice1 = (keybin[56]+keybin[48]+keybin[40]+keybin[32]+keybin[24]+keybin[16]+keybin[8]+keybin[0]+keybin[57]+keybin[49]+keybin[41]+keybin[33]+keybin[25]+keybin[17]+keybin[9]+keybin[1]+keybin[58]+keybin[50]+keybin[42]+keybin[34]+keybin[26]+keybin[18]+keybin[10]+keybin[2]+keybin[59]+keybin[51]+keybin[43]+keybin[35]+keybin[62]+keybin[54]+keybin[46]+keybin[38]+keybin[30]+keybin[22]+keybin[14]+keybin[6]+keybin[61]+keybin[53]+keybin[45]+keybin[37]+keybin[29]+keybin[21]+keybin[13]+keybin[5]+keybin[60]+keybin[52]+keybin[44]+keybin[36]+keybin[28]+keybin[20]+keybin[12]+keybin[4]+keybin[27]+keybin[19]+keybin[11]+keybin[3]).zfill(56)
print 'pc1=',pchoice1

pchoice1 = list(pchoice1)
lcs1 = shift1(pchoice1)
print 'lcs1= ',lcs1
k1 = pchoice2(lcs1)
print 'k1= ',k1
lcs2 = shift1(lcs1)
print 'lcs2= ',lcs2
k2 = pchoice2(lcs2)
print 'k2= ',k2
lcs3 = shift2(lcs2)
print 'lcs3= ',lcs3
k3 = pchoice2(lcs3)
print 'k3= ',k3
lcs4 = shift2(lcs3)
print 'lcs4= ',lcs4
k4 = pchoice2(lcs4)
print 'k4= ',k4
lcs5 = shift2(lcs4)
print 'lcs5= ',lcs5
k5 = pchoice2(lcs5)
print 'k5= ',k5
lcs6 = shift2(lcs5)
print 'lcs6= ',lcs6
k6 = pchoice2(lcs6)
print 'k6= ',k6
lcs7 = shift2(lcs6)
print 'lcs7= ',lcs7
k7 = pchoice2(lcs7)
print 'k7= ',k7
lcs8 = shift2(lcs7)
print 'lcs8= ',lcs8
k8 = pchoice2(lcs8)
print 'k8= ',k8
lcs9 = shift1(lcs8)
print 'lcs9= ',lcs9
k9 = pchoice2(lcs9)
print 'k9= ',k9
lcs10 = shift2(lcs9)
print 'lcs10=',lcs10
k10 = pchoice2(lcs10)
print 'k10=',k10
lcs11 = shift2(lcs10)
print 'lcs11=',lcs11
k11 = pchoice2(lcs11)
print 'k4=',k4
lcs12 = shift2(lcs11)
print 'lcs12=',lcs12
k12 = pchoice2(lcs12)
print 'k12=',k12
lcs13 = shift2(lcs12)
print 'lcs13=',lcs13
k13 = pchoice2(lcs13)
print 'k13=',k13
lcs14 = shift2(lcs13)
print 'lcs14=',lcs14
k14 = pchoice2(lcs14)
print 'k14=',k14
lcs15 = shift2(lcs14)
print 'lcs15=',lcs15
k15 = pchoice2(lcs15)
print 'k15=',k15
lcs16 = shift1(lcs15)
print 'lcs16=',lcs16
k16 = pchoice2(lcs16)
print 'k16=',k16

txt = open('ciphertext.txt','rb')
txtout = open('decryptiontext.txt','wb')

for y in range (1,217):
	'print y'
	pt = ''
	for z in range (1,9):
		plc = txt.read(8)
		pc = str(plc)
		print pc
		pt = pt+(pc.zfill(8))
		print pt

	ippt = ip(pt) 
	left = ippt[0:32]
	print left
	right = ippt[32:64]
	print right
	(left,right) = encrypt(left,right,k16)

	print left
	print right

	(left,right) = encrypt(left,right,k15)
	(left,right) = encrypt(left,right,k14)
	(left,right) = encrypt(left,right,k13)
	(left,right) = encrypt(left,right,k12)
	(left,right) = encrypt(left,right,k11)
	(left,right) = encrypt(left,right,k10)
	(left,right) = encrypt(left,right,k9)
	(left,right) = encrypt(left,right,k8)
	(left,right) = encrypt(left,right,k7)
	(left,right) = encrypt(left,right,k6)
	(left,right) = encrypt(left,right,k5)
	(left,right) = encrypt(left,right,k4)
	(left,right) = encrypt(left,right,k3)
	(left,right) = encrypt(left,right,k2)
	(left,right) = encrypt(left,right,k1)

	temp = left
	left = right
	right = temp

	swapout = (left+right).zfill(64)

	ct = invip(swapout)
	print ct
	ct1 = ct[0:8]
	"c1 = ct1.encode('utf-8')"
	c1 = chr(int(ct1,2)) 
	print c1
	ct2 = ct[8:16]
	"c2 = ct2.encode('utf-8')"
	c2 = chr(int(ct2,2)) 
	print c2
	ct3 = ct[16:24]
	"c3 = ct3.encode('utf-8')"
	c3 = chr(int(ct3,2)) 
	print c3
	ct4 = ct[24:32]
	"c4 = ct4.encode('utf-8')"
	c4 = chr(int(ct4,2)) 
	print c4
	ct5 = ct[32:40]
	"c5 = ct5.encode('utf-8')"
	c5 = chr(int(ct5,2)) 
	print c5
	ct6 = ct[40:48]
	"c6 = ct6.encode('utf-8')"
	c6 = chr(int(ct6,2)) 
	print c6
	ct7 = ct[48:56]
	"c7 = ct7.encode('utf-8')"
	c7 = chr(int(ct7,2)) 
	print c1
	ct8 = ct[56:64]
	"c8 = ct8.encode('utf-8')"
	c8 = chr(int(ct8,2)) 
	print c8
	
	ctext = (c1+c2+c3+c4+c5+c6+c7+c8)
	print ctext
	txtout.write(ctext)
	print (8*y+z)
txt.close()
txtout.close()


