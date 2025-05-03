# Colonnes
## Dans le CSV

iid,id,gender,idg,condtn,wave,round,position,positin1,order,partner,pid,match,int_corr,samerace,age_o,race_o,pf_o_att,pf_o_sin,pf_o_int,pf_o_fun,pf_o_amb,pf_o_sha,dec_o,attr_o,sinc_o,intel_o,fun_o,amb_o,shar_o,like_o,prob_o,met_o,age,field,field_cd,undergra,mn_sat,tuition,race,imprace,imprelig,from,zipcode,income,goal,date,go_out,career,career_c,sports,tvsports,exercise,dining,museums,art,hiking,gaming,clubbing,reading,tv,theater,movies,concerts,music,shopping,yoga,exphappy,expnum,attr1_1,sinc1_1,intel1_1,fun1_1,amb1_1,shar1_1,attr4_1,sinc4_1,intel4_1,fun4_1,amb4_1,shar4_1,attr2_1,sinc2_1,intel2_1,fun2_1,amb2_1,shar2_1,attr3_1,sinc3_1,fun3_1,intel3_1,amb3_1,attr5_1,sinc5_1,intel5_1,fun5_1,amb5_1,dec,attr,sinc,intel,fun,amb,shar,like,prob,met,match_es,attr1_s,sinc1_s,intel1_s,fun1_s,amb1_s,shar1_s,attr3_s,sinc3_s,intel3_s,fun3_s,amb3_s,satis_2,length,numdat_2,attr7_2,sinc7_2,intel7_2,fun7_2,amb7_2,shar7_2,attr1_2,sinc1_2,intel1_2,fun1_2,amb1_2,shar1_2,attr4_2,sinc4_2,intel4_2,fun4_2,amb4_2,shar4_2,attr2_2,sinc2_2,intel2_2,fun2_2,amb2_2,shar2_2,attr3_2,sinc3_2,intel3_2,fun3_2,amb3_2,attr5_2,sinc5_2,intel5_2,fun5_2,amb5_2,you_call,them_cal,date_3,numdat_3,num_in_3,attr1_3,sinc1_3,intel1_3,fun1_3,amb1_3,shar1_3,attr7_3,sinc7_3,intel7_3,fun7_3,amb7_3,shar7_3,attr4_3,sinc4_3,intel4_3,fun4_3,amb4_3,shar4_3,attr2_3,sinc2_3,intel2_3,fun2_3,amb2_3,shar2_3,attr3_3,sinc3_3,intel3_3,fun3_3,amb3_3,attr5_3,sinc5_3,intel5_3,fun5_3,amb5_3

En résumé rapide, ce que contient ce document :
- Identification des participants (iid, id, gender, etc.)
- Contexte de l'événement (wave, condtn, etc.)
- Évaluations pendant les rendez-vous (match, int_corr, age_o, attr_o, etc.)
- Données du formulaire d'inscription (âge, niveau d'études, préférences raciales/religieuses, revenus par code postal, etc.)
- Évaluations d'attributs personnels et attentes vis-à-vis des partenaires (attractivité, sincérité, intelligence, etc.), avec plusieurs phases de mesure (avant, pendant, après).
- Feedback post-événement (satisfaction, nombre de rendez-vous obtenus, poursuite des contacts).

🆔 Identification et organisation des participants
Colonne | Description
|-|-|
iid | Numéro d'identification unique du sujet (participant)
id | Numéro du sujet dans l'onde (wave)
gender | Sexe (0 = Femme, 1 = Homme)
idg | Numéro du sujet par sexe dans la vague
condtn | Condition : 1 = choix limité, 2 = choix étendu
wave | Numéro de la vague (événement)
round | Nombre de personnes rencontrées pendant la vague
position | Station où le participant rencontre le partenaire
positin1 | Station de départ du participant
order | Ordre du rendez-vous ce soir-là
partner | ID du partenaire rencontré ce soir-là
pid | IID du partenaire

## Identification et organisation
- **iid** : Numéro unique du participant
- **id** : Numéro du participant dans l'événement
- **gender** : Sexe (0 = Femme, 1 = Homme)
- **idg** : Numéro dans le genre
- **condtn** : Condition expérimentale (1 = choix limité, 2 = choix étendu)
- **wave** : Numéro de l'événement (vague)
- **round** : Nombre de personnes rencontrées
- **position** : Station de rencontre
- **positin1** : Station de départ
- **order** : Ordre du rendez-vous
- **partner** : ID du partenaire
- **pid** : IID du partenaire

❤️ Résultat du rendez-vous (matching)
Colonne | Description
|-|-|
match | 1 = oui (match réciproque), 0 = non
dec | Décision du participant (1 = oui, 0 = non)
dec_o | Décision du partenaire (1 = oui, 0 = non)
int_corr | Corrélation entre les intérêts (Time 1)
samerace | 1 = même race, 0 = différente

