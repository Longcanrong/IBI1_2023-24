class students:
    def __init__(stu, name, major, code_portfolio_score, group_project_score, exam_score):
        stu.name = name
        stu.major = major
        stu.code_portfolio_score = code_portfolio_score
        stu.group_project_score = group_project_score
        stu.exam_score = exam_score

    def print_details(stu):
        print("Name: {}, Major: {}, Code Portfolio Score: {}, Group Project Score: {}, Exam Score: {}".format(stu.name, stu.major, stu.code_portfolio_score, stu.group_project_score, stu.exam_score))


student = students(name="Loong",major="BMS",code_portfolio_score=90,group_project_score=90,exam_score=88)
student.print_details()