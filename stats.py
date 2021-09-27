import statistics
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")

mList=df["middle school"].to_list()
hList=df["hight school"].to_list()

mMean=statistics.mean(mList)
mMode=statistics.mode(mList)
mMedian=statistics.median(mList)
mStd=statistics.stdev(mList)

hMean=statistics.mean(hList)
hMode=statistics.mode(hList)
hMedian=statistics.median(hList)
hStd=statistics.stdev(hList)

mStart, mEnd = mMean-mStd, mMean+mStd
hStart, mEnd = hMean-hStd, hMean+hStd

std1=[result for result in data if result > firstStd_start and result < firstStd_end]