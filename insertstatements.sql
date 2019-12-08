--populating sample zip_code

-- populating sample users; number uids represent emails for now
insert into ruser values('0', 'Animated Andy', 'password123', 'I talk a lot, and really fast', 27708);
insert into ruser values('1', 'Ballistic Ben', 'password124', 'I am libertarian!', 27708);
insert into ruser values('2', 'Sadistic Sammy', 'password125', 'My favorite color is blue', 27708);
insert into ruser values('3', 'Emo Tommy', 'password126', 'I hate everything happy and everyone hates me' , 27708);
insert into ruser values('4', 'Amphibious Abby', 'password127', 'Not sure why Im on here', 27708);
insert into ruser values('5', 'Mellow Minsoo', 'password128', 'Bro!', 27705);
insert into ruser values('6', 'Catastrophic Claire', 'password129', 'Does this picture make my face look fat?', 27705);
insert into ruser values('7', 'Elephant Elijah', 'password130', 'I sometimes lay on the floor and pretend Im a carrot', 27708);
insert into ruser values('8', 'Needy Nicholas', 'password131', 'I play guitar sometimes', 27708);
insert into ruser values('9', 'Random Ruth', 'password132', 'Still not over my ex-boyfriend', 27708);

-- populating sample community
insert into community values('Music', 'Those who enjoy going to concerts with friends or want to join a band');
insert into community values('Animals', 'Like to look at animals? Hunt? Talk about biology? Heres your group!');
insert into community values('Games', 'Board games, tabletop RPG, online games, we got them all');
insert into community values('Sports', 'Whoever wants to watch or play');
insert into community values('Nightlife', 'What came before part b? Partaaaaaaaaay!');

  -- populating sample subcommunity
insert into subcommunity values('Music', 'Playing together', 'Looking for a bass player');
insert into subcommunity values('Animals', 'Birdwatching', 'Some great parks around that we can check out!');
insert into subcommunity values('Games', 'Dungeons and Dragons', 'Looking for a campaign');
insert into subcommunity values('Sports', 'Football', 'Those who enjoy watching the NFL on weekends');
insert into subcommunity values('Nightlife', 'Trivia Nights', 'Theres always a trivia night somewhere!');
insert into subcommunity values('Nightlife', 'Bar hopping', 'Hit those Durham bars, usually Friday/Saturday nights');

-- populating sample GROUPS
insert into groups values('a', 'Bluegrass Musicians', 'Music', 'Playing together', 27708, 'private', 'Looking for a bass player -- auditions coming soon!');
insert into groups values('b', 'Animal Lovers', 'Animals', NULL, 27708, 'public', 'We stalk Nugget and post updates about where she is');
insert into groups values('c', 'Any games for fun!', 'Games', NULL, 27708, 'private', 'Board game fans at Duke, raise your hands!');
insert into groups values('d', 'PATRIOTS FANS ONLY', 'Sports', 'Football', 27705, 'public', 'Duke football game watch parties');
insert into groups values('e', 'Trivial Players', 'Nightlife', 'Trivia Nights', 27708, 'public', 'We attend Krafthouse Trivia night every Thursday night at 8pm!');

-- populating sample members
insert into members values('1', 'a', TRUE);
insert into members values('1', 'c');
insert into members values('2', 'd', TRUE);
insert into members values('2', 'e');
insert into members values('6', 'a', TRUE);
insert into members values('7', 'b', TRUE);
insert into members values('8', 'a', TRUE);
insert into members values('8', 'c', TRUE);
insert into members values('8', 'd', TRUE);
insert into members values('8', 'e');


--populating sample Events
insert into events values('b', '#a1', 'Talking about animals!', '7', 'West Union', '2019-10-09', '20:00:00', 'public');
insert into events values('a', '#a2', 'First Practice', '6', 'Biddle', '2019-11-10', '12:00:00', 'private');
insert into events values('e', '#a3', 'Marvel Trivia', '2', 'Krafthouse', '2019-12-10', '12:00:00', 'public');

--populating sample attending
insert into attending values('#a3', '0');
insert into attending values('#a3', '1');
insert into attending values('#a3', '2');
insert into attending values('#a3', '3');
insert into attending values('#a3', '4');
insert into attending values('#a3', '5');
insert into attending values('#a3', '6');
insert into attending values('#a3', '7');
insert into attending values('#a3', '8');
insert into attending values('#a2', '6');
insert into attending values('#a2', '1');
insert into attending values('#a1', '7');

-- populating sample requests
insert into requests values('1', 'a', '#b1');
insert into requests values('1', 'c', '#b2');
insert into requests values('2', 'd', '#b3');
insert into requests values('2', 'e', '#b4');
insert into requests values('6', 'a', '#b5');
insert into requests values('7', 'b', '#b6');
insert into requests values('8', 'a', '#b7');
insert into requests values('8', 'c', '#b8');
insert into requests values('8', 'd', '#b9');
insert into requests values('8', 'e', '#b10');
insert into requests values('9', 'c', '#b11');


  --populating sample Messages
insert into messages values('#b1', 'a', '1', 'I can play bass', '2019-10-08', '00:32:00');
insert into messages values('#b2', 'c', '1', 'I can DM a game', '2019-10-09', '00:32:00');
insert into messages values('#b3', 'd', '2', 'I like football', '2019-10-10', '00:32:00');
insert into messages values('#b4', 'e', '2', 'I love triva!', '2019-10-11', '00:32:00');
insert into messages values('#b5', 'a', '6', 'I NEED to start a band', '2019-10-12', '00:32:00');
insert into messages values('#b6', 'b', '7', 'I love animals so much', '2019-10-13', '00:32:00');
insert into messages values('#b7', 'a', '8', 'I play piano', '2019-10-14', '00:32:00');
insert into messages values('#b8', 'c', '8', 'I wanna play DnD', '2019-10-15', '00:32:00');
insert into messages values('#b9', 'd', '8', 'I like watching football', '2019-10-16', '00:32:00');
insert into messages values('#b10', 'e', '8', 'Trivia is great', '2019-10-17', '00:32:00');
insert into messages values('#b11', 'c', '9', 'Hi I really wanna join games!', '2019-10-18', '00:32:00');
