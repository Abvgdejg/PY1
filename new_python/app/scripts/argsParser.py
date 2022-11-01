import argparse

def make_parser():

    parser = argparse.ArgumentParser("YOLOX")
  

    parser.add_argument("--frames", default=None, help="Frames")
        
    parser.add_argument("--video", help="Video")

    
    return parser

def ArgParse():

    tmp_args = make_parser().parse_args()

    try:
        tmp_args.frames = tmp_args.frames.split(",")
        
        tmp_args.frame_list = []

        for param in tmp_args.frames:
            param = int(param)
            tmp_args.frame_list.append(param)

    except:
        tmp_args.frames = "all"
    
    tmp_args.ckpt = '../YOLOX/assets/yolox_s.pth'
    tmp_args.exp_file = '../YOLOX/exps/default/yolox_s.py'
    tmp_args.path = "../YOLOX/assets/"
    tmp_args.save_result = True
    tmp_args.experiment_name = None
    tmp_args.name = None
    tmp_args.camid = 0
    tmp_args.device = "cpu"
    tmp_args.conf = 0.3
    tmp_args.nms = 0.3
    tmp_args.tsize = None
    tmp_args.fp16 = False
    tmp_args.legacy = False
    tmp_args.fuse = False
    tmp_args.trt = False
    
    return tmp_args