seqlen = 1
# network='vgg16_reduced'
network='resnet50'
# data_path="/Users/yanxinzhou/course/kaggle/agriculture/data/rsna/data"
data_path="/home/xyan22/home/xyan22/work/multicls/data/"
# root_path = "/Users/yanxinzhou/course/kaggle/agriculture/data/rsna/data/root"
root_path = "/home/xyan22/home/xyan22/work/multicls/data/root"

CT_set = ['train']

image_set = 'train'

fp_file = ''
valid_image_set = 'valid'  # ''valid_dalian_fp'
# valid_data_path = "/Users/yanxinzhou/course/kaggle/agriculture/data/rsna/data"
valid_data_path = "/home/xyan22/home/xyan22/work/multicls/data/"
valid_CT_set = ['valid']  # [   'test_gt']

model_dir = "/home/xyan22/home/xyan22/work/multicls/data/model"  # ''./'

classes = ['bc', 'ill']
CLASSES = classes

CLASS_DICT = {'ill': 'ill'}

WEIGHT_DICT = {'ill': 1 }

detailed_class = ['ill']

subgraph=True
has_crop = True
data_shape =512# 1024
crop_scale = 0.25
fg_thresh = 0.6
bg_thresh = 0.000001
soft_degree = 5
enable_soft_mining = False
enable_aspp = False
batch_size = 48
num_gpus = 4
lr = 2e-3
train_samples_count = 4544+1115
valid_samples_count = 1115
exclude_dirs = []#'/media/tx-eva-test/Data_ssd/zhh_data/test/lanfei_test/dcm/',
                #'/media/tx-eva-test/Data_ssd/zhh_data/test/test_gt/dcm/']
