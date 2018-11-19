import numpy as np
import numbers
import struct
from mxnet.recordio import IRHeader,_IR_FORMAT
try:
    import cv2
except ImportError:
    cv2 = None

from prepare import private_config

def pack_CT(header, CT_imgs, quality=95):
    """Pack an CT_image into ``MXImageRecord``.

    """
    # CT_imgs=[img[:,:,np.newaxis] for img in CT_imgs]
    assert cv2 is not None
    encode_params = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    img_fmt = '.jpg'
    re_str=b''
    # ret, buf = cv2.imencode(img_fmt, np.concatenate(CT_imgs,axis=0), encode_params)
    # re_str=buf.tostring()
    list_end_img_size=[]
    last_size=0
    ## todo double check imencode
    for img in CT_imgs:
        ret, buf = cv2.imencode(img_fmt, img[:,:,np.newaxis], encode_params)
        cur_buf_str=buf.tostring()
        list_end_img_size.append(last_size+len(cur_buf_str))
        last_size=list_end_img_size[-1]
        re_str+=cur_buf_str
        assert ret, 'failed to encode image'

    return pack(header,re_str,list_end_img_size)



def pack(header, s,list_end_img_size):
    """Pack a string into MXImageRecord.
    """
    #todo wtf is irheader
    header = IRHeader(*header)
    if isinstance(header.label, numbers.Number):
        header = header._replace(flag=0)
    else:
        ### todo here is the bug
        if len(header.label)>2:
            label = np.asarray([2 + private_config.seqlen, 6] + list_end_img_size + header.label[2:], dtype=np.double)
        else:
            label = np.asarray([2 + private_config.seqlen, 6] + list_end_img_size, dtype=np.double)
        # label = np.asarray(header.label, dtype=np.float32)
        header = header._replace(flag=label.size, label=0)
        s = label.tostring() + s
    s = struct.pack(_IR_FORMAT, *header) + s

    return s