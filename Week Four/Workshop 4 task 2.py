# Name: Nimuthu Ganegoda
# Student ID: 10695889

def print_heading(heading_text ="Example Heading Text", width = 30):
    #heading_text = 'Example Heading Text'
    ideal_width = len(heading_text) + 2
    
    if width < ideal_width:
        width = ideal_width 
        
    print('=' * width)
    print('|' + heading_text.center(width -2) + '|')
    print('=' *  width)

print_heading("Example Heading Text", 10)