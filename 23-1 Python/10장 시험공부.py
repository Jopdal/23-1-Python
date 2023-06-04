def map_student_language(**student_language) :
    for name in student_language.keys() :
        print("%s 님의 수강 언어 ==> %s"%(name,student_language[name]))
        
map_student_language(민석='Python', 민서='Java', 주환='Ruby')