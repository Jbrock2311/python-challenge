{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "pybank = os.path.join('budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "--------------------------------------------------\n",
      "Total Months:86\n",
      "Total: $38382578\n",
      "Average Change: $-2315.1176470588234\n",
      "Greatest Increase in Profits: Jan-2012($1926159)\n",
      "Greatest Decrease in Profits: Aug-2013($-2196167)\n"
     ]
    }
   ],
   "source": [
    "#import os\n",
    "#import csv\n",
    "\n",
    "#pybank = os.path.join('budget_data.csv')\n",
    "\n",
    "dates=[]\n",
    "rev =[]\n",
    "overall_monthly_change = []\n",
    "\n",
    "count= -1\n",
    "start = 0\n",
    "total_change=0\n",
    "\n",
    "with open(pybank,newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    #skip the header row\n",
    "    next(csvreader)\n",
    "    \n",
    "    #collect info in lists\n",
    "    for row in csvreader:\n",
    "        dates.append(row[0])\n",
    "        rev.append(row[1])\n",
    "    \n",
    "    #total number of months \n",
    "    total_months = len(dates)\n",
    "    \n",
    "    #total amount of \"Profit/Losses\"\n",
    "    total_revenue = 0\n",
    "    i=0\n",
    "    for i in range(total_months):\n",
    "        total_revenue = total_revenue +int(rev[i])\n",
    "                    #for row in csvreader: WHY DON'T THESE WORK?\n",
    "                        #net_total = float(row[1]) gives 0\n",
    "                    #net_total = sum(float(row[1]) for row in csvreader)\n",
    "\n",
    "    #average of the changes in \"Profit/Losses\" over the entire period\n",
    "    \n",
    "    csvfile.seek(0)\n",
    "    next(csvreader) \n",
    "    \n",
    "    for row in csvreader:\n",
    "        \n",
    "        count = count +1\n",
    "        end_profit = int(row[1])\n",
    "        monthly_changes = end_profit - start\n",
    "        \n",
    "        #add changes to list\n",
    "        overall_monthly_change.append(monthly_changes)\n",
    "\n",
    "       \n",
    "        #read in new loop the start is our prior end\n",
    "        total_change = total_change + monthly_changes\n",
    "        start = end_profit\n",
    "        \n",
    "        \n",
    "    #calc avg\n",
    "    overall_monthly_change.pop(0)\n",
    "    avg_change = sum(overall_monthly_change)/ count\n",
    "    \n",
    "    #greatest increase in profits(date and amount) over the entire period\n",
    "    #greatest decrease in losses (date and amount) over the entire period\n",
    "    greatest_inc = max(overall_monthly_change)\n",
    "    inc_date = dates[overall_monthly_change.index(greatest_inc)]\n",
    "    greatest_dec = min(overall_monthly_change)\n",
    "    dec_date = dates[overall_monthly_change.index(greatest_dec)]\n",
    "\n",
    "    #print out results\n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"--------------------------------------------------\")\n",
    "    print(\"Total Months:\" + str(total_months)) \n",
    "    print(\"Total: $\" + str(total_revenue))\n",
    "    print(\"Average Change: $\" + str(avg_change))\n",
    "    print(\"Greatest Increase in Profits: \" + str(inc_date) + \"($\" + str(greatest_inc) + \")\")\n",
    "    print(\"Greatest Decrease in Profits: \" + str(dec_date) + \"($\" + str(greatest_dec) + \")\")\n",
    "\n",
    "    \n",
    "    pybank_final = (\"pybank_final.txt\")\n",
    "with open(pybank_final, \"w\") as txtfile:\n",
    "    txtfile.write(\"  Financial Analysis  \\n\")\n",
    "    txtfile.write(\"----------------------\\n\")\n",
    "    txtfile.write(\"Total Months:\" + str(total_months) + \"\\n\") \n",
    "    txtfile.write(\"Total: $\" + str(total_revenue) + \"\\n\")\n",
    "    txtfile.write(\"Average Change: $\" + str(avg_change) + \"\\n\")\n",
    "    txtfile.write(\"Greatest Increase in Profits: \" + str(inc_date) + \"($\" + str(greatest_inc) + \")\" + \"\\n\")\n",
    "    txtfile.write(\"Greatest Decrease in Profits: \" + str(dec_date) + \"($\" + str(greatest_dec) + \")\" + \"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
