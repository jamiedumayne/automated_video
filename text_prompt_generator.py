import datetime

today = datetime.datetime.now()

os.chdir(file_path+"scripts/")
used_prompts_df = pd.read_csv("used_prompts.txt")
used_prompts_df[' date'] = used_prompts_df[' date'].astype(str)

today_str = str(today.day) + str(today.month) + str(today.year)

#only get text prompt if there's no prompt for today
if used_prompts_df[' date'].eq(today_str).any() == False:
    #get text prompt
    prompts_doc = open('prompts.txt','r')
    prompts = prompts_doc.read()
    prompts_list = prompts.split("\n")
    prompts_doc.close()

    #randomly select an item from the list
    selection = prompts_list[random.randint(0, len(prompts_list))]
    print(selection)

    #stops the same prompt being selected again
    while used_prompts_df['prompt'].eq(selection).any() == True:
        selection = prompts_list[random.randint(0, len(prompts_list))]
        
    #add current selection to list of used prompts
    file = open("used_prompts.txt", "a")
    file.write(selection + ", " + str(today.day) + str(today.month) + str(today.year) + "\n")
    file.close()

#create used prompts file
#my_file = open("test_file.txt", "w")
#my_file.write("prompt, date,\n")
#my_file.write("penguin, 132023,\n")
#my_file.close()