import os                                                                                                                                                                                                                                                                      
import re                                                                                                                                                                                                                                                                      
import shutil                                                                                                                                                                                                                                                                  
from classes.FileParser import FileParser
from classes.Logger import Logger
                                                                                                                                                                                                                                                                               
rootdir = '/storage/staging'                                                                                                                                                                                                                                                   
logfile = '/tmp/manage_downloads.log'                                                                                                                                                                                                                         
tvdirectory = '/storage/Videos/TV'                                                                                                                                                                                                                                             
moviedirectory = '/storage/Videos/Movies'                                                                                                                                                                                                                                      

#log.write('This is a test\n')
tvregex = re.compile(r"(.*[Ss]\d\d[Ee]\d\d.*)|(.*(daily.*show|colbert.*report).*)(\.avi|\.mpeg|\.mpg|\.mp4|\.mkv)", re.IGNORECASE)
seasonregex = re.compile(r"[Ss]\d\d", re.IGNORECASE)
movieregex = re.compile(r".*(brrip|bdrip|dvdrip|hdrip|hdcam|ppvrip|dvd|1080p|720p|r5|r6).*(\.avi|\.mpeg|\.mpg|\.mp4|\.mkv)", re.IGNORECASE)
sampleregex = re.compile(r".*sample.*", re.IGNORECASE)

fileName = 'theawesometvshowS01E03.avi'
logger = Logger(logfile)
parser = FileParser(logger)
parser.isTvShow(fileName)
parser.isMovie(fileName)
parser.isSample(fileName)
parser.getSeasonNumber(fileName)