👥 Données sur le partenaire
Colonne | Description
|-|-|
age_o | Âge du partenaire
race_o | Race/ethnie du partenaire
pf_o_att | Préférences déclarées du partenaire pour les 6 attributs
attr_o, sinc_o, intel_o, fun_o, amb_o, shar_o | Évaluation par le partenaire sur l'attractivité, sincérité, intelligence, fun, ambition, centres d'intérêt communs

📝 Inscription / Formulaire initial (Time 1)

Colonne | Description
|-|-|
age | Âge du participant
field | Domaine d'étude (texte)
field_cd | Domaine d'étude (codé 1-18)
undergrd | Université de premier cycle fréquentée
mn_sat | Score SAT médian de l'université
tuition | Frais de scolarité
race | Race/ethnie
imprace | Importance d'être de même race dans le choix d'un partenaire
imprelig | Importance d'avoir la même religion
from | Origine géographique
zipcode | Code postal d'origine
income | Revenu médian du code postal
goal | Objectif de participation
date | Fréquence habituelle de rencontres
go_out | Fréquence de sorties sociales
career | Carrière visée (texte)
career_c | Carrière visée (codée 1-17)

🎯 Préférences et perception de soi (avant le speed-dating)
Colonne | Description
|-|-|
attr1_1, sinc1_1, intel1_1, fun1_1, amb1_1, shar1_1 | Ce que le participant recherche chez un partenaire
attr4_1, sinc4_1, intel4_1, fun4_1, amb4_1, shar4_1 | Ce que le participant pense que les autres recherchent
attr2_1, sinc2_1, intel2_1, fun2_1, amb2_1, shar2_1 | Ce que le participant pense que l'autre sexe recherche
attr3_1, sinc3_1, intel3_1, fun3_1, amb3_1 | Comment le participant s’évalue lui-même
attr5_1, sinc5_1, intel5_1, fun5_1, amb5_1 | Comment le participant pense être perçu par les autres

🧘‍♂️ Centres d'intérêt
(évaluations de 1 à 10)
Colonne | Description
|-|-|
sports, tvsports, excersice, dining, museums, art, hiking, gaming, clubbing, reading, tv, theater, movies, concerts, music, shopping, yoga | Degré d'intérêt pour différentes activités

🙋‍♀️ Évaluation après les rendez-vous (Scorecard)
Colonne | Description
|-|-|
like | Combien on aime la personne rencontrée (1-10)
prob | Probabilité estimée que l'autre dise "oui"
met | Si on connaissait la personne avant (1 = oui, 2 = non)
match_es | Nombre de matchs estimés

📋 Suivi post-événement (Time 2 et Time 3)
Colonne | Description
|-|-|
satis_2 | Satisfaction globale avec les participants rencontrés
length | Jugement sur la durée des rendez-vous
numdat_2 | Jugement sur le nombre de rendez-vous
attr1_2, sinc1_2, intel1_2, fun1_2, amb1_2, shar1_2 | Préférences après l’événement
attr7_2, attr4_2, attr2_2, attr3_2, attr5_2 | Réévaluations des préférences et perceptions
you_call, them_cal | Combien de contacts ont été pris après
date_3, numdat_3, num_in_3 | Combien de rencontres post-speed-dating ont eu lieu
attr1_3, attr7_3, attr4_3, attr2_3, attr3_3, attr5_3 | Réévaluation finale après plusieurs semaines

# Speed Dating Dataset - Dictionnaire des Colonnes

## Identification et organisation
- **iid** : Numéro unique du participant
- **id** : Numéro du participant dans l'événement
- **gender** : Sexe (0 = Femme, 1 = Homme)
- **idg** : Numéro dans le genre
- **condtn** : Condition expérimentale (1 = choix limité, 2 = choix étendu)
- **wave** : Numéro de l'événement (vague)
- **round** : Nombre de personnes rencontrées
- **position** : Station de rencontre
- **positin1** : Station de départ
- **order** : Ordre du rendez-vous
- **partner** : ID du partenaire
- **pid** : IID du partenaire

## Résultat du rendez-vous
- **match** : Match réciproque (1 = oui, 0 = non)
- **dec** : Décision du participant
- **dec_o** : Décision du partenaire
- **int_corr** : Corrélation d’intérêts
- **samerace** : Même race (1 = oui, 0 = non)

## Caractéristiques du partenaire
- **age_o** : Âge du partenaire
- **race_o** : Race du partenaire
- **pf_o_att** : Préférences déclarées du partenaire
- **attr_o**, **sinc_o**, **intel_o**, **fun_o**, **amb_o**, **shar_o** : Évaluations faites par le partenaire

