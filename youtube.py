from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

#ALL FUNCTION

#====variables =====#
FolderName = ""
filesizeInBytes = 0
MaxFileSize = 0 

#======= OPEN DIR FUNC=======#
def openDirectory():
        global FolderName
        FolderName =  filedialog.askdirectory()
        if(len(FolderName) > 1):
            fileLocationLabelError.config(text=FolderName,
                                               fg="green")
        
        else:
            fileLocationLabelError.config(text="Please choose folder!",
                                         fg="red")
        

def DownloadFile():
        global MaxFileSize,fileSizeInBytes
        
        choice = youtubeChoices.get()
        video = youtubeEntry.get()
        
        if(len(video)>1):
                youtubeEntryError.config(text="")
                # print(video,"at",FolderName)
                yt = YouTube(video,on_progress_callback=progress())
                #on_complete_callback=complete
                # print("Video Name is:\n\n",yt.title)
                
                
                if(choice == downloadChoices[0]):
                    # print("720p Video file downloading...")
                    fileLocationLabelError.config(text="720p Video file downloading...")
                    
                    selectedVideo =yt.streams.filter(progressive=True).first()
                                
                elif(choice == downloadChoices[1]):
                    # print("144p video file downloading...")
                    fileLocationLabelError.config(text="144p video file downloading...")
                    selectedVideo =yt.streams.filter(progressive=True,
                                                     file_extension='mp4').last()
                  
                elif(choice == downloadChoices[2]):
                    #print("3gp file downloading...")
                    fileLocationLabelError.config(text="3gp file downloading...")
                    selectedVideo =yt.streams.filter(file_extension='3gp').first()
                    
                elif(choice == downloadChoices[3]):
                    #print("Audio file downloading...")
                    fileLocationLabelError.config(text="Audio file downloading...")
                    selectedVideo = yt.streams.filter(only_audio=True).first()
                    
                fileSizeInBytes = selectedVideo.filesize
                MaxFileSize = fileSizeInBytes/1024000
                MB = str(MaxFileSize) + " MB"
                #print("File Size = {:00.00f} MB".format(MaxFileSize))
                
                #now Download ------->
                selectedVideo.download(FolderName)  
                progress()             
                #==========>
                # print("Downloaded on:  {}".format(FolderName))
                loadingLabel.config(text=("Download Complete ",MB))
                complete()
                
        else:
                youtubeEntryError.config(text="Please paste youtube link",
                                         fg="red")
        #============progress bar==================

def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # Gets the percentage of the file that has been downloaded.
    #nextLevel = Toplevel(root)
    #percent = (100 * (fileSizeInBytes - remaining)) / fileSizeInBytes
    #print("{:00.0f}% downloaded".format(percent))
    loadingLabel.config(text="Downloading...") 
            
def complete():
    loadingLabel.config(text=("Download Complete \n     Downloaded on:  {} \n   File Size = {:00.00f} MB".format(FolderName, MaxFileSize)))



#=================GUI WINDOW=============================#
base = Tk() 
base.geometry("700x700")
base.title("YOUTUBE   DOWNLOADER")
base.grid_columnconfigure(0,weight = 1)
#========you tube link label =================#
youtubeLinkLabel = Label(
                    base , text = " PASTE YOUR LINK HERE!!!!!! " ,
                    fg = "white" , 
                    bg = "red",
                    width = 100 ,
                    height = 1,
                    font=("Agency FB", 30)
                    )
youtubeLinkLabel.grid()
#=======BOX to paste you tube link=============#
youtubeEntryVar = StringVar()
youtubeEntry = Entry(
                     base,
                     width=50, 
                     textvariable=youtubeEntryVar
                     )
youtubeEntry.grid(pady=(15,20))
#=======LABEL WHEN LINK IS WRONG =============#
youtubeEntryError = Label(base,fg="red",
                        text="",font=("Agency FB", 20)
                          )
ERRORMESSAGES = "WRONG LINK !!!!!!!!PLEASE CHECK IT ONCE" 
youtubeEntryError.grid(pady=(0,9))

#=======FILE LOCATION LABEL =================#
saveLabel = Label(
                  base ,
                  text = "CHOOSE LOCATION TO STORE THIS VIDEO",
                  fg = "white",
                  bg="red" ,
                  width = 100 ,
                  height = 1,
                  font=("Agency FB", 30)
                  )
saveLabel.grid()
#=======path chooseing========================#
saveEntry = Button(
                base,
                fg = "white",
                bg= "red",
                text="CHOOSE FOLDER",
                font=('arial', 16),
                command=openDirectory)
saveEntry.grid(pady = (5 , 2))
#=======if user is not choosing path========#
fileLocationLabelError = Label(
                            base,
                            text="", font=("Agency FB", 20)
                            )
fileLocationLabelError.grid(pady=(0,0))
#======= what to download choice==========
youtubeChooseLabel = Label(
                            base,
                            text="Please choose what to download: ",
                            font=("Agency FB", 20)
                           )
youtubeChooseLabel.grid()
# Combobox with four choices:
downloadChoices = ["Mp4_720p",
                   "Mp4_480p",
                   "Video_3gp",
                   "Song_MP3"]
youtubeChoices = ttk.Combobox(
                            base,
                            values=downloadChoices
                            )
youtubeChoices.grid()
#==================Download button===================
downloadButton = Button(base,
                                     text="Download", width=15,bg="red",fg="white",
                                     command=DownloadFile
                        )
downloadButton.grid(pady=(20,20))




loadingLabel = ttk.Label(base,
                        text="",
                        font=("Agency FB", 20)
                        )
loadingLabel.grid()

base.mainloop() 
