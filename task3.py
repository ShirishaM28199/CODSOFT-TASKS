import struct,os

def get_image_data(f):
    with open(f,'rb') as x:
        d=x.read(25)
        if d.startswith(b'\x89PNG\r\n\x1a\n'):
            w,h=struct.unpack('>ii',d[16:24])
            return "PNG",w,h
        elif d.startswith(b'\xff\xd8'):
            x.seek(0)
            x.read(2)
            b=x.read(1)
            while b and b!=b'\xda':
                while b!=b'\xff':b=x.read(1)
                while b==b'\xff':b=x.read(1)
                if b>=b'\xc0' and b<=b'\xc3':
                    x.read(3)
                    h,w=struct.unpack('>HH',x.read(4))
                    return "JPEG",w,h
                else:
                    x.read(int(struct.unpack('>H',x.read(2))[0])-2)
                b=x.read(1)
    return "Unknown",0,0

def run_task3():
    print("--- CodSoft Task 3: Image Captioning AI ---")
    p=input("Paste image path: ").strip().replace('"','')
    try:
        t,w,h=get_image_data(p)
        print(f"\n[AI Analysis] Image Type: {t} | Resolution: {w}x{h}")
        if w>h:
            c=f"A wide {t} image, likely a landscape or screenshot."
        elif h>w:
            c=f"A vertical {t} image, similar to a mobile photo."
        else:
            c=f"A square {t} image, suitable for profile or icon."
        print("GENERATED CAPTION:",c)
    except:
        print("Error reading file")

if __name__=="__main__":
    run_task3()