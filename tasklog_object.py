import csv
import datetime

import re
import os


class New_entry:## this class is used to log a new entry
    
    def __init__(self,task_name,minutes,notes,date):
        self.task_name=task_name
        self.minutes=minutes
        self.notes=notes
        self.date=date

    def saving(self):## this method saves the new log
        ## saving to csv file
        with open('task.csv','a') as csvfile:
            fieldnames = ['task_name','minutes','notes','date']
            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
            teachwriter.writeheader()

            
            teachwriter.writerow({'task_name':str(self.task_name),
                                  'minutes':str(self.minutes),
                                  'notes':str(self.notes),
                                  'date':str(self.date)
                                  })
            
        print('\n.................. SUCCESSFULLY SAVED ........................\n')

       

            

    



class Look_up:## this class is used to  search previous logs



    def By_range(self):  ## this method searches the a log by using a date range
        back='this page is not availabel'## i created this string to be used when
                                         ##we choose to go back on the first item
                                         ## since there is no result to go back to

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
              '\n\n\n\n\n\n\n\n\n\n\n.....TASK SEARCH BY DATE RANGE WINDOW.......\n\n')
        ## this describes the window
        ## the new lines are used to create a single page for the task
        while True:
            self.range1=input('\n\nENTER THE START DATE (mm-dd-YYYY): ')## here we take the first date
            self.range2=input('\nENTER THE END DATE (mm-dd-YYYY: ')## here we take the second date
            

            if '-' not in self.range1 and '-' not in self.range2:
                print('\n\n..oops .your input was invalid.\n please try again.\n\n')
                
            else:
                
                self.li_range1=self.range1.split('-')## changing the dates to a list to make using them easier
                self.li_range2=self.range2.split('-')

                if len(self.li_range1)==3 and len(self.li_range2)==3:
                

                    if str in self.li_range1 or  str in self.li_range2 :
                        print('...oops. your input was invalid.\n please try again')

                        self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                        if self.answer3=='0':
                            Menu()

                        if self.answer3=='1':

                            self.By_range()
                        else:
                            exit()
                                


                    ##here we get the sum of the day,the month and the year together to compare and find the dates between them

                    self.sum_range1=self.li_range1[0]+self.li_range1[1]+self.li_range1[2]
                    self.sum_range2=self.li_range2[0]+self.li_range2[1]+self.li_range2[2]


                    
                    if self.sum_range1<=self.sum_range2:## this code checks if the start date is less than the end date
                        with open ('task.csv',newline='')as csvfile:## opening the csv
                            taskreader=csv.reader(csvfile,delimiter='|')
                            file=list(taskreader)
                        
                            self.exist='no'
                        for item in file[::2]:
                            self.to_str=''.join(item)
                            self.to_li=self.to_str.split(',')
                            self.se=self.to_li[3]
                            if self.se!='date':## making sure the date heading is skipped
                                


                                self.se_toli=self.se.split('-')
                                self.se_sum=self.se_toli[0]+self.se_toli[1]+self.se_toli[2]## finding the sum of the date to compare



                                
                                    

                                
                                 ## checking if the date is in the range

                                check1=bool(int(self.se_sum)>=int(self.sum_range1))
                                check2=bool(int(self.se_sum)<=int(self.sum_range2))
                                    

                                if check1== True and check2==True:
                                    self.exist='yes'## to be used to check if the item we are searching for exists
                                    if self.to_li[2].lower()=='skip':
                                        ## skipping the note for the one's that say skip
                                        print('\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n'
                                              '\n'.format(self.to_li[0],self.to_li[1],self.to_li[3]))
                                        self.page=input('1 NEXT PAGE\n'
                                                        '2 BACK: ')

                                        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                              '\n\n\n\n\n\n\n\n\n\n\n\n'
                                              '\n\n\n\n\n\n\n\n\n\n\n\n\n')## creating a clear screen

                                        try:
                                            self.page=int(input('1 NEXT PAGE \n'
                                                                '2 BACK : '))## to navigate to the previous or next page


                                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                                  '\n\n\n\n\n\n\n\n\n\n\n\n'
                                                   '\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                            if str(self.page)=='1':

                                            ## saving incase we want to go back
                                                

                                                                                           
                                                if self.to_li[2].lower()=='skip':
                                                    back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n
                                                          \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])## print without a note
                                                   
                                                else:   
                                                    back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                                    continue
                                            if str(self.page)=='2':
                                                
                                            
                                                print(back)

                                                self.page=int(input('1 NEXT PAGE\n'
                                                                    '2 BACK: '))

                                            if str(self.page) =='1' or str(self.page) =='2':
                                                continue
                                            else:
                                                print('\n ..ooops! the page is not availabel!\n')
                                                self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                                                   'ENTER 0 FOR MAIN MENU \n'
                                                                   'ENTER ANY OTHER KEY TO EXIT: ')
                                            if self.answer3=='0':
                                                Menu()

                                            if self.answer3=='1':

                                                self.By_range()
                                            else:
                                                exit()




                                                
                                        except ValueError as Err:
                                            print('\n ..ooops! the page is not availabel!\n')
                                            self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                                               'ENTER 0 FOR MAIN MENU \n'
                                                               'ENTER ANY OTHER KEY TO EXIT: ')
                                        if self.answer3=='0':
                                            Menu()

                                        if self.answer3=='1':

                                            self.By_range()
                                        else:
                                            exit()



                                    else:   
                                        print('\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                              '\n'.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3]))## print with note


                                        try:
                                            self.page=int(input('1 NEXT PAGE \n'
                                                                '2 BACK : '))


                                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                                  '\n\n\n\n\n\n\n\n\n\n'
                                                   '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                            if str(self.page)=='1':
                                                ## saving incase back is called
                                                if self.to_li[2].lower()=='skip':
                                                    back='\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n''\n'.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                                   
                                                else:   
                                                    back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                                    continue
                                            if str(self.page)=='2':
                                                
                                            
                                                print(back)

                                                self.page=int(input('1 NEXT PAGE\n'
                                                                    '2 BACK: '))

                                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                                      '\n\n\n\n\n\n\n\n\n\n\n\n'
                                                     '\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                                
                                            if str(self.page) =='1' or str(self.page) =='2':
                                                continue
                                            else:
                                                print('\n ..ooops! the page is not availabel!\n')
                                                self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                                                   'ENTER 0 FOR MAIN MENU \n'
                                                                   'ENTER ANY OTHER KEY TO EXIT: ')
                                                if self.answer3=='0':
                                                    Menu()

                                                if self.answer3=='1':

                                                    self.By_range()
                                                else:
                                                    exit()
                                                    
                                        except ValueError as Err:
                                            print('\n ..ooops! the page is not availabel!\n')
                                            self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                                               'ENTER 0 FOR MAIN MENU \n'
                                                               'ENTER ANY OTHER KEY TO EXIT: ')
                                        if self.answer3=='0':
                                            Menu()

                                        if self.answer3=='1':

                                            self.By_range()
                                        else:
                                            exit()

                else:
                    print('\n\n..oops! your input was invalid \nplease try again\n\n')


                    self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                               'ENTER 0 FOR MAIN MENU \n'
                               'ENTER ANY OTHER KEY TO EXIT: ')
                    if self.answer3=='0':
                        Menu()

                    if self.answer3=='1':

                        self.By_range()
                    else:
                        exit()


                if self.exist=='yes':
                    self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                       'ENTER 0 FOR MAIN MENU \n'
                                       'ENTER ANY OTHER KEY TO EXIT: ')
                    if self.answer3=='0':
                        Menu()

                    if self.answer3=='1':

                        self.By_range()
                    else:
                        exit()

                else:
                    
                

                    print('\n\n....oops! there are no items for this date\n please try again.\n')



                    self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                               'ENTER 0 FOR MAIN MENU \n'
                               'ENTER ANY OTHER KEY TO EXIT: ')
                    if self.answer3=='0':
                        Menu()

                    if self.answer3=='1':

                        self.By_range()
                    else:
                        exit()
                                 
             ## this code takes us back to menu or lets us do another operation   
            self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                               'ENTER 0 FOR MAIN MENU \n'
                               'ENTER ANY OTHER KEY TO EXIT: ')
            if self.answer3=='0':
                Menu()

            if self.answer3=='1':

                self.By_range()
            else:
                exit()


         

    def By_Date(self):## this method finds by exact date
        back='this page is not availabel'
        with open ('task.csv',newline='')as csvfile:
            taskreader=csv.reader(csvfile,delimiter='|')
            file=list(taskreader)
        
        self.date_list=[]

        for item in file[::2]:
            self.to_str=''.join(item)
            self.to_li=self.to_str.split(',')
            self.se=self.to_li[3]
            self.date_list.append(self.se)

        if len(self.date_list)==0:
            print('\n...oops!  you dont have any saved tasks....\n')
            self.answer3=input('ENTER 0 FOR MAIN MENU \n'
                               'ENTER ANY OTHER KEY TO EXIT: ')
            if self.answer3=='0':
                Menu()

            
            else:
                exit()

                
            
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
              '\n\n\n\n\n\n\n\n\n\n\n\n............Date of all tasks ............\n\n')
        ## here i list all the dates
        
        for self.i in self.date_list:
            if self.i !='date':
                print(self.i)




        while True:
            while True:
                self.searchdate=input('\n\nenter date mm-dd-YYYY : ')
                if'-' in self.searchdate:
                    break
                else:
                    print('\n\n...oops! your input was invalid.\n please try again.')
                    self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                    if self.answer3=='0':
                        Menu()

                    if self.answer3=='1':

                        self.By_range()
                    else:
                        exit()
            

            self.exist='no'
            for item in file[::2]:
                self.to_str=''.join(item)
                self.to_li=self.to_str.split(',')
                self.se=self.to_li[3]

                if str(self.se)==self.searchdate :
                    
                    self.exist='yes'
                    
                    if self.to_li[2].lower()=='skip':
                        print('\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n'
                              '\n'.format(self.to_li[0],self.to_li[1],self.to_li[3]))


                        try:
                            self.page=int(input('1 NEXT PAGE \n'
                                                '2 BACK : '))

                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                  '\n\n\n\n\n\n\n\n\n'
                                   '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if str(self.page)=='1':
                                ## saving incase back is called
                                if self.to_li[2].lower()=='skip':
                                    back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n
                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                   
                                else:   
                                    back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                    continue
                            if str(self.page)=='2':
                                
                            
                                print(back)

                                self.page=int(input('1 NEXT PAGE\n'
                                                    '2 BACK: '))


                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                      '\n\n\n\n\n\n\n\n\n'
                                      '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if str(self.page)=='1' or str(self.page) =='2':
                                print('\n ..ooops! the page is not availabel!\n')
                                continue
                            else:
                                print('\n ..ooops! the page is not availabel!\n')
                                break
                                    
                        except ValueError as Err:
                            print('\n ..ooops! the page is not availabel!\n')
                            break
                    else:   
                        print('\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                              '\n'.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3]))

                        try:
                            self.page=int(input('1 NEXT PAGE \n'
                                           '2 BACK : '))

                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                  '\n\n\n\n\n\n\n\n\n\n'
                                   '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if str(self.page)=='1':
                                ## saving incase back is called
                                if self.to_li[2].lower()=='skip':
                                    back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n
                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                   
                                else:   
                                    back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                    continue
                            if str(self.page)=='2':
                                
                            
                                print(back)

                                self.page=int(input('1 NEXT PAGE\n'
                                               '2 BACK: '))

                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                      '\n\n\n\n\n\n\n\n\n\n'
                                       '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if str(self.page) =='1' or str(self.page) =='2':
                                continue
                            else:
                                print('\n ..ooops! the page is not availabel!\n')
                                break
                                    
                        except ValueError as Err:
                            print('\n ..ooops! the page is not availabel!\n')
                            break


            if self.exist=='yes':
                break
            else:

                print('\n\n....oops! there are no items for this date\n please try again.\n')
                self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                if self.answer3=='0':
                    Menu()

                if self.answer3=='1':

                    self.By_Date()
                else:
                    exit()
        csvfile.close()
        
        self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                           'ENTER 0 FOR MAIN MENU \n'
                           'ENTER ANY OTHER KEY TO EXIT: ')
        if self.answer3=='0':
            Menu()

        if self.answer3=='1':

            self.By_Date()
        else:
            exit()


    def By_Time(self):## this method searches by minutes spent on task

        back='this page is not availabel'
        with open ('task.csv',newline='')as csvfile:
            taskreader=csv.reader(csvfile,delimiter='|')
            file=list(taskreader)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
              '\n\n\n\n\n\n\n\n\n\n.....TASK SEARCH BY TIME SPENT WINDOW.......\n\n')
        while True:
            with open ('task.csv',newline='')as csvfile:
                taskreader=csv.reader(csvfile,delimiter='|')
                file=list(taskreader)
               

                while True:
                    
                    try:
                        self.searchtime=int(input('\n\nENTER TIME SPENT ON TASK : '))
                    except ValueError as Err:
                        print('\n\n...oops! your input was invalid.\n please try again.')
                        self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                        if self.answer3=='0':
                            Menu()

                        if self.answer3=='1':

                            self.By_range()
                        else:
                            exit()
                    else:
                        break
            self.exist='no'

            for item in file[::2]:
                self.to_str=''.join(item)
                self.to_li=self.to_str.split(',')
                self.se=self.to_li[1]
                
                if str(self.se)==str(self.searchtime):
                    self.exist='yes'
                    

                    if str(self.to_li[2]).lower()=='skip':
                        print('\n\nTask name:  {}\nMinutes:  {}\nDate:  {}\n'
                              '\n'.format(self.to_li[0],self.to_li[1],self.to_li[3]))

                        try:
                            self.page=int(input('1 NEXT PAGE \n'
                                           '2 BACK : '))

                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                  '\n\n\n\n\n\n\n\n\n\n'
                                   '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if str(self.page)=='1':
                                ## saving incase back is called
                                if self.to_li[2].lower()=='skip':
                                    back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n
                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                   
                                else:   
                                    back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                    continue
                            if str(self.page)=='2':
                                
                            
                                print(back)

                                self.page=int(input('1 NEXT PAGE\n'
                                               '2 BACK: '))
                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                      '\n\n\n\n\n\n\n\n\n\n\n'
                                       '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if str(self.page) =='1' or str(self.page) =='2':
                                continue
                            else:
                                print('\n ..ooops! the page is not availabel!\n')
                                break
                                    
                        except ValueError as Err:
                            print('\n ..ooops! the page is not availabel!\n')

                            break

                    else:   
                        print('\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                            '\n'.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3]))


                        try:
                            self.page=int(input('1 NEXT PAGE \n'
                                           '2 BACK : '))

                            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                  '\n\n\n\n\n\n\n\n\n\n'
                                   '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if str(self.page)=='1':
                                ## saving incase back is called
                                if self.to_li[2].lower()=='skip':
                                    back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n
                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                   
                                else:   
                                    back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n
                                         \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                    continue
                            if str(self.page)=='2':
                                
                            
                                print(back)

                                self.page=int(input('1 NEXT PAGE\n'
                                               '2 BACK: '))

                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                      '\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                       '\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                            if str(self.page) =='1' or str(self.page) =='2':
                                continue
                            else:
                                print('\n ..ooops! the page is not availabel!\n')
                                break
                                    
                        except ValueError as Err:
                            print('\n ..ooops! the page is not availabel!\n')
                            break


            if self.exist=='no':
                print('\n\n.....oops! your search doesnt exist\n please try again\n\n')
                self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                if self.answer3=='0':
                    Menu()

                if self.answer3=='1':

                    self.By_range()
                else:
                    exit()
            else:
                self.answer3=input('\nENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                if self.answer3=='0':
                    Menu()
                
                    break
                if self.answer3=='1':
                    continue
                else:
                    exit()
                    break

    def By_String(self):## this method searches by exact string

        back='this page is not availabel'
        with open ('task.csv',newline='')as csvfile:
            taskreader=csv.reader(csvfile,delimiter='|')
            file=list(taskreader)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
              '\n\n\n\n\n\n\n\n\n\n.....TASK SEARCH BY EXACT STRING WINDOW.......\n\n')
        while True:
            
            with open ('task.csv',newline='')as csvfile:
                taskreader=csv.reader(csvfile,delimiter='|')
                file=list(taskreader)
           
            self.searchname=input('\n\nENTER A STRING : ')
            self.exist='no'
            for item in file[::2]:
                self.to_str=''.join(item)
                self.to_li=self.to_str.split(',')
                self.se=self.to_li[0]
                self.st_note=self.to_li[2]
                if self.to_li[0]!='task_name':

                    
                    check1=bool(str(self.se)==self.searchname)
                    check2=bool(str(self.st_note)==self.searchname)
                    check3=bool(self.searchname in str(self.st_note))

                    
                    if check1==True or check2==True  or check3==True :
                        self.exist='yes'
                    
                        if self.to_li[2].lower()=='skip':
                            print('\n\nTask name:  {}\nMinutes:  {}\nDate:  {}\n'
                                  '\n'.format(self.to_li[0],self.to_li[1],self.to_li[3]))




                            try:
                                self.page=int(input('1 NEXT PAGE \n'
                                               '2 BACK : '))

                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                       '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if str(self.page)=='1':
                                    ## saving incase back is called
                                    if self.to_li[2].lower()=='skip':
                                        back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n
                                             \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                       
                                    else:   
                                        back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                             \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                        continue
                                if str(self.page)=='2':
                                    
                                
                                    print(back)

                                    self.page=int(input('1 NEXT PAGE\n'
                                                        '2 BACK: '))

                                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                           '\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if str(self.page) =='1' or str(self.page) =='2':
                                    continue
                                else:
                                    print('\n ..ooops! the page is not availabel!\n')
                                    break
                                        
                            except ValueError as Err:
                                print('\n ..ooops! the page is not availabel!\n')
                                break
                                
                        else:
                            print('''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                  \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3]))



                            try:
                                self.page=int(input('1 NEXT PAGE \n'
                                                    '2 BACK : '))

                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                       '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if str(self.page)=='1':
                                    ## saving incase back is called
                                    if self.to_li[2].lower()=='skip':
                                        back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n
                                             \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                       
                                    else:   
                                        back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                             \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                        continue
                                if str(self.page)=='2':
                                    
                                
                                    print(back)

                                    self.page=int(input('1 NEXT PAGE\n'
                                                        '2 BACK: '))

                                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                           '\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if str(self.page) =='1' or str(self.page) =='2':
                                    continue
                                else:
                                    print('\n ..ooops! the page is not availabel!\n')
                                    break
                                        
                            except ValueError as Err:
                                print('\n ..ooops! the page is not availabel!\n')
                                break


                                
            if self.exist=='yes':
                self.answer3=input('\nENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                if self.answer3=='0':
                    Menu()
                    break
                if self.answer3=='1':
                    continue
                else:
                    exit()
                    break
            else:
                print('\n\n..oops! this string doesnt exist\n please try again\n')
                self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                if self.answer3=='0':
                    Menu()

                if self.answer3=='1':

                    self.By_String()
                else:
                    exit()

    def By_Pattern(self): ## this method searches by re pattern

        back='this page is not availabel'
        with open ('task.csv',newline='')as csvfile:
            taskreader=csv.reader(csvfile,delimiter='|')
            file=list(taskreader)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
              '\n\n\n\n\n\n\n\n\n\n.....TASK SEARCH BY PATTERN WINDOW.......\n\n')
        while True: ## i used the while loop here to be able to ask the input again if the input was wrong
            
            with open ('task.csv',newline='')as csvfile:
                taskreader=csv.reader(csvfile,delimiter='|')
                file=list(taskreader)
            
            self.searchpattern=input('\n\nENTER A REGULAR EXPRESSION: ')
            self.exist='no'## i used this variable to check if the searched item exists

            ## accessing the files in the csv file
            for item in file[::2]:
                self.to_str=''.join(item)
                self.to_li=self.to_str.split(',')
                self.li_for_regex=[self.to_li[0],self.to_li[2]]
                self.li_for_regex_str=''.join(self.li_for_regex)
                
                
                ## checking if the task name or the note matches
                self.match=bool(re.search(r'{}'.format(self.searchpattern),self.li_for_regex_str))##true if it matches 
                
                
                
                if self.match==True :## if it mathces the following code executes
                    self.exist='yes'## this variable is used to know if the searched pattern exists
                    if self.to_li[0]!='task_name':## this code makes sure the heading is skiped
                        if self.to_li[2].lower()=='skip': ## this code checks if a note exists


                            ## here we print the answer in a nice format
                            print('\n\nTask name:  {}\nMinutes:  {}\nDate:  {}\n'
                                '\n'.format(self.to_li[0],self.to_li[1],self.to_li[3]))


                            try:
                                self.page=int(input('1 NEXT PAGE \n'
                                               '2 BACK : '))

                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                      '\n\n\n\n\n\n\n\n\n\n'
                                       '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if str(self.page)=='1':
                                    ## saving incase back is called
                                    if self.to_li[2].lower()=='skip':
                                        back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n'
                                             \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                       
                                    else:   
                                        back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                             \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                        continue
                                if str(self.page)=='2':
                                    
                                
                                    print(back)

                                    self.page=int(input('1 NEXT PAGE\n'
                                                        '2 BACK: '))

                                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                          '\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                           '\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if str(self.page) =='1' or str(self.page) =='2':
                                    continue
                                else:
                                    print('\n ..ooops! the page is not availabel!\n')
                                    break
                                        
                            except ValueError as Err:
                                print('\n ..ooops! the page is not availabel!\n')
                                break

                                

                        else:
                            print('\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                  '\n'.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3]))


                            try:
                                self.page=int(input('1 NEXT PAGE \n'
                                                    '2 BACK : '))


                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                      '\n\n\n\n\n\n\n\n\n\n'
                                       '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if str(self.page)=='1':
                                    ## saving incase back is called
                                    if self.to_li[2].lower()=='skip':
                                        back='''\n\nTask name:  {}\nMinutes :  {}\nDate:  {}\n
                                             \n'''.format(self.to_li[0],self.to_li[1],self.to_li[3])
                                       
                                    else:   
                                        back='''\n\nTask name:  {}\nMinutes:  {}\nNotes:  {}\nDate:  {}\n'
                                             \n'''.format(self.to_li[0],self.to_li[1],self.to_li[2],self.to_li[3])

                                        continue
                                if str(self.page)=='2':
                                    
                                
                                    print(back)

                                    self.page=int(input('1 NEXT PAGE\n'
                                                   '2 BACK: '))

                                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                                           '\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                if str(self.page) =='1' or str(self.page) =='2':
                                    continue
                                else:
                                    print('\n ..ooops! the page is not availabel!\n')
                                    break
                                        
                            except ValueError as Err:
                                print('\n ..ooops! the page is not availabel!\n')
                                break

                                
             ## if the searched value was found then the option to go back to menu or exit appears
            if self.exist=='yes':
                break
            if self.exist=='no':
                print('\n...oops! your search doesnt exist\n')
                continue

        self.answer3=input('\n\nENTER 1 TO DO ANOTHER SEARCH\n'
                           'ENTER 0 FOR MAIN MENU \n'
                           'ENTER ANY OTHER KEY TO EXIT: ')

        if self.answer3=='0':
            Menu()
        
        if self.answer3=='1':
            self.By_Pattern()
        else:
            exit()



class Delete_task:## this class is for deleting tasks 

    def Delete(self):
    


        while True:
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
                  '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n.....TASK DELETING WINDOW.......\n\n')
            
            with open ('task.csv',newline='')as csvfile:
                taskreader=csv.reader(csvfile,delimiter='|')
                file=list(taskreader)
                self.searchname=input('\n\nENTER task name : ')
                csvfile.close()
                self.check=input('\n\nARE YOU SURE YOU WANT TO DELETE THIS TASK \nY/N: ')## checks if we are sure about deleting
                if self.check.lower()=='y':
                    csvfile.close()
                    os.remove('task.csv')## this code deletes the csv file after i assign it to a 
                
                    
                    
                self.exist='no'
                for item in file[::2]:
                    self.to_str=''.join(item)
                    self.to_li=self.to_str.split(',')
                    self.se=self.to_li[0]
                    self.st_note=self.to_li[2]
                    self.count=0
                    if self.to_li[0]!='task_name':
                        
                       
                        if str(self.se)==self.searchname:
                            self.exist='yes'
                            
                        else:
                            ## here i save everything back except the log we wanted to delete
                            
                           


                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.to_li[0]),
                                                  'minutes':str(self.to_li[1]),
                                                  'notes':str(self.to_li[2]),
                                                  'date':str(self.to_li[3])
                                                  })
                


                if self.exist=='no':
                    print('\n\n..oops! this task name doesnt exist.\n please try again\n.')
                    self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                               'ENTER 0 FOR MAIN MENU \n'
                               'ENTER ANY OTHER KEY TO EXIT: ')
                    if self.answer3=='0':
                        Menu()

                    if self.answer3=='1':

                        self.Delete()
                    else:
                        exit()
                else:
                    break
        
        csvfile.close()

        self.answer3=input('\n\nENTER 1 TO DELETE ANOTHER TASK\n'
                           'ENTER 0 FOR MAIN MENU \n'
                           'ENTER ANY OTHER KEY TO EXIT: ')

        if self.answer3=='0':
            Menu()
        
        if self.answer3=='1':
            self.Delete()
        else:
            exit()



class Edit:## this class edits the log
    def Edit_task(self):
        print('\n\n............TASK EDIT WINDOW............')

        while True:

            with open ('task.csv',newline='')as csvfile:
                taskreader=csv.reader(csvfile,delimiter='|')
                file=list(taskreader)
                
                self.searchname=input('\n\nENTER task name : ')
                
                
                    
                
            
                            
                            
                self.exist='no'
                
                for item in file[::2]:
                    self.to_str=''.join(item)
                    self.to_li=self.to_str.split(',')
                    self.se=self.to_li[0]
                    self.st_note=self.to_li[2]
                    self.count=0
                    if self.to_li[0]!='task_name':
                        
                       
                        if str(self.se)==self.searchname:
                            self.exist='yes'
                                                    
                        
                                
                            
                if self.exist=='no':
                    print('\n\n..oops! this task name doesnt exist.\n please try again.\n\n')
                    self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                    if self.answer3=='0':
                        Menu()

                    if self.answer3=='1':

                        self.Edit_task()
                    else:
                        exit()
                else:
                    break
        

        while True:
                try:
                    self.choice=int(input('\n\n ENTER 1 TO EDIT THE TASK NAME\n'
                                     '\n\n ENTER 2 TO EDIT DATE\n'
                                     '\n\n ENTER 3 TO EDIT NOTE\n'
                                     '\n\n ENTER 4 TO EDIT MINUTE: '))
                except ValueError as Err:
                    print('\n\n....oops. your input was invalid.\n please try again.\n\n')
                    self.answer3=input('ENTER 1 TO DO ANOTHER SEARCH\n'
                                   'ENTER 0 FOR MAIN MENU \n'
                                   'ENTER ANY OTHER KEY TO EXIT: ')
                    if self.answer3=='0':
                        Menu()

                    if self.answer3=='1':

                        self.Edit_task()
                    else:
                        exit()

                check1=bool(str(self.choice)=='1')
                check2=bool(str(self.choice)=='2')
                check3=bool(str(self.choice)=='3')
                check4=bool(str(self.choice)=='4')
                if check1==True or check2==True or check3==True or check4==True:
                    break
                else:
                    print('\n\n...oops! your input was invalid.\n please try again\n\n')
                    self.answer3=input('ENTER 1 TO DO ANOTHER EDIT\n'
                                       'ENTER 0 FOR MAIN MENU \n'
                                       'ENTER ANY OTHER KEY TO EXIT: ')
                    if self.answer3=='0':
                        Menu()

                    if self.answer3=='1':

                        self.Edit_task()
                    else:
                        exit()
        
        if str(self.choice)=='1':
            self.new_taskname=input('ENTER THE NEW TASK NAME: ')

            self.check1=input('\n\nARE YOU SURE YOU WANT TO EDIT THIS TASK \nY/N : ')
            
        

        
            if self.check1.lower()=='y':
                csvfile.close()
                os.remove('task.csv')## this code deletes the csv file after i assign it to a variable

                            

                
                self.exist='no'
                for item in file[::2]:
                    self.to_str=''.join(item)
                    self.to_li=self.to_str.split(',')
                    self.se=self.to_li[0]
                    
                    self.st_note=self.to_li[2]

                    

                    
                    if self.to_li[0]!='task_name':
                        if str(self.se)!=self.searchname:
                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            self.exist='yes'
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.to_li[0]),
                                                  'minutes':str(self.to_li[1]),
                                                  'notes':str(self.to_li[2]),
                                                  'date':str(self.to_li[3])
                                                  })
                            
                                
                        else:

                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.new_taskname),
                                                  'minutes':str(self.to_li[1]),
                                                  'notes':str(self.to_li[2]),
                                                  'date':str(self.to_li[3])
                                                  })
                        csvfile.close()
            print('\n........TASK EDITED SUCESSFULLY.......\n\n')
            answer3=input('\n\nENTER 1 TO EDIT ANOTHER TASK\n'
                          'ENTER 0 FOR MAIN MENU \n'
                          'ENTER ANY OTHER KEY TO EXIT: ')

            if answer3=='0':
                Menu()
            if answer3=='1':
                self.Edit_task()
            else:
                exit()

        if str(self.choice)=='2':
            self.new_date=input('ENTER THE NEW DATE: ')
            self.check2=input('\n\nARE YOU SURE YOU WANT TO EDIT THIS TASK \nY/N : ')

            if self.check2.lower()=='y':
                os.remove('task.csv')## this code deletes the csv file after i assign it to a variable

                            

                
                self.exist='no'
                for item in file[::2]:
                    self.to_str=''.join(item)
                    self.to_li=self.to_str.split(',')
                    self.se=self.to_li[0]
                    
                    self.st_note=self.to_li[2]

                    

                    
                    if self.to_li[0]!='task_name':
                        if str(self.se)!=self.searchname:
                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            self.exist='yes'
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.to_li[0]),
                                                  'minutes':str(self.to_li[1]),
                                                  'notes':str(self.to_li[2]),
                                                  'date':str(self.to_li[3])
                                                  })
                            
                                
                        else:

                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.to_li[0]),
                                                  'minutes':str(self.to_li[1]),
                                                  'notes':str(self.to_li[2]),
                                                  'date':str(self.new_date)
                                                  })
                        csvfile.close()
            print('\n........TASK EDITED SUCESSFULLY.......\n\n')
            answer3=input('\n\nENTER 1 TO EDIT ANOTHER TASK\n'
                          'ENTER 0 FOR MAIN MENU \n'
                          'ENTER ANY OTHER KEY TO EXIT: ')

            if answer3=='0':
                Menu()
            if answer3=='1':
                self.Edit_task()
            else:
                exit()

        if str(self.choice)=='3':
            self.new_note=input('ENTER THE NEW NOTE: ')
            self.check3=input('\n\nARE YOU SURE YOU WANT TO EDIT THIS TASK \nY/N : ')
            
        

        
            if self.check3.lower()=='y':

                os.remove('task.csv')## this code deletes the csv file after i assign it to a variable

                            

                
                self.exist='no'
                for item in file[::2]:
                    self.to_str=''.join(item)
                    self.to_li=self.to_str.split(',')
                    self.se=self.to_li[0]
                    
                    self.st_note=self.to_li[2]

                    

                    
                    if self.to_li[0]!='task_name':
                        if str(self.se)!=self.searchname:
                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            self.exist='yes'
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.to_li[0]),
                                                  'minutes':str(self.to_li[1]),
                                                  'notes':str(self.to_li[2]),
                                                  'date':str(self.to_li[3])
                                                  })
                            
                                
                        else:

                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.to_li[0]),
                                                  'minutes':str(self.to_li[1]),
                                                  'notes':str(self.new_note),
                                                  'date':str(self.to_li[3])
                                                  })
                        csvfile.close()
            print('\n........TASK EDITED SUCESSFULLY.......\n\n')
            answer3=input('\n\nENTER 1 TO EDIT ANOTHER TASK\n'
                          'ENTER 0 FOR MAIN MENU \n'
                          'ENTER ANY OTHER KEY TO EXIT: ')

            if answer3=='0':
                Menu()
            if answer3=='1':
                self.Edit_task()
            else:
                exit()

        if str(self.choice)=='4':
            self.new_minute=input('ENTER THE NEW MINUTE: ')
            self.check2=input('\n\nARE YOU SURE YOU WANT TO EDIT THIS TASK \nY/N : ')
            
        

        
            if self.check2.lower()=='y':
                os.remove('task.csv')## this code deletes the csv file after i assign it to a variable

                            

                
                self.exist='no'
                for item in file[::2]:
                    self.to_str=''.join(item)
                    self.to_li=self.to_str.split(',')
                    self.se=self.to_li[0]
                    
                    self.st_note=self.to_li[2]

                    

                    
                    if self.to_li[0]!='task_name':
                        if str(self.se)!=self.searchname:
                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            self.exist='yes'
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.to_li[0]),
                                                  'minutes':str(self.to_li[1]),
                                                  'notes':str(self.to_li[2]),
                                                  'date':str(self.to_li[3])
                                                  })
                            
                                
                        else:

                            csvfile=open('task.csv','a') 
                            fieldnames = ['task_name','minutes','notes','date']
                            teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
                            teachwriter.writeheader()
                            teachwriter.writerow({'task_name':str(self.to_li[0]),
                                                  'minutes':str(self.new_minute),
                                                  'notes':str(self.to_li[2]),
                                                  'date':str(self.to_li[3])
                                                  })
                        csvfile.close()
        print('\n........TASK EDITED SUCESSFULLY.......\n\n')
        answer3=input('\n\nENTER 1 TO EDIT ANOTHER TASK\n'
                      'ENTER 0 FOR MAIN MENU \n'
                      'ENTER ANY OTHER KEY TO EXIT: ')

        if answer3=='0':
            Menu()
        if answer3=='1':
            self.Edit_task()
        else:
            exit()

        
        

       

        answer3=input('\n\nENTER 1 TO EDIT ANOTHER TASK\n'
                      'ENTER 0 FOR MAIN MENU \n'
                      'ENTER ANY OTHER KEY TO EXIT: ')

        if answer3=='0':
            Menu()
            
        if answer3=='1':
            self.Edit_task()
        else:
            exit()




            
                
                         
def Menu():
    
    print('\n...........MAIN MENU.........\n\n')

    while True:
        try:
            selection=int(input('ENTER 1 TO LOG NEW TASK\n'
                        'ENTER 2 TO SEARCH PREVIOUS ENTRY\n'
                        'ENTER 3 TO EDIT PREVIOUS ENTRY\n'
                        'ENTER 4 TO DELETE ENTRY \n'
                        'ENTER 0 TO QUIT    :'))

            if str(selection)=='0':
                exit()
            
            if str(selection)=='1' or str(selection)=='2' or str(selection)=='3' or str(selection)=='4':
                
                break
               
            else:
                print('\n...oops! your input was invalid\nTry again.\n')
                continue
        except ValueError as Err:
            print('\n..OOPS! your input was invalid.\n Try again.\n')


    if str(selection)=='1':

        while True:
            print('\n...... NEW TASK ENTRY WINDOW .......\n')
            
            task_name=input('\nENTER TASK NAME: ')
    
        ### handling the error
            while True:
                try:
                    minutes= int(input('\nENTER MINUTES SPENT ON TASK: '))
                    
                except ValueError as Err:
                    print('\n\n......oops! you have to use numbers only\nplease try again')
                else:
                    break
            
        
        
            notes=input('\nENTER NOTES OR ENTER SKIP: ')
            d=datetime.datetime.now()
            date=d.strftime('%m-%d-%Y')
            new=New_entry(task_name,minutes,notes,date)
            new.saving()
            answer3=input('\n\nENTER 1 TO LOG ANOTHER TASK\n'
                          'ENTER 0 FOR MAIN MENU \n'
                          'ENTER ANY OTHER KEY TO EXIT: ')

            if answer3=='0':
                Menu()
            
            if answer3=='1':
                continue
            else:
                exit()

            
    if str(selection)=='2':
        search=Look_up()
        print('\n\n.....TASK LOOK UP WINDOW......\n\n')

       
        csvfile=open('task.csv','a') ## here i created empty csv file just incase the user tries
                                             ## to search before saving any work log.
        csvfile.close()
            
        while True:
                try:
                    lookup_selection=int(input('ENTER 1 TO FIND BY DATE\n'
                                           'ENTER 2 TO FIND BY MINUTES\n'
                                           'ENTER 3 TO FIND BY EXACT STRING\n'
                                           'ENTER 4 TO FIND BY PATTERN  \n'
                                           'ENTER 5 TO FIND BY RANGE OF DATE :'))


                    if str(lookup_selection)=='1' or str(lookup_selection)=='2'or str(lookup_selection)=='3' or str(lookup_selection)=='4'or str(lookup_selection)=='5':
                    
                        if str(lookup_selection)=='1':
                            search.By_Date()

                        if str(lookup_selection)=='2':
                            search.By_Time()
                        if str(lookup_selection)=='3':
                            search.By_String()
                        if str(lookup_selection)=='4':
                            search.By_Pattern()
                        if str(lookup_selection)=='5':
                            search.By_range()
                    else:
                        print('...oops! your input was invalid.\n Try again.')
                        continue
                except ValueError as Err:
                    print('...oops! your input was invalid.\n Try again.')

                

    if str(selection)=='4':
        csvfile=open('task.csv','a')
        csvfile.close()
        
        delete=Delete_task()
        delete.Delete()
    if str(selection)=='3':

        csvfile=open('task.csv','a')
        csvfile.close()
        edit=Edit()
        edit.Edit_task()
    
Menu()
        
              
              
              

    
    
