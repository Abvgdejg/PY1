import cv2
import numpy as np
import framesProcessing
import argsParser
import av
import writeTools

def SplitVideo(video):
    try:
        if args.frames == "all":
            writeTools.SetupWriting()
        
            current_video = av.open(video)
            frames_list = []
            for frame in current_video.decode():
                
                arr_frame = frame.to_ndarray(format='bgr24')
                frames_list += [arr_frame]
                
                writeTools.WriteConsole("Preparing frames")
        

            writeTools.WriteConsole("Preparing frames complete", True)
            
            return frames_list
        else:
            writeTools.SetupWriting()
        
            current_video = av.open(video)
            frames_list = []
            decoded_list = list(current_video.decode())
            
            for frame in args.frame_list:
                
                tmp_frame = decoded_list[frame]
                arr_frame = tmp_frame.to_ndarray(format='bgr24')
                frames_list += [arr_frame]
                
                writeTools.WriteConsole("Preparing frames")
        

            writeTools.WriteConsole("Preparing frames complete", True)
            
            return frames_list
    except:
        VideoError()

def VideoError():
    print("Video Error")
    print("Use --video=path")
    raise SystemExit

def FrameProcessing(video):
   return framesProcessing.main_search(framesProcessing.get_exp(args.exp_file), args, video)
      
                

def WriteVideo(video_frames):
    
    out = cv2.VideoWriter('Processed video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 22, (1920, 1080))

    writeTools.SetupWriting(video_frames)

    for frame in video_frames:
        
        out.write(frame)

        writeTools.WriteConsole("Frame recording")
    
    writeTools.WriteConsole("Frame recording complete", True)  
    out.release()
    

def Start():

    global args 
    args = argsParser.ArgParse()

    


    splited_video = SplitVideo(args.video)
    processed_video = FrameProcessing(splited_video)

    WriteVideo(processed_video)  

    print("Video processing complete")
    

Start()

#/app/resources/develop_streem.ts
