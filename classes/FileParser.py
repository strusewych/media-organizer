import os                                                                                                                                                                                                                                                                      
import re                                                                                                                                                                                                                                                                      
import shutil  
from Logger import Logger

class FileParser:
  
    rootdir = '/storage/staging'                                                                                                                                                                                                                                 
    tvdirectory = '/storage/Videos/TV'                                                                                                                                                                                                                                             
    moviedirectory = '/storage/Videos/Movies'    
    #log.write('This is a test\n')
    tvregex = re.compile(r"(.*[Ss]\d\d[Ee]\d\d.*)|(.*(daily.*show|colbert.*report).*)(\.avi|\.mpeg|\.mpg|\.mp4|\.mkv)", re.IGNORECASE)
    seasonregex = re.compile(r"[Ss]\d\d", re.IGNORECASE)
    movieregex = re.compile(r".*(brrip|bdrip|dvdrip|hdrip|hdcam|ppvrip|dvd|1080p|720p|r5|r6).*(\.avi|\.mpeg|\.mpg|\.mp4|\.mkv)", re.IGNORECASE)
    sampleregex = re.compile(r".*sample.*", re.IGNORECASE)
  
    def __init__(self, logger):
        self.data = []
        self.logger = logger
        
    def isTvShow(self, fileName):
        if self.tvregex.match(fileName):
          self.logger.write(fileName + ' has been determined to be a tv show')
          return True
        else:
          return False 
      
    def isMovie(self, fileName):
        if self.movieregex.match(fileName):
          self.logger.write(fileName + ' has been determined to be a movie')
          return True
        else:
          return False
      
    def isSample(self, fileName):
        if self.sampleregex.match(fileName):
          self.logger.write(fileName  + ' has been determined to be a sample clip')
          return True
        else:
          return False
      
    def getSeasonNumber(self, fileName):
        season = self.seasonregex.search(fileName)
        seasonnumber = str(int(season.group()[1:]))
        self.logger.write('season number for ' + fileName + ' is ' + seasonnumber)
        return seasonnumber
      
    def getDestinationFolder(self, fileName, destinationRoot):
        #try and locate the correct season folder
        seasonnumber = str(int(season.group()[1:]))
        for seasonsfolder in os.walk(tvdirectory + '/' + tvshows).next()[1]:
          correctfolderregex = re.compile(r".*season\s" + seasonnumber , re.IGNORECASE)
          correctfolder = correctfolderregex.match(seasonsfolder)
          if correctfolder:
            logger.write('moving ' + subdir + '/' + file + " to " + tvdirectory + '/' + tvshows+ '/' + seasonsfolder + '\n')
            shutil.move(subdir + '/'+ file, tvdirectory + '/' + tvshows + '/' + seasonsfolder)
            
    
    
