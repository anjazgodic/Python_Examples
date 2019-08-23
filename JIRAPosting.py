from jira import JIRA
import os
jira = JIRA(‘yourserver/‘, basic_auth=(‘yourusername’, ‘yourpassword’))

issue_list = [‘IS-1’, ‘IS-5’, ‘IS-2’]

#FOR EACH OF THE ISSUES IN WHICH YOU WANT TO POST, WRITE WHAT DO YOU WANT TO POST
post_dict = {
                ‘IS-1’: ['comment', 'attachment'], 
                ‘IS-5’: ['attachment'], 
                ‘IS-2’: ['transitions']
                }

#FOR EACH OF THE ISSUES IN WHICH YOU WANT TO POST A COMMENT, WRITE WHAT COMMENT YOU WANT TO POST 
comment_dict = {
                ‘IS-1’: 'final test with if statements IS-1 [www.github.com]',
                ‘IS-5’: 'final test IS-5’, 
                ‘IS-2’: 'final test IS-4’
                }

#FOR EACH OF THE ISSUES IN WHICH YOU WANT TO POST A ATTACHMENT, WRITE THE PATH TO THE ATTACHMENT YOU WANT TO POST 
attachment_dict = {
                    'IS-1': '//10.10.1.5/Analytics/TeamMembers/name/working/attach1.png', 
                    'IS-5': '//10.10.1.5/Analytics/TeamMembers/name/working/attach2.png', 
                    'IS-2': '//10.10.1.5/Analytics/TeamMembers/name/working/attach3.png'
                    }

#Code to see which transitions are available
#for item in issue_list:
    #issue = jira.issue(item)
    #transitions = jira.transitions(issue)
    #print(transitions)
    
#FOR EACH OF THE ISSUES IN WHICH YOU WANT TO POST A TRANSITION, WRITE WHAT TRANSITION NUMBER YOU WANT TO POST 
status_dict = {
                'IS-1': '3', #3=Done, 4=In Progress, 
                'IS-5': '4', 
                'IS-2': '4'
                }

#FOR EACH OF THE ISSUES IN WHICH YOU WANT TO POST A RESOLUTION, WRITE WHAT RESOLUTION NUMBER YOU WANT TO POST 
resolution_dict = {
                'IS-1': '3', 
                'IS-5': '3', 
                'IS-2': '3'
                }
                
for item in issue_list:
    issue = jira.issue(item)
    for post in post_dict[item]:
        if post=='comment':
            comment = jira.add_comment(item, comment_dict[item])
        if post=='attachment':
            attachment = jira.add_attachment(issue=item, attachment=attachment_dict[item]) 
        if post=='transitions':
            transition = jira.transition_issue(item, status_dict[item], resolution={'id': resolution_dict[item]})
   

#NOTES ON DIRECTORIES IN WINDOWS
#os.chdir('Z:\TeamMembers\name\working') #use backwards slashes when specifying letter of mount
#os.chdir('//10.10.1.5/Analytics/TeamMembers/name/working') #use forward slashes when specifying IP
