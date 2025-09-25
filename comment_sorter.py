# Started 9/24/2025

class CommentSorter:
    def __init__(self):
        
        self.all_file_lines: list[str] = (
            []
        )  # Holds every single commend + adds a line infront of them
        self.hashtag_comments: list[str] = (
            []
        )  # Holds all the valid comments from "grab_comments" function
        self.inprogress_comments: list[str] = (
            []
        )  # Holds all the comments that have "(In Progress)" or "In Progress:" in them
        self.todo_comments: list[str] = (
            []
        )  # Holds all the comments that have "(To Do)"" or "To Do" in them
        self.miscellaneous_comments: list[str] = (
            []
        )  # Holds all the comments that dont have "To Do" or "In Progress" in them at all        
        
        self.empty_list_inprogress: list[str] = (
            []
         )  # This will hold our trimmed strings from the function below for future use in other functions
        
        self.empty_miscellaneous_comments_list: list[str] = []
        # -------------- "Grab Comments" Section -------------- #



    def grab_all_lines(self, read_file: str) -> None:

        if isinstance(read_file, str) == False:
            print(ValueError("Make sure the file is a string."))   
        # ^ Forces user to have the file be a string
    
        file_to_str = str(read_file)
        file_to_str.replace("\\", "/")
        file_to_str.replace("\\", "\\\\")
        # ^ Makes sure every file is formated correctly

        with open(read_file, "r") as file:
            for line_number, line in enumerate(file):
                formatted_lines = f"{line}(Line: {line_number + 1})"  # Adds line number infront of the line Eg. 245 print("hello word") | +1 because without it, the line number is 1 number below the actual real line number in the pyton code
                self.all_file_lines.append(formatted_lines)

    def grab_comments(self) -> None:
            for line in self.all_file_lines: 
                trim_white_space = line.strip()
                if trim_white_space.__contains__("#"):
                    remove_text_before_hastag = str(trim_white_space.split("#", 1)[1] )
                    self.hashtag_comments.append(remove_text_before_hastag) 

    def grab_inprogress(self) -> None:
        for comment in self.hashtag_comments:
            if comment.__contains__("(In Progress)") or comment.__contains__(
                "In Progress:"
            ):
                self.inprogress_comments.append(comment)

    def grab_todo(self):
        for comment in self.hashtag_comments:
            if comment.__contains__("(To Do)") or comment.__contains__("To Do:"):
                self.todo_comments.append(comment)

    def grab_miscellaneous_comments(self) -> (
        None
    ):  # (Gets Comments that neither contain "To Do", or "In Progress")
        for comment in self.hashtag_comments:
            if (
                "(To Do)" not in comment
                and "To Do:" not in comment
                and "(In Progress)" not in comment
                and "In Progress:" not in comment
            ):
                self.miscellaneous_comments.append(comment)




    # -------------- "Clean & Print Comments" Section -------------- #



    def clean_inprogress_comments(self) -> (
        None
    ):  # Removes the "#" and "In Progress" text from the comments, making them easier to read
        for comment in self.inprogress_comments:
            trimmed_comment = comment.strip()
            trimmed_comment_lowercase = trimmed_comment.lower() # Makes it lowercase so that both upper and lowercase letters get processed at the same time, making it more leanient for mistakes
            
            if trimmed_comment_lowercase.__contains__("in progress:"):
                replace_todo_and_hashtag = comment.lower().replace("In Progress:", "").replace(
                    "#", ""
                )
                self.empty_list_inprogress.append(replace_todo_and_hashtag.strip())

            elif trimmed_comment_lowercase.__contains__("(in progress)"):
                replace_todo_and_hashtag = comment.lower().replace("(in progress)", "").replace(
                    "#", ""
                )
                self.empty_list_inprogress.append(replace_todo_and_hashtag.strip())


    def print_formatted_inprogress_comments(self):
        print(
            '\n ------------- Here are all your tasks that are "In Progress"! ------------- \n'
        )
        for comment in self.empty_list_inprogress:
            print(f"In Progress: {comment.capitalize()} \n")



    empty_list_todo: list[str] = (
        []
    )  # This will hold our trimmed strings from the function below for future use in other functions

    def clean_todo_comments(self) -> (
        None
    ):  # Removes the "#" and "To Do" text from the comments, making them easier to read
        for comment in self.todo_comments:
            trimmed_comment = comment.strip()
            trimmed_comment_lowercase = trimmed_comment.lower() # Makes it lowercase so that both upper and lowercase letters get processed at the same time, making it more leanient for mistakes
            if trimmed_comment_lowercase.__contains__("to do:"):
                replace_todo_and_hashtag = comment.lower().replace("to do:", "").replace("#", "")
                self.empty_list_todo.append(replace_todo_and_hashtag.strip()) 

            elif trimmed_comment_lowercase.__contains__("(to do)"):
                replace_todo_and_hashtag = comment.lower().replace("(to do)", "").replace("#", "")
                self.empty_list_todo.append(replace_todo_and_hashtag.strip()) 


    def print_formatted_todo_comments(self) -> None:
        print('\n ------------- Here are all your "To Do" tasks! ------------- \n')
        for comment in self.empty_list_todo:
            print(f"To Do: {comment.capitalize()} \n") 


    
 

    def clean_miscellaneous_comments(self) -> None:
        for comment in self.miscellaneous_comments:   
            replace_hashtag = comment.replace("#", "")
            self.empty_miscellaneous_comments_list.append(replace_hashtag.strip()) 


    def print_clean_miscellaneous_comments(self) -> None:
        print(
            '\n ------------- Here are all your "Miscellaneous" comments! ------------- \n'
        )
        for comment in self.empty_miscellaneous_comments_list:
            print(f"{comment.capitalize()} \n")
            
            
            
            
    # -------------- "Call Functions Section -------------- #

    def format_comments(self, read_file: str):
        self.grab_all_lines(read_file)
        self.grab_comments()
        self.grab_inprogress()
        self.grab_todo()
        self.grab_miscellaneous_comments()
        
        self.clean_todo_comments()
        self.clean_inprogress_comments()
        self.clean_miscellaneous_comments()

        self.print_formatted_todo_comments()
        self.print_formatted_inprogress_comments()
        self.print_clean_miscellaneous_comments()