## Informations personnelles (Time 1)
- **age** : Âge
- **field** : Domaine d’étude
- **field_cd** : Domaine codé
- **undergrd** : Université de premier cycle
- **mn_sat** : SAT médian
- **tuition** : Frais de scolarité
- **race** : Race
- **imprace** : Importance de la race
- **imprelig** : Importance de la religion
- **from** : Origine géographique
- **zipcode** : Code postal
- **income** : Revenu par code postal
- **goal** : Objectif de participation
- **date** : Fréquence de rencontres
- **go_out** : Fréquence de sorties
- **career** : Carrière souhaitée
- **career_c** : Carrière codée

## Préférences et perception de soi
- **attr1_1** à **shar1_1** : Importance des qualités recherchées
- **attr4_1** à **shar4_1** : Ce que pensent rechercher les autres
- **attr2_1** à **shar2_1** : Ce que pense rechercher l’autre sexe
- **attr3_1** à **amb3_1** : Auto-évaluation
- **attr5_1** à **amb5_1** : Comment on pense être perçu

## Centres d’intérêt
- **sports**, **tvsports**, **excersice**, **dining**, **museums**, **art**, **hiking**, **gaming**, **clubbing**, **reading**, **tv**, **theater**, **movies**, **concerts**, **music**, **shopping**, **yoga** : Activités et loisirs

## Feedback pendant l'événement
- **like** : Degré d’appréciation d’un partenaire
- **prob** : Probabilité estimée que le partenaire dise oui
- **met** : Connaissance antérieure du partenaire
- **match_es** : Nombre estimé de matchs

## Suivi post-événement (Time 2, Time 3)
- **satis_2**, **length**, **numdat_2** : Satisfaction, longueur, nombre de rendez-vous
- **you_call**, **them_cal** : Suivi des contacts
- **date_3**, **numdat_3**, **num_in_3** : Dates effectives
- **attr1_2**, **attr7_2**, **attr4_2**, **attr2_2**, **attr3_2**, **attr5_2** : Réévaluation après l'événement
- **attr1_3**, **attr7_3**, **attr4_3**, **attr2_3**, **attr3_3**, **attr5_3** : Réévaluation 3-4 semaines après



attr, sinc, intel, fun, amb, shar:
1_1: We want to know what you look for in the opposite sex / Please rate the importance of the following attributes in a potential date
4_1: Now we want to know what you think MOST of your fellow men/women look for in the opposite sex.

2_1: What do you think the opposite sex looks for in a date?

3_1: How do you think you measure up? Please rate your opinion of your own attributes

5_1: And finally, how do you think others perceive you? Please rate yourself how you think others would rate you on each of the following attributes


Half way through meeting all potential dates during the night of the event on their scorecard: Hold up!  Now that you are half way through your Speed Dates, we have a few questions for you…

1_s: Please rate the importance of the following attributes in a potential date on
3_s: Please rate your opinion of your own attributes

followup/Time2:
[Survey is filled out the day after participating in the event.  Subjects must have submitted this in order to be sent their matches.]

satis_2: Overall, how satisfied were you with the people you met? (1=not at all satisfied, 10=extremely satisfied)

length: Four minutes is: Too little=1 / Too much=2 /Just Right=3
numdat_2: The number of Speed "Dates" you had was: Too few=1 / Too many=2

7_2: Now, think back to your yes/no decisions during the Speed Dating event.  Try to distribute the 100 points among these six attributes in the way that best reflects the actual importance of these attributes in your decisions. Give more points to those attributes that were more important in your decisions, and fewer points to those attributes that were less important in your decisions.  Total points must equal 100. 

1_2: We want to know what you look for in the opposite sex

4_2: What do you think MOST of your fellow men/women look for in the opposite sex?
2_2: What do you think the opposite sex looks for in a date?
3_2: How do you think you measure up?
5_2: And finally, how do you think others perceive you?

followup2/ Time3:
[Subjects filled out 3-4 weeks after they had been sent their matches]


1.  Of the matches that you received:
you_call: 
(a) How many have you contacted to set up a date?
them_cal:
(b) How many have contacted you?

date_3:
Have you been on a date with any of your matches?
	Yes=1
	No=2

If you have been on at least one date, please answer the following:
numdat_3: 
(a) How many of your matches have you been on a date with so far?
num_in_3
If yes, how many?

Waves 6-9: Please rate the importance of the following attributes in a potential date on a scale of 1-10 (1=not at all important, 10=extremely important):
Waves 1-5, 10-21: You have 100 points to distribute among the following attributes -- give more points to those attributes that are more important in a potential date, and fewer points to those attributes that are less important in a potential date.  Total points must equal 100.

1_3: What do you look for in the opposite sex?
7_3: Now, think back to your yes/no decisions during the night of the Speed Dating event.  Try to distribute the 100 points among these six attributes in the way that best reflects the actual importance of these attributes in your decisions

4_3: Now we want to know what you think MOST of your fellow men/women look for in the opposite sex. 

2_3: What do you think the opposite sex looks for in a date? 
3_3: Please rate your opinion of your own attributes,
5_3: And finally, how do you think others perceive you?
