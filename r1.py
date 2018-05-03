import csv
import sqlite3
from datetime import datetime

db = sqlite3.connect('/home/andre/Downloads/premier/databasefile.sqlite')
cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS teams')
cursor.execute('DROP TABLE IF EXISTS matchs')
cursor.execute('CREATE TABLE teams(id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('CREATE TABLE matchs(id INTEGER PRIMARY KEY, home_team INTEGER, away_team INTEGER, date DATE, home_score INTEGER, away_score INTEGER);')
db.commit()

def convertDate(dateString):
  return datetime.strptime(dateString, '%d/%m/%y').strftime("%Y-%m-%d")

def findTeamId(teamName):
  teamName = teamName.replace('\'', '')
  cursor.execute('SELECT id from teams where name = \'' + teamName + '\'')
  team = cursor.fetchone()
  if team is None: 
    cursor.execute('INSERT INTO teams(name) VALUES(:name)', {'name': teamName})
    db.commit()
    return cursor.lastrowid
  return team[0]

def saveMatch(homeTeam, awayTeam, date, homeScore, awayScore):
  homeTeamId = findTeamId(homeTeam)
  awayTeamId = findTeamId(awayTeam)
  matchData = {'homeTeam': homeTeamId, 'awayTeam': awayTeamId, 'date': date, 'homeScore': homeScore, 'awayScore': awayScore}
  cursor.execute('INSERT INTO matchs(home_team, away_team, date, home_score, away_score) VALUES(:homeTeam, :awayTeam, :date, :homeScore, :awayScore)', matchData)
  db.commit()

def handleFile(filename):
  with open(filename, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      if row[0] == 'E0':
        date = convertDate(row[1])
        homeTeamName = row[2]
        awayTeamName = row[3]
        homeScore = int(row[4])
        awayScore = int(row[5])
        saveMatch(homeTeamName, awayTeamName, date, homeScore, awayScore)

handleFile('E24.csv')
handleFile('E23.csv')
handleFile('E22.csv')
handleFile('E21.csv')
handleFile('E20.csv')
handleFile('E19.csv')
handleFile('E18.csv')
handleFile('E17.csv')
handleFile('E16.csv')
handleFile('E15.csv')
handleFile('E14.csv')
handleFile('E13.csv')
handleFile('E12.csv')
handleFile('E11.csv')
handleFile('E10.csv')
handleFile('E09.csv')
handleFile('E08.csv')
handleFile('E07.csv')
handleFile('E06.csv')
handleFile('E05.csv')
handleFile('E04.csv')
handleFile('E03.csv')
handleFile('E02.csv')
handleFile('E01.csv')
handleFile('E00.csv')

db.close()