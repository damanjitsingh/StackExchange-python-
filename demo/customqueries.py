from __future__ import print_function

# Same directory hack
import sys
sys.path.append('.')
sys.path.append('..')

try:
    get_input = raw_input
except NameError:
    get_input = input

user_api_key = get_input("Please enter an API key if you have one (Return for none):")
if not user_api_key: user_api_key = None

import stackexchange
site = stackexchange.Site(stackexchange.StackOverflow, app_key=user_api_key)

'''
e.g. find all the questions with tag name python.
this method returns a list of questions
https://api.stackexchange.com/docs/advanced-search
'''
def questionsTaggedWith():
    pages = int(get_input("Please enter number of pages of result you want to see!"))
    #result = site.search_advanced(q='python')
    result = site.search_advanced(sort='activity',tagged='python',accepted='false')
    
    
    page=1
    while page<=pages and result.has_more==True:
        print("questions with tag python on page..",page,end='\n')
        numQuestions = len(result)
        print("Number of questions tagged with python.",numQuestions)
    
        i = 0
        while i<numQuestions:
            print('Question: ',result[i].title,' and is tagged with ',result[i].tags,end='\n')
            i+=1
        result = result.fetch_next()
        page+=1

def questionsWithTitle():
    pages = int(get_input("Please enter number of pages of result you want to see!"))
    result = site.search_advanced(sort='activity',title='static code analysis')
    
    
    page=1
    while page<=pages and result.has_more==True:
        print("static analysis questions on page..",page,end='\n')
        numQuestions = len(result)
        print("Number of questions having static analysis in the title.",numQuestions)
    
        i = 0
        while i<numQuestions:
            print('Question: ',result[i].title,end='\n')
            i+=1
        result = result.fetch_next()
        page+=1
    
def getAllTags():
    pages = int(get_input("Please enter number of pages of tags you want to see!"))
    tags = site.all_tags()
    
    page=1
    while page<=pages and tags.has_more==True:
        print("tags on page..",page,end='\n')
        tagsNum = len(tags)
        print("Number of tags.",tagsNum)
    
        i = 0
        while i<tagsNum:
            print(tags[i].name)
            i+=1
        tags = tags.fetch_next()
        page+=1
    

        
if __name__ == '__main__':
    questionsWithTitle()
    