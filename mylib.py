import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # years = np.array([2005,2006,2007,2011])
# # grade = np.array([54.5,34,77,60])

# # plt.plot(grade,years)
# # plt.show()


# years = np.array([2005,2006,2007,2011])
# grade = np.array([54.5,34,77,60])

# plt.plot(grade,years)
# plt.title("my academic grades")
# plt.xlabel("years")
# plt.ylabel("grades")
# plt.grid()
# plt.show()

        #pie graph

# marks=np.array(["maths","ppa","cfoa","bc","pom"])
# marks=np.array([60,45,89,77,90])
# plt.legend(marks)
# plt.pie(marks)
# plt.title("sem1")
# plt.show()



            #bar graph
years = np.array([2005,2006,2007,2011])
grade = np.array([54.5,34,77,60])

plt.bar(years,grade)
plt.title("my academic grades")
plt.xlabel("years")
plt.ylabel("grades")
plt.grid()
plt.show()


#