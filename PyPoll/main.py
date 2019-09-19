{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "---------------------\n",
      "Total Votes: 3521001\n",
      "---------------------\n",
      "Khan: 63% + (2218231)\n",
      "Correy: 20% + (704200)\n",
      "Li: 14% + (492940)\n",
      "O'Tooley: 3% + (105630)\n",
      "---------------------\n",
      "Winner: Khan\n",
      "---------------------\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "pypoll = os.path.join('election_data.csv')\n",
    "\n",
    "num_votes = 0\n",
    "candidate = \"\"\n",
    "cand_votes = {}\n",
    "cand_percent = {}\n",
    "win = 0\n",
    "winner = \"\"\n",
    "\n",
    "\n",
    "with open(pypoll,newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    #skip the header row\n",
    "    next(csvreader)\n",
    "    \n",
    "    for row in csvreader:\n",
    "        \n",
    "        num_votes = num_votes + 1\n",
    "        \n",
    "        candidate = row[2]\n",
    "        \n",
    "        if candidate in cand_votes:\n",
    "            cand_votes[candidate] = cand_votes[candidate] + 1\n",
    "        else:\n",
    "            cand_votes[candidate] = 1\n",
    "       \n",
    "for cand, vote_count in cand_votes.items():\n",
    "        cand_percent[cand] = '{0:.0%}'.format(vote_count/num_votes)\n",
    "        if vote_count > win:\n",
    "            win = vote_count\n",
    "            winner = cand\n",
    "\n",
    "print(\"Election Results\")\n",
    "print(\"---------------------\")\n",
    "print(f\"Total Votes: {num_votes}\")\n",
    "print(\"---------------------\")\n",
    "for cand, vote_count in cand_votes.items():\n",
    "    print(f\"{cand}: {cand_percent[cand]} + ({vote_count})\")\n",
    "print(\"---------------------\")\n",
    "print(f\"Winner: {winner}\")\n",
    "print(\"---------------------\")\n",
    "\n",
    "pypoll_final = (\"pypoll_final.txt\")\n",
    "with open(pypoll_final, \"w\") as txtfile:\n",
    "    txtfile.write(\"Election Results \\n\")\n",
    "    txtfile.write(\"----------------------\\n\")\n",
    "    txtfile.write(f\"Total Votes: {num_votes}\" + \"\\n\") \n",
    "    txtfile.write(\"----------------------\\n\")\n",
    "    for cand, vote_count in cand_votes.items():\n",
    "        txtfile.write(f\"{cand}: {cand_percent[cand]} + ({vote_count})\" + \"\\n\")\n",
    "    txtfile.write(\"----------------------\\n\")\n",
    "    txtfile.write(f\"Winner: {winner}\"+ \"\\n\")\n",
    "    txtfile.write(\"----------------------\\n\")"
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
