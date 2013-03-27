'''
Created on 21 Nov 2012

@author: Michael Kemp
'''
import urllib2
import os

from bs4 import BeautifulSoup

page = urllib2.urlopen("http://www.metoffice.gov.uk/weather/uk/observations/")
soup = BeautifulSoup(page)
        
        
## This need to be changed to allow the print and write to be separate.  Too much duplication here
def get_data(name):
    print 'Met Office: UK: Latest observations for ' + name + "\n"
    forest = soup.find(text=name).findPrevious('tr')
    
    print  "Weather " + forest.img['title'] +"\n"
    write_data("Weather", forest.img['title'] +"\n")
    
    print "Degrees C\n" + forest('td')[2].text + "\n"
    write_data("Degrees>C", forest('td')[2].text + "\n")
    
    print "Wind direction\n" + forest('td')[4].text + "\n"
    write_data("Wind>direction", forest('td')[4].text + "\n")
     
    print "Wind speed (Mph)\n" + forest('td')[5].text + "\n"
    write_data("Wind>speed>(Mph)", forest('td')[5].text + "\n")
    
    print "Gust speed (Mph)\n" + forest('td')[7].text + "\n"
    write_data("Gust>speed>(Mph)", forest('td')[7].text + "\n")
    
    print "Visability (Kilometers)\n" + forest('td')[9].text + "\n"
    write_data("Visability", forest('td')[9].text + "\n")
    
    print "Pressure \n" + forest('td')[11].text
    write_data("Pressure", forest('td')[11].text.replace(u'\xa0', u' '))
  
    print  "Files have been sent to " + os.getcwd()
    

        
def write_data(name, value):
    output = open(name +".txt", "w")
    output.write(name + "\n" + value)
    output.close()
     

##file.write(soup.title.string + ' for Ballypatrick Forest\n')
##file.write('\n')
##
##file.write("Degrees C\n" + forest('td')[2].text + "\n")
##file.write('\n')
##file.write("Wind direction\n" + forest('td')[4].text + "\n")
##file.write('\n')
##file.write("Wind speed (Mph)\n" + forest('td')[5].text + "\n")
##file.write('\n')
##file.write("Gust speed (Mph)\n" + forest('td')[7].text + "\n")
##file.write('\n')
##file.write("Visability (Kilometers)\n" + forest('td')[9].text + "\n")
##file.write('\n')
##file.write("Pressure\n" + forest('td')[11].text.replace(u'\xa0', u' '))
##file.write('\n')
##file.close()

get_data('Ballypatrick Forest')
    
    

