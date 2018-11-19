import os
import cv2
import shutil
import random
from prepare import  private_config as private_config

def fun2(dataset_path=None, CT_sets=None, save_file_name=None,is_train=True):
    if dataset_path is None:
        if is_train:
            dataset_path = private_config.data_path
        else:
            dataset_path = private_config.valid_data_path
    if CT_sets is None:
        if is_train:
            CT_sets = private_config.CT_set
        else:
            CT_sets = private_config.valid_CT_set
    if save_file_name is None:
        if is_train:
            save_file_name = private_config.image_set + '.lst'
        else:
            save_file_name = private_config.valid_image_set + '.lst'
    if len(CT_sets) == 0:
        CT_sets = os.listdir(dataset_path)
        if 'patient_list' in CT_sets:
            CT_sets.remove('patient_list')
        if 'cache' in CT_sets:
            CT_sets.remove('cache')
        if 'pak' in CT_sets:
            CT_sets.remove('pak')

    ## where put the combined .list
    save_path = os.path.join(dataset_path, 'patient_list')

    if not os.path.exists(save_path):
        os.mkdir(save_path)
    exclude_dirs=private_config.exclude_dirs

    exclude_pids=[]
    for e_dir in exclude_dirs:
        exclude_pids.extend(os.listdir(e_dir))
    exclude_pids=set(exclude_pids)
 
    lines = []
    exclude_wrong_ids=[]
    exclude_count=0
    for ct_set in CT_sets:
        ct_set_path = os.path.join(dataset_path, ct_set)
        if os.path.isdir(ct_set_path):
            set_dicom_path = os.path.join(ct_set_path, 'dcm')
            set_anno_path = os.path.join(ct_set_path, 'anno_folder')
            # set_seg_path = os.path.join(ct_set_path, 'seg')
            #todo seal
            all_dcm=os.listdir(set_dicom_path)
            select_count=len(all_dcm)
            # select_count=len(all_dcm[:1000])
            random.shuffle(all_dcm)
            all_dcm=all_dcm[:select_count]
            print (ct_set,select_count)
            ## todo cancel test
            for dcm in all_dcm:

                patient_dicom_path = os.path.join(set_dicom_path,dcm[:-4]+".dcm")

                patient_anno_path = os.path.join(set_anno_path, dcm[:-4]+".xml")

                lines.append('%s\t%s\t%s\n' % (patient_dicom_path, patient_anno_path, dcm[:-4]))
    print (len(lines),exclude_count)
    print (exclude_wrong_ids)
    random.shuffle(lines)

    with open(os.path.join(save_path, "train.lst"), 'w') as f:
        f.writelines(lines[:int(select_count*0.8)])

    with open(os.path.join(save_path, "valid.lst"), 'w') as f:
        f.writelines(lines[int(select_count*0.8):])


if __name__ == '__main__':
    fun2(is_train=True)
