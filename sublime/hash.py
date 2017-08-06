
import hashlib

def get_md5(s):
    hashlib.md5(s).hexdigest()


def get_sha1(s):
    hashlib.sha1(s).hexdigest()

def get_file_md5(f):
    m = hashlib.md5()
    while True:
        data = f.read(10240)
	if not data:
	    break
        m.update(data)
    return m.hexdigest()

with open(YOUR_FILE, 'rb') as f:
    file_md5 = get_file_md5(f)

main()
