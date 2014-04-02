#Players
bryce_year1 = {"year": "2012", "team": "Washington Nationals", "kind": "hitter", "games": 139, "pa": 597, "avg": .270, "obp": .340, "slg": .477, "hr": 22, "rbi": 59 }
bryce_year2 = {"year": "2013", "team": "Washington Nationals", "kind": "hitter", "games": 118, "pa": 497, "avg": .274, "obp": .368, "slg": .486, "hr": 20, "rbi": 58 }
bryce_player = { "name": "Bryce Harper", "number": 34, "position": "OF",  "social": "@Bharper3407" ,"bats": "R", "throws": "L", "height": 74, "weight": 230, "school": "College of Southern Nevada"}
bryce_image = "http://mlb.com/images/players/525x330/547180.jpg"
bryce_years = [bryce_year1, bryce_year2]

yu_year1 = {"year": "2012", "team": "Texas Rangers", "kind": "pitcher", "games": 29, "w": 16, "l": 9, "era": 3.90, "gs": 29, "s": 0, "whip": 1.280, "ip": 191.1}
yu_year2 = { "year": "2013", "team": "Texas Rangers", "kind": "pitcher", "games": 32, "w": 13, "l": 9, "era": 2.83, "gs": 32, "s": 0, "whip": 1.073, "ip": 209.2}
yu_image = "http://mlb.com/images/players/525x330/506433.jpg"
yu_player = { "name": "Yu Darvish", "number": 11, "position": "P", "social": "@faridyu" ,"bats": "R", "throws": "R", "height": 77, "weight": 225, "school": "Sendai, Japan" }
yu_years = [yu_year1, yu_year2]

mike_year1 = {"year": "2011", "team": "Los Angeles Angels of Anaheim", "kind": "hitter", "games": 40, "pa": 135, "avg": .220, "obp": .281, "slg": .390, "hr": 5, "rbi": 16 }
mike_year2 = {"year": "2012", "team": "Los Angeles Angels of Anaheim", "kind": "hitter", "games": 139, "pa": 639, "avg": .326, "obp": .399, "slg": .564, "hr": 30, "rbi": 83 }
mike_year3 = {"year": "2013", "team": "Los Angeles Angels of Anaheim", "kind": "hitter", "games": 157, "pa": 716, "avg": .323, "obp": .432, "slg": .557, "hr": 27, "rbi": 97 }
mike_image = "http://mlb.com/images/players/525x330/545361.jpg"
mike_player = { "name": "Mike Trout", "number": 27, "position": "OF", "social": "@Trouty20" ,"bats": "R", "throws": "R", "height": 74, "weight": 230, "school": "Millville Senior HS, Millville, NJ" }
mike_years = [mike_year1, mike_year2, mike_year3]

bryce = dict(player=bryce_player, image=bryce_image, years=bryce_years)
mike = dict(player=mike_player, image=mike_image, years=mike_years)
yu = dict(player=yu_player, image=yu_image, years=yu_years)

# Leave out yu because we don't have a Texas team in the DB
players = [bryce, mike, yu]