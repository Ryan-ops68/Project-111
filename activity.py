from os import stat
import pandas as pd
import csv
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
def random_set_of_means(counter): 
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data [random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "mean"))
    fig.show()
mean_list = []
for i in range (0,100):
    set_of_means = random_set_of_means(30)
    mean_list.append(set_of_means)
show_fig(mean_list)
mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
print ("Mean of Sampling Distribution is ", mean)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(std_deviation*2), mean+(std_deviation*2)
third_std_deviation_start, third_std_deviation_end = mean-(std_deviation*3), mean+(std_deviation*3)
fig = ff.create_distplot([mean_list],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0,0.17], mode = "lines", name = "first std deviation start"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0,0.17], mode = "lines", name = "first std deviation end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,0.17], mode = "lines", name = "second std deviation start"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17], mode = "lines", name = "second std deviation end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0,0.17], mode = "lines", name = "third std deviation start"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17], mode = "lines", name = "fthird std deviation end"))
fig.show()

